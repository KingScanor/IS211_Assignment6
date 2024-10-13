#Assignment 6 / Conversions

def convertCelsiusToKelvin(celsius):
    """Celsius to Kelvin"""
    kelvin = celsius + 273.15
    return kelvin

def convertCelsiusToFahrenheit(celsius):
    """Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convertKelvinToCelsius(kelvin):
    """Kelvin to Celsius"""
    celsius = kelvin - 273.15
    return celsius

def convertKelvinToFahrenheit(kelvin):
    """Kelvin to Fahrenheit"""
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Fahrenheit to Kelvin"""
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin