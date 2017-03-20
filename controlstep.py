from time import monotonic, sleep


class ControlStep(object):

    def __init__(self):
        self.name = "Step"
        self.controls = []  # type: List[ControlNode]
        self.conditions = []  # type: List[ConditionNode]
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


class ControlStepManager(object):

    def __init__(self):
        self.steps = []  # type: List[ControlStep]
        self.actualStepIndex = 0

    def do_work(self):
        while True:
            if self.steps[self.actualStepIndex].work():
                self.actualStepIndex += 1

            if self.actualStepIndex > len(self.steps):
                self.actualStepIndex = -1
                break

            sleep(1)

        print("All Steps done...")


class BaseNode(object):
    def __init__(self):
        self.name = "BaseNode"
        self._id = -1


class InputNode(BaseNode):

    def __init__(self):
        super().__init__()
        self.name = "InputNode"

    @property
    def input_value(self):
        return


class OutputNode(BaseNode):

    def __init__(self):
        super().__init__()
        self.name = "OutputNode"

    @property
    def output_value(self):
        return

    @output_value.setter
    def output_value(self, value):
        pass


class ControlNode(BaseNode):

    def __init__(self):
        super().__init__()
        self._inputNode = None  # type: InputNode
        self._outputNode = None  # type: OutputNode

    def work(self):
        pass

    @property
    def input(self) -> InputNode:
        return self._inputNode

    @input.setter
    def input(self, value: InputNode):
        self._inputNode = value

    @property
    def output(self) -> OutputNode:
        return self._outputNode

    @output.setter
    def output(self, value: OutputNode):
        self._outputNode = value


class ConditionNode(BaseNode):

    def __init__(self):
        super().__init__()
        self.name = "ConditionNode"
        self.nextStep = False
        self.booleanAnd = None  # type: ConditionNode

    def start(self):
        pass

    @property
    def condition_met(self):
        state = True
        if self.booleanAnd:
            state = state and self.booleanAnd.condition_met
        return state


class TimeConditionNode(ConditionNode):

    def __init__(self):
        super().__init__()
        self.name = "TimedConditionNode"
        self._timeSeconds = 0
        self._timeStarted = -1

    def start(self):
        """
        start the timer
        :return: 
        """
        if self._timeStarted < 0:
            print("TimedCondition Start")
            self._timeStarted = monotonic()

    @property
    def time_seconds(self):
        return self._timeSeconds

    @time_seconds.setter
    def time_seconds(self, value):
        self._timeSeconds = value

    @property
    def condition_met(self):
        state = False
        if self._timeStarted > 0:  # Evaluate only if the timer is started
            state = self._timeStarted + self._timeSeconds <= monotonic()
            # if our condition is met, start the next in the line
            if self.booleanAnd and state:
                self.booleanAnd.start()
                state = state and self.booleanAnd.condition_met

        return state


class ValueConditionNode(ConditionNode):

    def __init__(self):
        super().__init__()
        self.name = "ValueConditionNode"
        self._inputNode = None  # type: InputNode
        self._conditionValue = 0

    @property
    def condition_value(self):
        return self._conditionValue

    @condition_value.setter
    def condition_value(self, value):
        self._conditionValue = value

    @property
    def input_node(self) -> InputNode:
        return self._inputNode

    @input_node.setter
    def input_node(self, value: InputNode):
        self._inputNode = value

    @property
    def condition_met(self):
        state = False
        if self._inputNode:
            state = self._inputNode.input_value >= self._conditionValue
            # if our condition is met, start the next in the line
            if self.booleanAnd and state:
                self.booleanAnd.start()
                state = state and self.booleanAnd.condition_met

        return state
