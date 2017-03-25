import RPi.GPIO as GPIO
from iolayer.ioBase import InputBase, OutputBase


class RPiGpioBase(object):
    def __init__(self, gpiopin):
        GPIO.setmode(GPIO.BOARD)
        self._gpiopin = gpiopin


class RPiGpioInput(RPiGpioBase, InputBase):
    def __init__(self, pin: int):
        super().__init__(pin)
        GPIO.setup(pin, GPIO.IN)

    def read(self):
        pass  # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/


class RPiGpioOutput(RPiGpioBase, OutputBase):
    def __init__(self, pin: int):
        super().__init__(pin)
        GPIO.setup(pin, GPIO.OUT)
        self._state = False

    def write(self, value):
        self._state = bool(value)  # convert to bool
        GPIO.output(self._gpiopin, self._state)

    @property
    def state(self):
        return self._state


class RPiGpioPwmOutput(RPiGpioBase, OutputBase):
    def __init__(self, pin: int):
        super().__init__(pin)
        self._frequency = 10
        self._pwmout = GPIO.PWM(pin, self._frequency)
