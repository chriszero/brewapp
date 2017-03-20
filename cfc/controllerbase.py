from controlstep import ControlNode


class ControllerBase(object):

    def __init__(self):
        self.name = "Controller base"
        self.setpoint = 0
        self.actual = 0

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint

    def getError(self):
        return self.setpoint - self.actual


class ManualController(ControllerBase, ControlNode):

    def work(self):
        pass


class Hysteresis(ControllerBase, ControlNode):

    def __init__(self):
        super().__init__()
        self.hysteresis = 2.0

    def work(self):
        self.actual = self.input.input_value

        if self.actual < self.setpoint + self.hysteresis:
            self.output.output_value = True

        elif self.actual > self.setpoint:
            self.output.output_value = False
