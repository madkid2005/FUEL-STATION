$(document).ready(function() {
    $('#id_gasoline_nozzles').change(function() {
        var count = $(this).val();
        updateNozzleFormset('gasoline', count);
    });

    $('#id_gas_nozzles').change(function() {
        var count = $(this).val();
        updateNozzleFormset('gas', count);
    });

    $('#id_gasoline_tanks').change(function() {
        var count = $(this).val();
        updateTankFormset('gasoline', count);
    });

    $('#id_gas_tanks').change(function() {
        var count = $(this).val();
        updateTankFormset('gas', count);
    });

    function updateNozzleFormset(type, count) {
        var formset = $('#' + type + '_nozzle_formset');
        formset.empty();
        for (var i = 0; i < count; i++) {
            var form = $('<div>').append(
                $('<label>').text('شماره نازل ' + (i + 1) + ' پایان توتالایزر'),
                $('<input>').attr({
                    'type': 'number',
                    'name': type + '_nozzle-' + i + '-totalizer_start',
                    'id': 'id_' + type + '_nozzle-' + i + '-totalizer_start'
                }),
                $('<label>').text('شماره نازل ' + (i + 1) + ' شروع توتالایزر'),
                $('<input>').attr({
                    'type': 'number',
                    'name': type + '_nozzle-' + i + '-totalizer_end',
                    'id': 'id_' + type + '_nozzle-' + i + '-totalizer_end'
                }),
                $('<input>').attr({
                    'type': 'hidden',
                    'name': type + '_nozzle-' + i + '-nozzle_number',
                    'value': (i + 1)
                }),
                $('<input>').attr({
                    'type': 'hidden',
                    'name': type + '_nozzle-' + i + '-station',
                    'value': ''
                })
            );
            formset.append(form);
        }
    }

    function updateTankFormset(type, count) {
        var formset = $('#' + type + '_tank_formset');
        formset.empty();
        for (var i = 0; i < count; i++) {
            var form = $('<div>').append(
                $('<label>').text('شماره مخزن ' + (i + 1) + ' موجودی نهایی'),
                $('<input>').attr({
                    'type': 'number',
                    'name': type + '_tank-' + i + '-final_stock',
                    'id': 'id_' + type + '_tank-' + i + '-final_stock'
                }),
                $('<input>').attr({
                    'type': 'hidden',
                    'name': type + '_tank-' + i + '-tank_number',
                    'value': (i + 1)
                }),
                $('<input>').attr({
                    'type': 'hidden',
                    'name': type + '_tank-' + i + '-station',
                    'value': ''
                })
            );
            formset.append(form);
        }
    }

    function calculateTotals() {
        var gasolineTotal = 0;
        $('#gasoline_nozzle_formset input[id^="id_gasoline_nozzle-"]').each(function(index) {
            var totalizerStart = parseFloat($('#id_gasoline_nozzle-' + index + '-totalizer_start').val()) || 0;
            var totalizerEnd = parseFloat($('#id_gasoline_nozzle-' + index + '-totalizer_end').val()) || 0;
            gasolineTotal += (totalizerEnd - totalizerStart);
        });

        var gasTotal = 0;
        $('#gas_nozzle_formset input[id^="id_gas_nozzle-"]').each(function(index) {
            var totalizerStart = parseFloat($('#id_gas_nozzle-' + index + '-totalizer_start').val()) || 0;
            var totalizerEnd = parseFloat($('#id_gas_nozzle-' + index + '-totalizer_end').val()) || 0;
            gasTotal += (totalizerEnd - totalizerStart);
        });

        $('#gasoline_total').text('مجموع بنزین: ' + gasolineTotal);
        $('#gas_total').text('مجموع گاز: ' + gasTotal);
    }

    // Recalculate totals when input values change
    $(document).on('input', 'input[id^="id_gasoline_nozzle-"], input[id^="id_gas_nozzle-"]', calculateTotals);
});