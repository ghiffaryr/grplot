from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class IAnnotate(ABC):
    @abstractproperty
    def ax(self):
        pass

    @abstractproperty
    def axis(self):
        pass

    @abstractmethod
    def annotate(self, ax) -> Any:
        pass

    @abstractmethod
    def get_ax(self) -> Any:
        pass
