from actors.digitaloutput import DigitalOutput


class Pump(DigitalOutput):

    def __init__(self):
        super().__init__()
        self.name = "Pump"


class RegulatedPump(Pump):

    def __init__(self):
        super().__init__()
        self.name = "Regulated pump"

    def serPower(self):
        return True

