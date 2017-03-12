
class ControllerBase(object):

    def __init__(self):
        self.name = "Controller base"
        self.setpoint = 0
        self.actual = 0
        self.min = 0
        self.max = 255

    def setactual(self, actual):
        self.actual = actual

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def getError(self):
        return self.setpoint - self.actual


class Hysteresis(ControllerBase):

    def __init__(self):
        super().__init__()
        self.hysteresis = 0

    def compute(self, setpoint, actual):
        self.set_setpoint(setpoint)
        self.setactual(actual)
        return 0

