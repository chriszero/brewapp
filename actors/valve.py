from actors.digitaloutput import DigitalOutput


class TwoPointValve(DigitalOutput):

    def __init__(self):
        super().__init__()
        self.name = "2-point valve"

    def open(self):
        return super().on()

    def close(self):
        return super().off()


class ThreePointValve(TwoPointValve):

    def __init__(self):
        super().__init__()
        self.name = "3-point valve"
        self.runtime = 120

    def open(self, time):
        return True

    def close(self, time):
        return True

    def stop(self):
        return True
