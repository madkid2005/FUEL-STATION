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
                $('<label>').text('Nozzle ' + (i + 1) + ' Totalizer Start'),
                $('<input>').attr({
                    'type': 'number',
                    'name': type + '_nozzle-' + i + '-totalizer_start',
                    'id': 'id_' + type + '_nozzle-' + i + '-totalizer_start'
                }),
                $('<label>').text('Nozzle ' + (i + 1) + ' Totalizer End'),
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
                $('<label>').text('Tank ' + (i + 1) + ' Final Stock'),
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
});