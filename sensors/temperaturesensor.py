from sensors.analoginput import AnalogInput


class TemperatureSensor(AnalogInput):
    def __init__(self):
        super().__init__()
        self.name = "Temperature Sensor"

    @property
    def get_temperature(self):
        return super().read_integer() / 1000
