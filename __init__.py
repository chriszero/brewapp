from actors.heatingelement import HeatingElement
from actors.pump import Pump
from controllers.controllerbase import Hysteresis, ManualController
from iolayer.ioBase import DummyInput, DummyOutput
from sensors.temperaturesensor import TemperatureSensor
from stepplayer import ControlStepPlayer
from unitconversion import UnitConversion


def main():
    """
    Simple brew
    :return: 
    """

    UnitConversion.targetSystem = UnitConversion.SI_SYSTEM

    # our Sensor
    tSensor1 = TemperatureSensor("Dummy Temperaturesensor")
    tSensor1.input = DummyInput()

    heater = HeatingElement("Dummy Heater")
    heater.output = DummyOutput()

    hyst_controller = Hysteresis()

    pump_controller = ManualController("Manual Pump Controller", True)
    pump = Pump("Dummy Pump")
    pump.output = DummyOutput()
    pump_controller.output = pump

    step_player = ControlStepPlayer()

    step_player.add_simple_step("Einmaischen", tSensor1, hyst_controller, heater, value=45, manual=True)
    step_player.add_simple_step("Weizenrast", tSensor1, hyst_controller, heater, value=43, time=20 * 60)
    step_player.add_simple_step("Maltoserast", tSensor1, hyst_controller, heater, value=63, time=30 * 60)
    step_player.add_simple_step("Verzuckerung ", tSensor1, hyst_controller, heater, value=72, time=30 * 60)
    step_player.add_simple_step("Abmaischen ", tSensor1, hyst_controller, heater, value=78).append(pump_controller)
    step_player.add_simple_step("Läuterruhe", tSensor1, hyst_controller, heater, time=15*60, manual=True)
    step_player.add_simple_step("Kochen ", tSensor1, hyst_controller, heater, value=100, time=70 * 60)
    step_player.add_simple_step("Whirlpool ", tSensor1, hyst_controller, heater, time=15 * 60, manual=True)

    step_player.do_work()  # start process -> new thread or background task

if __name__ == '__main__':
    main()
