from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.fonts import addMapping
import arabic_reshaper
from bidi.algorithm import get_display




from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .forms import FuelStationForm, GasolineNozzleFormSet, GasNozzleFormSet
from .models import FuelStation, GasolineNozzle, GasNozzle, GasolineTank, GasTank
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .calculations import calculate_gasoline_total_volume, calculate_gas_total_volume

def create_station(request):
    if request.method == 'POST':
        form = FuelStationForm(request.POST)
        if form.is_valid():
            station = form.save()
            
            # nozzles
            gasoline_nozzles_count = station.gasoline_nozzles
            gas_nozzles_count = station.gas_nozzles
            
            #tanks
            gasoline_tanks_count = station.gasoline_tanks
            gas_tanks_count = station.gas_tanks
            
            
            # Save gasoline nozzles
            gasoline_nozzles_data = []

            for i in range(gasoline_nozzles_count):
                
                totalizer_start = request.POST.get(f'gasoline_nozzle-{i}-totalizer_start')
                totalizer_end = request.POST.get(f'gasoline_nozzle-{i}-totalizer_end')
                
                
                GasolineNozzle.objects.create(
                    station=station,
                    nozzle_number=i+1,
                    totalizer_start=request.POST.get(f'gasoline_nozzle-{i}-totalizer_start'),
                    totalizer_end=request.POST.get(f'gasoline_nozzle-{i}-totalizer_end')
                )
                
                gasoline_nozzles_data.append({
                    'totalizer_start': totalizer_start,
                    'totalizer_end': totalizer_end
                })
                
            # Calculate total volume for gasoline nozzles
            gasoline_total_volume = calculate_gasoline_total_volume(gasoline_nozzles_data)
                
            # Save gas nozzles  and prepare data for calculation
            gas_nozzles_data = []

            for i in range(gas_nozzles_count):
                
                totalizer_start = request.POST.get(f'gas_nozzle-{i}-totalizer_start')
                totalizer_end = request.POST.get(f'gas_nozzle-{i}-totalizer_end')
                
                GasNozzle.objects.create(
                    station=station,
                    nozzle_number=i+1,
                    totalizer_start=totalizer_start,
                    totalizer_end=totalizer_end
                )
                
                
                gas_nozzles_data.append({
                    'totalizer_start': totalizer_start,
                    'totalizer_end': totalizer_end
                })
                
            # Calculate total volume for gas nozzles
            gas_total_volume = calculate_gas_total_volume(gas_nozzles_data)
                
            # Save gasoline tanks
            gasoline_final_stock = 0
            for i in range(gasoline_tanks_count):
                tank_number = i + 1
                final_stock = float(request.POST.get(f'gasoline_tank-{i}-final_stock', 0))
                GasolineTank.objects.create(
                    station=station,
                    tank_number=tank_number,
                    final_stock=final_stock
                )
                
                gasoline_final_stock += final_stock


            # Save gas tanks
            gas_final_stock = 0
            for i in range(gas_tanks_count):
                tank_number = i + 1
                final_stock = float(request.POST.get(f'gas_tank-{i}-final_stock', 0))
                GasTank.objects.create(
                    station=station,
                    tank_number=tank_number,
                    final_stock=final_stock
                )
                
                gas_final_stock += final_stock

                    
            # Update station with final stocks
            station.gasoline_final_stock = gasoline_final_stock
            station.gas_final_stock = gas_final_stock
            
            station.gasoline_total_volume = gasoline_total_volume
            station.gas_total_volume = gas_total_volume
            
            station.save()

            return redirect('station_list')
    else:
        form = FuelStationForm()

    return render(request, 'station_form.html', {
        'form': form,
    })
    
    
    
def station_list(request):
    stations = FuelStation.objects.all()
    return render(request, 'station_list.html', {'stations': stations})

def station_detail(request, pk):
    station = FuelStation.objects.get(pk=pk)
    gasoline_nozzles = station.gasoline_nozzles_details.all()
    gas_nozzles = station.gas_nozzles_details.all()
    return render(request, 'station_detail.html', {'station': station, 'gasoline_nozzles': gasoline_nozzles, 'gas_nozzles': gas_nozzles})

