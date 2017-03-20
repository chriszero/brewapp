from actors.digitaloutput import DigitalOutput, AnalogOutput
from controlstep import OutputNode


class HeatingElement(DigitalOutput):
    def __init__(self):
        super().__init__()
        self.name = "Heating element"
        self.power = 1800


class RegulatedHeatingElement(AnalogOutput):

    def __init__(self):
        super().__init__()
        self.name = "Regulated heating element"
        self.power = 1800


class MultiStageHeatingElement(OutputNode):

    def __init__(self):
        super().__init__()
        self.name = "Multistage heating element"
        self.heatingelements = []  # type: HeatingElement

    @property
    def output_value(self):
        return

    @output_value.setter
    def output_value(self, value):
        pass
