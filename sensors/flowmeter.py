from sensors.analoginput import AnalogInput
from sensors.digitalinput import DigitalInput

# Scale this shit....

class FlowMeter(AnalogInput):

    def __init__(self):
        super().__init__()
        self.name = "Flowmeter"


    def unit_per_minute(self):
        return super().read_integer() / 180

class DigitalFlowmeter(DigitalInput):

    def __init__(self):
        super().__init__()
        self.name = "Digital Flowmeter"
        self.pulse_per_unit = 10

    def unit_per_minute(self):
        return 0
