from abc import ABC, abstractmethod, abstractproperty

class IAnnotate(ABC):
    @abstractproperty
    def ax(self):
        pass

    @abstractproperty
    def axis(self):
        pass

    @abstractmethod
    def annotate(self, ax) -> any:
        pass

    @abstractmethod
    def get_ax(self) -> any:
        pass