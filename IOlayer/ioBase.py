
class IoBase:

    def get_all_inputs(self):
        pass

    def get_all_outputs(self):
        pass


class InputBase:

    def __init__(self):
        self.name = "InputBase"
        self.inputId = 0

    def read(self):
        return 0


class OutputBase:

    def __init__(self):
        self.name = "OutputBase"
        self.inputId = 0

    def write(self, value):
        pass

    @property
    def state(self):
        return 0


class DummyInput(InputBase):

    def __init__(self):
        super().__init__()
        self.input = 0

    def read(self):
        return self.input


class DummyOutput(OutputBase):

    def __init__(self):
        super().__init__()
        self.out = 0

    def write(self, value):
        self.out = value
