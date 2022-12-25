from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class ISetFont(ABC):
    @abstractproperty
    def ax(self):
        pass

    @abstractmethod
    def set_font(self, ax) -> Any:
        pass

    @abstractmethod
    def get_ax(self) -> Any:
        pass
