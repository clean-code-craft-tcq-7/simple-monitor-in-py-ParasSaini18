def temperature_check(temperature):
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    return True
def soc_check(soc):
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    return True
def charge_rate_check(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True    
def battery_is_ok(temperature, soc, charge_rate):
    if temperature_check(temperature) == False or soc_check(soc) == False or charge_rate_check(charge_rate) == False:
        return False
    return True