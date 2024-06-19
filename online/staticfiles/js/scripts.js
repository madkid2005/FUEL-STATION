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
// -----------------------------------------------------------------------------------------

// .......... base.html

document.addEventListener('DOMContentLoaded', function() {
    var activeButtonId = localStorage.getItem('activeButtonId');
    if (activeButtonId) {
        var activeButton = document.querySelector(`.btn-change-color[data-id="${activeButtonId}"] i`);
        var activeText = document.querySelector(`.btn-change-color[data-id="${activeButtonId}"]`).parentElement.nextElementSibling;
        if (activeButton) {
            activeButton.classList.remove('default-color');
            activeButton.classList.add('orange-color');
        }
        if (activeText) {
            activeText.classList.remove('default-color');
            activeText.classList.add('orange-color');
        }
    }
});

document.querySelectorAll('.btn-change-color').forEach(function(element) {
    element.addEventListener('click', function(event) {
        document.querySelectorAll('.btn-change-color i').forEach(function(icon) {
            icon.classList.remove('orange-color');
            icon.classList.add('default-color');
        });
        document.querySelectorAll('.text-colorforbuy').forEach(function(text) {
            text.classList.remove('orange-color');
            text.classList.add('default-color');
        });

        var icon = this.querySelector('i');
        var text = this.parentElement.nextElementSibling;
        if (icon) {
            icon.classList.remove('default-color');
            icon.classList.add('orange-color');
        }
        if (text) {
            text.classList.remove('default-color');
            text.classList.add('orange-color');
        }

        var buttonId = this.getAttribute('data-id');
        localStorage.setItem('activeButtonId', buttonId);
    });
});

// ............. station form 

document.getElementById('showGas').addEventListener('click', function() {
    var allElements = document.querySelectorAll('.basehide, .GazoiilShow, .allShow');
    allElements.forEach(function(element) {
      element.style.display = 'none';
    });
    var gasElements = document.querySelectorAll('.GazShow');
    gasElements.forEach(function(element) {
      element.style.display = 'block';
    });
  });

  document.getElementById('showGasoiil').addEventListener('click', function() {
    var allElements = document.querySelectorAll('.basehide, .GazShow, .allShow');
    allElements.forEach(function(element) {
      element.style.display = 'none';
    });
    var gasoiilElements = document.querySelectorAll('.GazoiilShow');
    gasoiilElements.forEach(function(element) {
      element.style.display = 'block';
    });
  });

  document.getElementById('showAll').addEventListener('click', function() {
    var allElements = document.querySelectorAll('.basehide, .GazShow, .GazoiilShow');
    allElements.forEach(function(element) {
      element.style.display = 'none';
    });
    var allShowElements = document.querySelectorAll('.allShow');
    allShowElements.forEach(function(element) {
      element.style.display = 'block';
    });
  });

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

//  ......... station list 
