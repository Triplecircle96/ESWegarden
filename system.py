from abc import ABCMeta, abstractmethod

class System:
    __metaclass__ = ABCMeta

    @abstractmethod
    def instantiateSystem(self):
        raise NotImplementedError()

    @abstractmethod
    def 