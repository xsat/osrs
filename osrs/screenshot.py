from mss import mss
from mss.base import MSSBase
from numpy import ndarray, array
from cv2 import cvtColor, IMREAD_COLOR


_WINDOW_WIDTH: int = 1920
_WINDOW_HEIGHT: int = 1080

_MONITOR: tuple[int, int, int, int] = (0, 0, _WINDOW_WIDTH, _WINDOW_HEIGHT)

_SCREENSHOT_WIDTH: int = 70
_SCREENSHOT_HEIGHT: int = 70

_SMALL_MONITOR: tuple[int, int, int, int] = (
    int((_WINDOW_WIDTH / 2) - _SCREENSHOT_WIDTH), 
    int((_WINDOW_HEIGHT / 2) - _SCREENSHOT_HEIGHT), 
    int((_WINDOW_WIDTH / 2) + (_SCREENSHOT_WIDTH / 2)), 
    int((_WINDOW_HEIGHT / 2) + (_SCREENSHOT_HEIGHT / 2))
)

_base: MSSBase = mss()


def _screenshot(monitor: tuple[int, int, int, int]) -> ndarray:
    return cvtColor(array(_base.grab(monitor)), IMREAD_COLOR)


def make_screenshot() -> ndarray:
    return _screenshot(_MONITOR)


def make_small_screenshot() -> ndarray:
    return _screenshot(_SMALL_MONITOR)
