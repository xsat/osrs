from mss import mss
from mss.base import MSSBase
from numpy import ndarray, array, where
from cv2 import cvtColor, imshow, waitKey, countNonZero, destroyAllWindows, subtract, split, IMREAD_COLOR
from time import sleep


#  if original.shape == image_to_compare.shape:
#     print("The images have the same size and channels")
#     difference = cv2.subtract(original, image_to_compare)
#     b, g, r = cv2.split(difference)
    
# #image1 = original.shape
# #image2 = duplicate.shape
#     cv2.imshow("difference", difference)
#     #cv2.imshow("b", b)
#     #cv2.imshow("g", g)
#     #cv2.imshow("r", r)

base: MSSBase = mss()
WINDOW_WIDTH: int = 1920
WINDOW_HEIGHT: int = 1080

SCREENSHOT_WIDTH: int = 70
SCREENSHOT_HEIGHT: int = 70

MONITOR: tuple[int, int, int, int] = (
    int((WINDOW_WIDTH / 2) - SCREENSHOT_WIDTH), 
    int((WINDOW_HEIGHT / 2) - SCREENSHOT_HEIGHT), 
    int((WINDOW_WIDTH / 2) + (SCREENSHOT_WIDTH / 2)), 
    int((WINDOW_HEIGHT / 2) + (SCREENSHOT_HEIGHT / 2))
)

print("start")

sleep(5)

original: ndarray = cvtColor(array(base.grab(MONITOR)), IMREAD_COLOR)

imshow("original", original)

print("next")

sleep(5)



compare: ndarray = cvtColor(array(base.grab(MONITOR)), IMREAD_COLOR)

imshow("compare", compare)



if original.shape == compare.shape:
    difference: ndarray = subtract(original, compare)
    b, g, r = split(difference)

    print(countNonZero(b) == 0 and countNonZero(g) == 0 and countNonZero(r) == 0)

    imshow("Difference", difference)


    # imshow("b", b)
    # imshow("g", g)
    # imshow("r", r)


waitKey(0)
destroyAllWindows()
