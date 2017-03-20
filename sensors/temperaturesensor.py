from sensors.analoginput import AnalogInput
from unitconversion import UnitConversion


class TemperatureSensor(AnalogInput):
    def __init__(self, name=None):
        super().__init__()
        if not name:
            self.name = "Temperature Sensor"
        self.name = name

    @property
    def temperature(self):
        """
        Actual value
        :return: float
        """
        return UnitConversion.convert_temperature(self.read_scaled())

    @property
    def temperature_with_unit(self):
        """
        Actual value with unit sign
        :return: str 
        """
        return "{} {}".format(self.temperature, UnitConversion.target_unit_temperature())

    @property
    def input_value(self):
        return self.temperature

    def __str__(self):
        return "{} [{}]".format(self.name, self.temperature_with_unit)
