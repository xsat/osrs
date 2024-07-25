from numpy import ndarray
from cv2 import subtract, split, countNonZero


def is_same(first_image: ndarray, second_image: ndarray) -> bool:
    if first_image.shape == second_image.shape:
        difference: ndarray = subtract(first_image, second_image)
        b, g, r = split(difference)

        return countNonZero(b) == 0 and countNonZero(g) == 0 and countNonZero(r) == 0
    
    return False
