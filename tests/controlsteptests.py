import unittest
from IOlayer.ioBase import DummyInput, DummyOutput
from actors.digitaloutput import DigitalOutput
from cfc.controllerbase import Hysteresis
from controlstep import ValueConditionNode, TimeConditionNode
from sensors.temperaturesensor import TemperatureSensor

from time import sleep


class ControlStepsTestCase(unittest.TestCase):

    def test_value_condition(self):
        tSensor = TemperatureSensor("Dummy Sensor")
        tSensor.cacheTime = 0
        tSensor.input = DummyInput()

        condition = ValueConditionNode()
        condition.condition_value = 26
        condition.input_node = tSensor

        tSensor.input.input = 12000
        self.assertFalse(condition.condition_met)

        tSensor.input.input = 27000
        self.assertTrue(condition.condition_met)

    def test_timed_condition(self):
        condition = TimeConditionNode()
        condition.time_seconds = 1

        condition.start()

        self.assertFalse(condition.condition_met)

        sleep(1)
        self.assertTrue(condition.condition_met)

    def test_chained_condition(self):
        tSensor = TemperatureSensor("Dummy Sensor")
        tSensor.cacheTime = 0
        tSensor.input = DummyInput()

        condition = ValueConditionNode()
        condition.condition_value = 26
        condition.input_node = tSensor

        condition2 = TimeConditionNode()
        condition2.time_seconds = 1

        condition.booleanAnd = condition2

        tSensor.input.input = 12000
        self.assertFalse(condition.condition_met)

        tSensor.input.input = 27000
        self.assertFalse(condition.condition_met)

        self.assertFalse(condition.condition_met)

        sleep(1)
        self.assertTrue(condition.condition_met)

    def test_hysteresis(self):
        tSensor = TemperatureSensor("Dummy Sensor")
        tSensor.cacheTime = 0
        tSensor.input = DummyInput()
        tSensor.input.input = 12000

        output = DigitalOutput()
        dout = DummyOutput()
        output.output = dout

        hyst = Hysteresis()
        hyst.input = tSensor
        hyst.output = output
        hyst.hysteresis = 2
        hyst.setpoint = 10

        hyst.work()
        self.assertEqual(dout.out, 0)

        tSensor.input.input = 5000
        hyst.work()
        self.assertGreater(dout.out, 0)

        tSensor.input.input = 10000
        hyst.work()
        self.assertGreater(dout.out, 0)

        tSensor.input.input = 12000
        hyst.work()
        self.assertLess(dout.out, 1)

if __name__ == '__main__':
    unittest.main()
