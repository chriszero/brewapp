from basic_nodes import ControlNode


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

    def __init__(self, name="Manual Controller", start_state=False):
        super().__init__()
        self.name = name
        self.setpoint = start_state

    def work(self):
        self.output.output_value = self.setpoint

    def on(self):
        self.setpoint = True

    def off(self):
        self.setpoint = False

    def set_value(self, value):
        self.setpoint = value


class Hysteresis(ControllerBase, ControlNode):
    """
    Simple hysteresis controller
    """

    def __init__(self, hysteresis=1.0):
        super().__init__()
        self.hysteresis = hysteresis

    def work(self):
        self.actual = self.input.input_value

        if self.actual < self.setpoint + self.hysteresis:
            self.output.output_value = True

        elif self.actual > self.setpoint:
            self.output.output_value = False
