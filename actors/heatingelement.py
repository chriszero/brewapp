from actors.digitaloutput import DigitalOutput, AnalogOutput
from basic_nodes import OutputNode


class HeatingElement(DigitalOutput):
    def __init__(self, name="Heating element"):
        super().__init__()
        self.name = name
        self.power = 1800


class RegulatedHeatingElement(AnalogOutput):

    def __init__(self, name="Regulated heating element"):
        super().__init__()
        self.power = 1800
        self.name = name


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
