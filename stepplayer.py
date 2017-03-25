from time import sleep

from basic_nodes import InputNode, ControlNode, OutputNode, ValueConditionNode, TimeConditionNode, ManualConditionNode


class ControlStepPlayer(object):

    def __init__(self):
        self.steps = []  # type: List[ControlStep]
        self.actualStepIndex = 0

    def do_work(self):
        while True:
            if self.steps[self.actualStepIndex].work():  # next step
                self.steps[self.actualStepIndex].stop()
                self.actualStepIndex += 1

            if self.actualStepIndex > len(self.steps):  # last step, end
                self.steps[self.actualStepIndex].stop()
                self.actualStepIndex = -1
                break

            sleep(1)

        print("All Steps done...")

    def add_simple_step(self, name: str, input: InputNode, controller: ControlNode, output: OutputNode,
                        value=None, time=None, manual=False):
        """
        Creates a simple brew step, you must provide at least one condition
        :raise Exception: If no condition are provided
        :param name: 
        :param input: 
        :param controller: 
        :param output: 
        :param value: 
        :param time: 
        :param manual: 
        :return List of controllers: 
        """
        controller.input = input
        controller.output = output

        value_cond = timed_cond = manual_cond = None
        if value:
            value_cond = ValueConditionNode(value, input)
        if time:
            timed_cond = TimeConditionNode(time)
        if manual:
            manual_cond = ManualConditionNode()

        if value_cond and timed_cond and manual_cond:
            condition = value_cond.booleanAnd = timed_cond
            value_cond.booleanAnd.booleanAnd = manual
        elif value_cond and timed_cond:
            condition = value_cond.booleanAnd = timed_cond
        elif value_cond and manual_cond:
            condition = value_cond.booleanAnd = manual_cond
        elif timed_cond and manual_cond:
            condition = timed_cond.booleanAnd = manual_cond
        elif manual_cond:
            condition = manual_cond
        else:
            raise Exception("You have to specify at least one condition.")

        controllist = [controller]
        self.steps.append(ControlStep(name, controllist, [condition]))

        return controllist

class ControlStep(object):

    def __init__(self, name="Step", controls=None, conditions=None):
        if conditions is None:
            conditions = []
        if controls is None:
            controls = []
        self.name = name
        self.controls = controls  # type: List[ControlNode]
        self.conditions = conditions  # type: List[ConditionNode]
        self.proceedToNextStep = False

    def work(self):
        """

        :return: True if the conditions for this step are met
        """
        for cntrl in self.controls:
            cntrl.work()

        """
        All conditions are OR
        """
        for cond in self.conditions:
            cond.start()
            if cond.condition_met:
                print("Condition is met: [{}]", cond)
                self.proceedToNextStep = True

        return self.proceedToNextStep
