
class DigitalInput(object):

    def __init__(self):
        self.name = "Digital input"
        self.__callbacks = []

    def read(self):
        return True

    def add_callback(self, callback):
        self.__handlers.append(callback)
        return self

    def remove_callback(self, callback):
        self.__callbacks.remove(callback)
        return self

    def fire_callbacks(self, sender):
        for callback in self.__callbacks:
            callback(sender)

    __iadd__ = add_callback
    __isub__ = remove_callback
    __call__ = fire_callbacks
