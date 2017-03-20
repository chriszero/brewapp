from IOlayer.ioBase import InputBase
from time import monotonic
from controlstep import InputNode


class AnalogInput(InputNode):
    def __init__(self):
        super().__init__()
        self.name = "Analog input"

        self._input = None  # type: InputBase
        self._scaleInMin = 0
        self._scaleInMax = 1000.0
        self._scaleOutMin = 0
        self._scaleOutMax = 1.0

        self.cacheTime = 1000  # in ms
        self.__nextRead = monotonic() * 1000
        self.__cachedValue = 0

    @property
    def input(self) -> InputBase:
        """
        
        :return: InputBase 
        """
        return self._input

    @input.setter
    def input(self, value: InputBase):
        """
        
        :param value: InputBase
        :return: 
        """
        self._input = value

    def read_scaled(self):
        """
        get a scaled value of the input
        :return: float 
        """
        val = self.read() * 1.0
        scaled = (self._scaleOutMax - self._scaleOutMin) / (self._scaleInMax - self._scaleInMin) * val \
            - self._scaleInMin + self._scaleOutMin
        return scaled

    def read(self):
        """
        get the value of the input as raw
        :return: float
        """
        now = monotonic() * 1000
        if self.__nextRead <= now:
            self.__nextRead = now + self.cacheTime
            self.__cachedValue = self.input.read()

        return self.__cachedValue

    @property
    def input_value(self):
        return self.read_scaled()
