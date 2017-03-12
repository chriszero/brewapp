from abc import ABCMeta


class InputBase:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name
        self.id

    def read_integer(self):
        raise NotImplemented

    def read_float(self):
        raise NotImplemented

    def read_bool(self):
        raise NotImplemented

    def read_raw(self):
        raise NotImplemented


class OutputBase:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name
        self.id

    def write_bool(self):
        raise NotImplemented

    def write_int(self):
        raise NotImplemented

    def write_float(self):
        raise NotImplemented