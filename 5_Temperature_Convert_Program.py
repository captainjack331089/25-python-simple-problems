"""
This simple program is to convert between Celsius and Fahrenheit
The formation between C and F is: F = C * 1.8 + 32
"""



def temperature_Convert(degree, unit, valid_unit):
    if unit == valid_unit[0] or unit == valid_unit[1]:
        old_unit = valid_unit[1]
        new_degree = degree * 1.8 + 32
        new_unit = valid_unit[3]
    else:
        old_unit = valid_unit[3]
        new_degree = (degree - 32) / 1.8
        new_unit = valid_unit[1]
    return (new_degree, old_unit, new_unit)


if __name__ == '__main__':
    degree = 'a'
    while type(degree) is not float:
        degree = float(input('Please enter the Degree Number: '))
    unit = 'a'
    valid_unit = ['c', 'celsius', 'f', 'fahrenheit']
    while unit not in valid_unit:
        unit = input('Please enter the unit(C/F):  ')
        unit.lower()

    new_degree, old_unit, new_unit = temperature_Convert(degree, unit, valid_unit)
    print('%.2f %s -- > %.2f %s' %(degree, old_unit, new_degree, new_unit))