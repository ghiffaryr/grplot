from abc import ABC, abstractmethod, abstractproperty

class ISetFont(ABC):
    @abstractproperty
    def ax(self):
        pass

    @abstractmethod
    def set_font(self, ax) -> any:
        pass

    @abstractmethod
    def get_ax(self) -> any:
        pass