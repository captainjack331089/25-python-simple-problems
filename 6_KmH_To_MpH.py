"""
This simple program is to convert between Km/h and mile/h
The formation between kmh and mh is kmh = mh * 1.6
"""

def speed_Convert(speed, unit, valid_unit):
    #valid_unit = ['km/h', 'kilometer/hour', 'mile/h', 'm/h']
    if unit == valid_unit[0] or unit == valid_unit[1]:
        old_unit = valid_unit[0]
        new_speed = speed * 1.6
        new_unit = valid_unit[3]
    else:
        old_unit = valid_unit[3]
        new_speed = speed /  1.6
        new_unit = valid_unit[0]
    return (new_speed, old_unit, new_unit)


if __name__ == '__main__':
    speed = 'a'
    while type(speed) is not float:
        speed = float(input('Please enter the your speed: '))
    unit = 'a'
    valid_unit = ['km/h', 'kilometer/hour', 'mile/h', 'm/h']
    while unit not in valid_unit:
        unit = input('Please enter the unit(km/h or m/h):  ')
        unit.lower()

    new_speed, old_unit, new_unit = speed_Convert(speed, unit, valid_unit)
    print('%.2f %s -- > %.2f %s' %(speed, old_unit, new_speed, new_unit))