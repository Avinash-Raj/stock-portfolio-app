# base module for all the actions
from dataclasses import dataclass
from typing import Callable, Optional

from PySide6.QtWidgets import QWidget

from views.spinner import Spinner


@dataclass
class SpinnerBase:
    """
    Base class for the all the classes which expects spin operation on the foreground.
    """

    parent: QWidget
    callback: Optional[Callable] = None

    def __post_init__(self):
        self.spinner = Spinner(self.parent)
