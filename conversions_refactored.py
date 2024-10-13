#Assignment 6 / Conversions Refactored

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):

#To itself
    if fromUnit == toUnit:
        return value

#Temperature
    if fromUnit == "Celsius":
        if toUnit == "Kelvin":
            return value + 273.15
        elif toUnit == "Fahrenheit":
            return (value * 9 / 5) + 32
        else:
            raise ConversionNotPossible(f" It is impossible to convert from {fromUnit} to {toUnit}.")
    elif fromUnit == "Fahrenheit":
        if toUnit == "Celsius":
            return (value - 32) * 5 / 9
        elif toUnit == "Kelvin":
            return (value - 32) * 5 / 9 + 273.15
        else:
            raise ConversionNotPossible(f" It is impossible to convert from {fromUnit} to {toUnit}.")
    elif fromUnit == "Kelvin":
        if toUnit == "Celsius":
            return value - 273.15
        elif toUnit == "Fahrenheit":
            return (value * 9 / 5) - 459.67
        else:
            raise ConversionNotPossible(f" It is impossible to convert from {fromUnit} to {toUnit}.")

# Distance
    elif fromUnit == "Miles":
        if toUnit == "Yards":
            return value * 1760
        elif toUnit == "Meters":
            return value * 1609.34
        else:
            raise ConversionNotPossible(f" It is impossible to convert from {fromUnit} to {toUnit}.")
    elif fromUnit == "Yards":
        if toUnit == "Miles":
            return value / 1760
        elif toUnit == "Meters":
            return value * 0.9144
        else:
            raise ConversionNotPossible(f" It is impossible to convert from {fromUnit} to {toUnit}.")
    elif fromUnit == "Meters":
        if toUnit == "Miles":
            return value / 1609.34
        elif toUnit == "Yards":
            return value / 0.9144
        else:
            raise ConversionNotPossible(f" It is impossible to convert from {fromUnit} to {toUnit}.")



