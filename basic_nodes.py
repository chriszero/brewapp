from time import monotonic


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
        self._setpoint = 0

    def work(self):
        """
        override to implement your controller logic, it's called once every cycle
        :return: 
        """
        pass

    def stop(self):
        """
        Stops control, sets output to False, is called before next step
        override if the controller implementation require something special
        :return: 
        """
        self.output.output_value = False

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

    @property
    def setpoint(self):
        return self._setpoint

    @setpoint.setter
    def setpoint(self, value):
        self._setpoint = value


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

    def __init__(self, timeseconds=0):
        super().__init__()
        self.name = "TimedConditionNode"
        self._timeSeconds = timeseconds
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

    def __init__(self, value=0, inputnode=None):
        super().__init__()
        self.name = "ValueConditionNode"
        self._inputNode = inputnode  # type: InputNode
        self._conditionValue = value

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


class ManualConditionNode(ConditionNode):

    def __init__(self):
        super().__init__()
        self.name = "ManualConditionNode"
        self._conditionMet = False

    def condition_met(self):
        state = self._conditionMet
        if self.booleanAnd:
            state = state and self.booleanAnd.condition_met

        return state

    def set_condition_met(self, value=True):
        self._conditionMet = bool(value)
