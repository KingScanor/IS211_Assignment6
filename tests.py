#Assignment 6 / Tests
import unittest
from conversions import *
from conversions_refactored import *


class CelsiusConvertionTest(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        print("Testing convertCelsiusToKelvin...")
        self.assertAlmostEqual(convertCelsiusToKelvin(300.00), 573.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(565.00), 838.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(200.00), 473.15, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0.00, places=2)
        self.assertAlmostEqual(convertCelsiusToKelvin(150.00), 423.15, places=2)

    def test_convertCelsiusToFahrenheit(self):
        print("Testing convertCelsiusToFahrenheit...")
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300.00), 572.00, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(565.00), 1049.00, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(200.00), 392.00, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-273.15), -459.67, places=2)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(150.00), 302.00, places=2)

class KelvinConvertionTest(unittest.TestCase):
    def test_convertKelvinToCelsius(self):
        print ("Testing convertKelvinToCelsius...")
        self.assertAlmostEqual(convertKelvinToCelsius(573.15), 300.00, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(838.15), 565.00, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(473.15), 200.00, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(0.00), -273.15, places=2)
        self.assertAlmostEqual(convertKelvinToCelsius(423.15), 150.00, places=2)

    def test_convertKelvinToFahrenheit(self):
        print ("Testing convertKelvinToFahrenheit...")
        self.assertAlmostEqual(convertKelvinToFahrenheit(456.25), 361.58, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(260.00), 8.33, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(359.00), 186.53, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(489.00), 420.53, places=2)
        self.assertAlmostEqual(convertKelvinToFahrenheit(685.45), 774.14, places=2)

class FahrenheitConvertionTest(unittest.TestCase):
    def test_convertionFahrenheitToCelsius(self):
        print ("Testing convertFahrenheitToCelsius...")
        self.assertAlmostEqual(convertFahrenheitToCelsius(100.58), 38.1, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(259.00), 126.11, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(450.00), 232.22, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(625.00), 329.44, places=2)
        self.assertAlmostEqual(convertFahrenheitToCelsius(155.00), 68.33, places=2)

    def test_convertFahrenheitToKelvin(self):
        print ("Testing convertFahrenheitToKelvin...")
        self.assertAlmostEqual(convertFahrenheitToKelvin(100.00), 310.9278, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(458.00), 509.8167, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(000.00), 255.3722, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(456.25), 508.8444, places=2)
        self.assertAlmostEqual(convertFahrenheitToKelvin(159.00), 343.7056, places=2)

class TestRefactoredConversions(unittest.TestCase):
    def test_temperature(self):
        print("Testing temperature conversions..")
        self.assertAlmostEqual(convert("Celsius", "Kelvin", 300.00),573.15, places=2)
        self.assertAlmostEqual(convert("Kelvin", "Celsius", 838.15), 565.00, places=2)
        self.assertAlmostEqual(convert("Fahrenheit", "Kelvin", 100.00), 310.9278, places=2)
        self.assertAlmostEqual(convert("Celsius", "Fahrenheit", 159.00), 318.2, places=2)
        self.assertAlmostEqual(convert("Fahrenheit", "Celsius", 120.00),  48.8889, places=2)

    def test_distance(self):
        print ("Testing distance conversions...")
        self.assertAlmostEqual(convert("Miles", "Yards", 10.00), 17600.00, places=2)
        self.assertAlmostEqual(convert("Yards", "Miles", 10780.00), 6.125, places=2)
        self.assertAlmostEqual(convert("Miles", "Meters", 100.00), 160934.0, places=2)
        self.assertAlmostEqual(convert("Meters", "Yards", 100.00), 109.36133, places=2)
        self.assertAlmostEqual(convert("Yards", "Meters", 1000.00), 914.4, places=2)

    def test_ToItself(self):
        print ("Testing to itself conversions...")
        self.assertAlmostEqual(convert("Celsius", "Celsius", 20), 20)
        self.assertAlmostEqual(convert("Miles", "Miles", 100.00), 100.00)
        self.assertAlmostEqual(convert("Meters", "Meters", 100.00), 100.00)
        self.assertAlmostEqual(convert("Yards", "Yards", 1000.00), 1000.00)

    def test_impossible(self):
        print ("Testing impossible conversions...")
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Meters", 20)
        with self.assertRaises(ConversionNotPossible):
            convert("Kelvin", "Meters", 20)
        with self.assertRaises(ConversionNotPossible):
            convert("Fahrenheit", "Meters", 20)
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Yards", 20)
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Miles", 20)



if __name__ =='__main__':
    unittest.main()

