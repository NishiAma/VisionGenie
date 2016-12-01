from abc import  ABCMeta, abstractmethod
from AbstractSensor import AbstractSensor

class AbstractCamera(AbstractSensor):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.observers = []

    def register(self,observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def updateObservers(self,frame):
        for observer in self.observers:
            observer.update(frame)

    @abstractmethod
    def start(self):
        return