from abc import ABCMeta, abstractmethod
import threading

class system:
    __metaclass__ = ABCMeta

    @abstractmethod
    def instantiateSystem(self):
        raise NotImplementedError()

    @abstractmethod
    def deactivateSystem(self):
        raise NotImplementedError()

    @abstractmethod
    def diagnostic(self):
        raise NotImplementedError()

    def systemRun(self):
        t=threading.Thread(target=instantiateSystem)
        t.start()