import os
from django.conf import settings

def generate_pdf(request, pk):
    station = get_object_or_404(FuelStation, pk=pk)

    # محاسبات نهایی برای نازل‌های بنزین
    gasoline_nozzles = station.gasoline_nozzles_details.all()
    gasoline_total = sum([(nozzle.totalizer_end - nozzle.totalizer_start) for nozzle in gasoline_nozzles])

    # محاسبات نهایی برای نازل‌های گاز
    gas_nozzles = station.gas_nozzles_details.all()
    gas_total = sum([(nozzle.totalizer_end - nozzle.totalizer_start) for nozzle in gas_nozzles])

    # محاسبه‌ی جدید: حذف کامل محصول از ایستگاه
    gasoline_entire_product_removed = (station.gasoline_initial_stock or 0) + (station.gasoline_received or 0) - (station.gasoline_final_stock or 0)

    template_path = 'station_pdf.html'
    context = {
        'station': station,
        'gasoline_total': gasoline_total,
        'gas_total': gas_total,
        'gasoline_entire_product_removed': gasoline_entire_product_removed,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="station_{station.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    
    # تنظیمات فونت
    font_path = os.path.join(settings.BASE_DIR, 'static/fonts/Vazir.ttf')
    pisa_status = pisa.CreatePDF(
        html, dest=response,
        encoding='UTF-8',
        link_callback=lambda uri, rel: font_path if uri == 'static/fonts/Vazir.ttf' else uri
    )

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)    # shape the text
    bidi_text = get_display(reshaped_text)           # correct its direction
    return bidi_text

