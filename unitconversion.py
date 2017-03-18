

class UnitConversion(object):
    """
    Converts units from SI to Imperial and vice versa
    All inputs are defined in the SI-System
    """

    target_unit = None
    SI_SYSTEM = "SI"
    IMPERIAL_SYSTEM = "IU"

    _unitFahrenheit = "°F"
    _unitCelsius = "°C"

    baseSystem = SI_SYSTEM
    targetSystem = SI_SYSTEM

    @classmethod
    def target_unit_temperature(cls):
        b = UnitConversion.targetSystem
        if b is UnitConversion.SI_SYSTEM:
            return UnitConversion._unitCelsius

        if b is UnitConversion.IMPERIAL_SYSTEM:
            return UnitConversion._unitFahrenheit

    @classmethod
    def convert_temperature(cls, t):
        """
        Converts t from baseSystem to targetSystem according to the setting in this class
        
        :param t: temperature input 
        :return: converted temperature
        """
        a = UnitConversion.baseSystem
        b = UnitConversion.targetSystem
        if a is b:
            return t

        if b is UnitConversion.SI_SYSTEM:
            return UnitConversion._fahrenheit_to_celsius(t)

        if b is UnitConversion.IMPERIAL_SYSTEM:
            return UnitConversion._celsius_to_fahrenheit(t)

    @classmethod
    def _celsius_to_fahrenheit(cls, cel):
        return cel * 1.8 + 32

    @classmethod
    def _fahrenheit_to_celsius(cls, fah):
        return (fah - 32) * (5/9)
