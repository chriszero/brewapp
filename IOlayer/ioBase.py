from abc import ABCMeta


class IoBase:
    __metaclass__ = ABCMeta

    def get_all_inputs(self):
        pass

    def get_all_outputs(self):
        pass


class InputBase:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = "InputBase"
        self.inputId = 0

    def read(self):
        return 0


class OutputBase:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = "OutputBase"
        self.inputId = 0

    def write_bool(self):
        pass

    def write_int(self):
        pass

    def write_float(self):
        pass
