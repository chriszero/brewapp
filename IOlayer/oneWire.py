from IOlayer.ioBase import IoBase, InputBase, OutputBase
from os import path, listdir

class OneWireBase(object):
    BASE_DIRECTORY = "/sys/bus/w1/devices/"
    SLAVE_FILE = "w1_slave"

    def __init__(self, onewireid, slaveprefix):
        self._oneWireId = onewireid
        self._slavePrefix = slaveprefix

        self.sensorpath = path.join(self.BASE_DIRECTORY, self._slavePrefix + '-' + self._oneWireId, self.SLAVE_FILE)

    @classmethod
    def get_available_sensors(cls, sensortype):
        sensors = []
        for s in listdir(cls.BASE_DIRECTORY):
            if s.startswith(sensortype):
                sensors.append(s)
                print(s)

        return sensors


class OneWireThermSensor(OneWireBase, InputBase, ):
    DS18S20 = "10"
    DS1822 = "22"
    DS18B20 = "28"
    DS1825 = "3B"
    DS28EA00 = "42"
    MAX31850K = "3B"

    ALL = [DS18S20, DS1822, DS18B20, DS1825, DS28EA00, MAX31850K]

    def __init__(self, onewireid, slaveprefix):
        super(OneWireThermSensor, self).__init__(onewireid, slaveprefix)

    @classmethod
    def get_available_sensors(cls, sensortype=None):
        if not sensortype:
            sensortype = OneWireThermSensor.ALL
        sensors = []
        for i in sensortype:
            sensors.append(OneWireBase.get_available_sensors(i))

        return  sensors

    @property
    def _read_raw_input(self):
        try:
            with open(self.sensorpath, "r") as f:
                data = f.readlines()
        except IOError:
            print("sensor not found: ", self.sensorpath)  # TODO: log sensor not found

        if data[0].strip()[-3:] != "YES":
            pass # TODO: log sensor not ready
        return float(data[1].split("=")[1])

    def read(self):
        return self._read_raw_input
