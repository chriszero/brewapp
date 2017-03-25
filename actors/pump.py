from actors.digitaloutput import DigitalOutput


class Pump(DigitalOutput):

    def __init__(self, name="Pump"):
        super().__init__()
        self.name = name


class RegulatedPump(Pump):

    def __init__(self, name="Regulated pump"):
        super().__init__()
        self.name = name

    def serPower(self):
        return True

