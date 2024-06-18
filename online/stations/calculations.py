

# mohasebe FOrosh mekaniki - totalizer2 - totalizer1
def calculate_gasoline_total_volume(nozzles_data):
    total_volume = 0
    for nozzle in nozzles_data:
        totalizer_start = float(nozzle.get('totalizer_start', 0))
        totalizer_end = float(nozzle.get('totalizer_end', 0))
        total_volume += totalizer_end - totalizer_start
    return total_volume

def calculate_gas_total_volume(nozzles_data):
    total_volume = 0
    for nozzle in nozzles_data:
        totalizer_start = float(nozzle.get('totalizer_start', 0))
        totalizer_end = float(nozzle.get('totalizer_end', 0))
        total_volume += totalizer_end - totalizer_start
    return total_volume