from abc import ABC, abstractmethod

class UIHandler(ABC):

    @abstractmethod
    def updateUI(self):
        pass

class UIObjects:

    def __init__(self, enabled = False, visible = False):
        self.enabled = enabled
        self._visible = visible

    def showUI(self):
        print ("Object is shown")


class Button(UIHandler, UIObjects):
    #Oveririding the
    def updateUI(self):
        self.enabled = True
        print ("Button is updated")

    def showUI(self):
        if self.enabled:
            self._visible = True
            print ("Button is shown")


class RadioButton(UIHandler, UIObjects):
    def updateUI(self):
        self.enabled = True
        print ("Radio button is updated")

    def showUI(self):
        print ("Radio button is shown")


button = Button()
button.updateUI()
button.showUI()


# Decorator function
def decorator_func(func):
    def wrapper():
        print ("Before calling function")
        func()
        print ("After calling function")

    return wrapper

@decorator_func
def using_decorator():
    print ("I am using decorator")


# decorator using class
class decorator(object):
    class innerclass():
        def __init__(self, object):
            self.isEnabled = True
            print ("I am decorator")


@decorator.innerclass
def using_dec():
    print ("this is using decorator function")
