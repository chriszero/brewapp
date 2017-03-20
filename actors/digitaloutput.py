from IOlayer.ioBase import OutputBase
from controlstep import OutputNode


class DigitalOutput(OutputNode):

    def __init__(self):
        self.name = "Digital output"
        self._output = None  # type: OutputBase
        self._outputValue = False

    @property
    def output(self) -> OutputBase:
        """
        The underlying hardware io
        :return: OutputBase
        """
        return self._output

    @output.setter
    def output(self, value: OutputBase):
        """
        The underlying hardware io
        :param value: 
        :return: 
        """
        self._output = value

    @property
    def output_value(self):
        return self._outputValue

    @output_value.setter
    def output_value(self, value):
        self._outputValue = bool(value)
        if self._output:
            self._output.write(self._outputValue)
        else:
            print("No Output specified in {}", self.name)


class AnalogOutput(DigitalOutput):
    def __init__(self):
        super().__init__()
        self.name = "Analog output"
        self._outputValue = 0
        self._scaledOutputValue = 0

        self._scaleInMax = 100
        self._scaledOutMin = 0
        self._scaleOutMax = 255

    @property
    def output_value(self):
        return self._outputValue

    @output_value.setter
    def output_value(self, value):
        self._outputValue = value
        self._scaledOutputValue = self._scale_output(value)
        if self._output:
            self._output.write(self._scaledOutputValue)
        else:
            print("No Output specified in {}", self.name)

    def _scale_output(self, value):
        value = float(value)
        return (self._scaleOutMax - self._scaledOutMin) * value / self._scaleInMax + self._scaledOutMin
