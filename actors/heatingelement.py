from actors.digitaloutput import DigitalOutput


class HeatingElement(DigitalOutput):
    def __init__(self):
        super().__init__()
        self.name = "Heating element"
        self.power = 1800


class RegulatedHeatingElement(HeatingElement):

    def __init__(self):
        super().__init__()
        self.name = "Regulated heating element"

    def setPower(self, power):
        return True


class MultiStageHeatingElement(object):

    def __init__(self):
        self.name = "Multistage heating element"
        self.heatingelements = []