def generate_pdf_reportlab(request, pk):
    station = FuelStation.objects.get(pk=pk)
    
    # Fetch control period dates
    start_date = station.start_date if station.control_period == 'start' else None
    end_date = station.end_date if station.control_period == 'end' else None
    
    # محاسبه فروش کل بنزین
    total_gasoline_sales = sum([
        abs(nozzle.totalizer_end - nozzle.totalizer_start) 
        for nozzle in station.gasoline_nozzles_details.all()
    ])
    
    # محاسبه فروش کل گاز
    total_gas_sales = sum([
        abs(nozzle.totalizer_end - nozzle.totalizer_start) 
        for nozzle in station.gas_nozzles_details.all()
    ])
    
    # تبدیل مقادیر None به صفر
    gasoline_initial_stock = station.gasoline_initial_stock or 0
    gasoline_received = station.gasoline_received or 0
    gasoline_final_stock = station.gasoline_final_stock or 0
    gas_initial_stock = station.gas_initial_stock or 0
    gas_received = station.gas_received or 0
    gas_final_stock = station.gas_final_stock or 0
    
    # محاسبه محصول برداشته شده از جایگاه
    total_gasoline_removed = abs((gasoline_initial_stock + gasoline_received) - gasoline_final_stock)
    total_gas_removed = abs((gas_initial_stock + gas_received) - gas_final_stock)
    
    # محاسبه کسری یا سرک
    gasoline_deficit = total_gasoline_removed - total_gasoline_sales
    gas_deficit = total_gas_removed - total_gas_sales
    
    # محاسبه کسری غیرمجاز
    unauthorized_deficit = None
    if station.product_type in ['gasoline', 'both']:
        if gasoline_deficit > 0:
            unauthorized_deficit = (total_gasoline_sales * 0.0045) - gasoline_deficit
        else:
            unauthorized_deficit = 0
    
    # محاسبه اختلاف فروش مکانیکال و الکترونیکی
    mechanical_electronic_sales_diff = station.gasoline_electronic_sales - total_gasoline_sales
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    
    # ثبت فونت فارسی
    pdfmetrics.registerFont(TTFont('Vazirmatn-Black', 'static/fonts/Vazirmatn-Black.ttf'))
    addMapping('Vazirmatn-Black', 0, 0, 'Vazirmatn-Black')
    
    # تغییر سبک‌های پیش‌فرض به فونت فارسی
    styles['Title'].fontName = 'Vazirmatn-Black'
    styles['Normal'].fontName = 'Vazirmatn-Black'
    
    elements = []
    
    # نمایش اطلاعات جایگاه سوخت
    elements.append(Paragraph(reshape_text(f'اسم جایگاه: {station.name}'), styles['Title']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(reshape_text(f'تعداد نازل‌های بنزین: {station.gasoline_nozzles}'), styles['Normal']))
    elements.append(Paragraph(reshape_text(f'تعداد نازل‌های گاز: {station.gas_nozzles}'), styles['Normal']))
    elements.append(Paragraph(reshape_text(f'تعداد مخازن بنزین: {station.gasoline_tanks}'), styles['Normal']))
    elements.append(Paragraph(reshape_text(f'تعداد مخازن گاز: {station.gas_tanks}'), styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # نمایش مقادیر محاسباتی
    elements.append(Paragraph(reshape_text(f'فروش کل بنزین: {total_gasoline_sales} لیتر'), styles['Normal']))
    elements.append(Paragraph(reshape_text(f'فروش کل گاز: {total_gas_sales} لیتر'), styles['Normal']))
    elements.append(Spacer(1, 12))
    
    elements.append(Paragraph(reshape_text(f'کل محصول بنزین برداشته شده از جایگاه: {total_gasoline_removed} لیتر'), styles['Normal']))
    elements.append(Paragraph(reshape_text(f'کل محصول گاز برداشته شده از جایگاه: {total_gas_removed} لیتر'), styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # نمایش کسری یا سرک
    if gasoline_deficit < 0:
        elements.append(Paragraph(reshape_text(f'سرک بنزین: {abs(gasoline_deficit)} لیتر'), styles['Normal']))
    else:
        elements.append(Paragraph(reshape_text(f'کسری بنزین: {gasoline_deficit} لیتر'), styles['Normal']))
        
    if gas_deficit < 0:
        elements.append(Paragraph(reshape_text(f'سرک گاز: {abs(gas_deficit)} لیتر'), styles['Normal']))
    else:
        elements.append(Paragraph(reshape_text(f'کسری گاز: {gas_deficit} لیتر'), styles['Normal']))
    
    # نمایش اختلاف فروش مکانیکال و الکترونیکی
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(reshape_text(f'اختلاف فروش مکانیکال و الکترونیکی بنزین: {mechanical_electronic_sales_diff} لیتر'), styles['Normal']))
    
    # نمایش کسری غیرمجاز
    if unauthorized_deficit is not None:
        elements.append(Spacer(1, 12))
        if unauthorized_deficit > 0:
            elements.append(Paragraph(reshape_text(f'کسری غیرمجاز: {unauthorized_deficit} لیتر'), styles['Normal']))
        else:
            elements.append(Paragraph(reshape_text(f'کسری غیرمجاز: ۰ لیتر'), styles['Normal']))
    
    # اضافه کردن اطلاعات اضافی از کاربر به فایل PDF
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(reshape_text('اطلاعات اضافی از کاربر:'), styles['Title']))
    
    additional_info = [
        ('موجودی اول دوره بنزین:', f'{gasoline_initial_stock}'),
        ('مقدار رسیده دوره بنزین:', f'{gasoline_received}'),
        ('موجودی انتهای دوره بنزین:', f'{gasoline_final_stock}'),
        ('موجودی اول دوره گاز:', f'{gas_initial_stock}'),
        ('مقدار رسیده دوره گاز:', f'{gas_received}'),
        ('موجودی انتهای دوره گاز:', f'{gas_final_stock}'),
    ]
    
    for info in additional_info:
        elements.append(Paragraph(reshape_text(f'{info[0]} {info[1]}'), styles['Normal']))
    
    # نمایش دوره کنترل
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(reshape_text('دوره کنترل:'), styles['Title']))
    if start_date:
        elements.append(Paragraph(reshape_text(f'از تاریخ: {start_date}'), styles['Normal']))
    if end_date:
        elements.append(Paragraph(reshape_text(f'تا تاریخ: {end_date}'), styles['Normal']))
    
    doc.build(elements)
    buffer.seek(0)
    
    return HttpResponse(buffer, content_type='application/pdf')