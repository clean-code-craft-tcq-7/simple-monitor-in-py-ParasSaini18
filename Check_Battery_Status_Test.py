import Check_Battery_Status

def test_battery_is_ok():
    assert(Check_Battery_Status.battery_is_ok(-0.1, 70, 0.8) is False)
    assert(Check_Battery_Status.battery_is_ok(50, 70, 0.8) is False)
    assert(Check_Battery_Status.battery_is_ok(40, 19, 0.8) is False)
    assert(Check_Battery_Status.battery_is_ok(35, 81, 0.8) is False)
    assert(Check_Battery_Status.battery_is_ok(20, 70, 0.9) is False)
    assert(Check_Battery_Status.battery_is_ok(25, 70, 0.7) is True)

if __name__ == '__main__':
    test_battery_is_ok()