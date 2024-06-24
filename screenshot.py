from mss.base import MSSBase
from numpy import ndarray, array
from cv2 import cvtColor, IMREAD_COLOR


_MONITOR: tuple[int, int, int, int] = (0, 0, 1920, 1080)


def make_screenshot(base: MSSBase) -> ndarray:
    return cvtColor(array(base.grab(_MONITOR)), IMREAD_COLOR)
