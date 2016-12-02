from abc import ABCMeta, abstractmethod
import threading

class system(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def instantiateSystem(self):
        raise NotImplementedError()

    @abstractmethod
    def reactivateSystem(self):
        raise NotImplementedError()

    @abstractmethod
    def deactivateSystem(self):
        raise NotImplementedError()

    @abstractmethod
    def diagnostic(self):
        raise NotImplementedError()

    def systemRun(self):
        t = threading.Thread(target=self.instantiateSystem)
        t.start()
