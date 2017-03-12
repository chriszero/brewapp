from actors.digitaloutput import DigitalOutput


class Stirrer(DigitalOutput):

    def __init__(self):
        super().__init__()
        self.name = "Stirrer"


