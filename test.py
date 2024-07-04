from mss import mss
from mss.base import MSSBase
from numpy import ndarray, array, where
from cv2 import cvtColor, imshow, waitKey, destroyAllWindows, IMREAD_COLOR
from time import sleep

base: MSSBase = mss()
WINDOW_WIDTH: int = 1920
WINDOW_HEIGHT: int = 1080

SCREENSHOT_WIDTH: int = 80
SCREENSHOT_HEIGHT: int = 80

MONITOR: tuple[int, int, int, int] = (
    int((WINDOW_WIDTH / 2) - SCREENSHOT_WIDTH), 
    int((WINDOW_HEIGHT / 2) - SCREENSHOT_HEIGHT), 
    int((WINDOW_WIDTH / 2) + (SCREENSHOT_WIDTH / 2)), 
    int((WINDOW_HEIGHT / 2) + (SCREENSHOT_HEIGHT / 2))
)

print(MONITOR)

sleep(2)

result: ndarray = cvtColor(array(base.grab(MONITOR)), IMREAD_COLOR)

imshow("Test", result)
waitKey(0)
destroyAllWindows()
