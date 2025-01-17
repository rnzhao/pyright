# This sample tests the case where an issubclass type guard narrows
# to an abstract base class. When attempting to instantiate the
# class, there should be no "cannot instantiate ABC" error.

# pyright: strict

from abc import ABC, abstractmethod
from typing import Any


class Base(ABC):
    @abstractmethod
    def f(self) -> None:
        ...


def func(cls: Any):
    assert issubclass(cls, Base)
    _ = cls()
