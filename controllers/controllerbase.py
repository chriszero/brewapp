from basic_nodes import ControlNode


class ManualController(ControlNode):

    def __init__(self, name="Manual Controller", start_state=False):
        super().__init__()
        self.name = name
        self._setpoint = start_state

    def work(self):
        self.output.output_value = self.setpoint

    def on(self):
        self._setpoint = True

    def off(self):
        self._setpoint = False

    def set_value(self, value):
        self._setpoint = value


class Hysteresis(ControlNode):
    """
    Simple hysteresis controller
    """

    def __init__(self, hysteresis=1.0):
        super().__init__()
        self.hysteresis = hysteresis

    def work(self):
        actual = self.input.input_value

        if actual < self._setpoint + self.hysteresis:
            self.output.output_value = True

        elif actual > self._setpoint:
            self.output.output_value = False
