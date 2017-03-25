
class Scale(object):

    def __init__(self, scale_in_min=0, scale_in_max=1000, scale_out_min=0, scale_out_max=1):
        """
        Scales the input and output as the hardware needs it.
        eg: Your have an analog sensor with a range of -20°C to +60°C
            The D/A converter interpreting the signal in a 0-5V range.
            scaler = Scale(scale_in_min=0, scale_in_max=5, scale_out_min=-20, scale_out_max=60)
            scaled_value = scaler.input(raw_value_from_da)
        :param scale_in_min: 
        :param scale_in_max: 
        :param scale_out_min: 
        :param scale_out_max: 
        """
        self._scaleInMin = scale_in_min
        self._scaleInMax = scale_in_max
        self._scaleOutMin = scale_out_min
        self._scaleOutMax = scale_out_max

    def input(self, value):
        return (self._scaleOutMax - self._scaleOutMin) / (self._scaleInMax - self._scaleInMin) * value \
            - self._scaleInMin + self._scaleOutMin

    def output(self, value):
        return (self._scaleOutMax - self._scaleOutMin) * value / self._scaleInMax + self._scaleOutMin
