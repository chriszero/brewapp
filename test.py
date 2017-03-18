# -*- coding: utf-8 -*-

from builtins import print
from IOlayer.oneWire import OneWireThermSensor
from sensors.temperaturesensor import TemperatureSensor
from unitconversion import UnitConversion


def main():
    sensor = TemperatureSensor("1-Wire Sensor 1")
    sensor.input = OneWireThermSensor("000006cbe65b", OneWireThermSensor.DS18B20)
    print(sensor.read())
    print(sensor.read_scaled())
    print(sensor.temperature)
    print(sensor.temperature_with_unit)

    UnitConversion.targetSystem = UnitConversion.IMPERIAL_SYSTEM
    print(sensor.temperature)
    print(sensor.temperature_with_unit)

    print(sensor)


if __name__ == "__main__":
    main()
