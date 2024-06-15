from django.shortcuts import render, redirect
from .forms import FuelStationForm, GasolineNozzleFormSet, GasNozzleFormSet
from .models import FuelStation, GasolineNozzle, GasNozzle, GasolineTank, GasTank
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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
            for i in range(gasoline_nozzles_count):
                GasolineNozzle.objects.create(
                    station=station,
                    nozzle_number=i+1,
                    totalizer_start=request.POST.get(f'gasoline_nozzle-{i}-totalizer_start'),
                    totalizer_end=request.POST.get(f'gasoline_nozzle-{i}-totalizer_end')
                )
                
            # Save gas nozzles
            for i in range(gas_nozzles_count):
                GasNozzle.objects.create(
                    station=station,
                    nozzle_number=i+1,
                    totalizer_start=request.POST.get(f'gas_nozzle-{i}-totalizer_start'),
                    totalizer_end=request.POST.get(f'gas_nozzle-{i}-totalizer_end')
                )
                
            # Save gasoline tanks
            gasoline_final_stock = 0
            for i in range(gasoline_tanks_count):
                tank_number = i + 1
                final_stock = request.POST.get(f'gasoline_tank-{i}-final_stock')
                GasolineTank.objects.create(
                    station=station,
                    tank_number=tank_number,
                    final_stock=final_stock
                )
                if final_stock:
                    gasoline_final_stock += float(final_stock)

            # Save gas tanks
            gas_final_stock = 0
            for i in range(gas_tanks_count):
                tank_number = i + 1
                final_stock = request.POST.get(f'gas_tank-{i}-final_stock')
                GasTank.objects.create(
                    station=station,
                    tank_number=tank_number,
                    final_stock=final_stock
                )
                if final_stock:
                    gas_final_stock += float(final_stock)
                    
            # Update station with final stocks
            station.gasoline_final_stock = gasoline_final_stock
            station.gas_final_stock = gas_final_stock
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

def generate_pdf(request, pk):
    station = FuelStation.objects.get(pk=pk)
    template_path = 'station_pdf.html'
    context = {'station': station}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="station_{station.id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
