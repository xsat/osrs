from numpy import ndarray
from cv2 import matchTemplate, minMaxLoc, TM_CCOEFF_NORMED
from cv2.typing import Point


_SUCCESSFUL_MATCHED_PERCENT: float = .8


def _match_one(image: ndarray, haystack: ndarray) -> Point | None:
    try:
        result: ndarray = matchTemplate(image, haystack, TM_CCOEFF_NORMED)
        _, maxVal, _, maxLoc = minMaxLoc(result)
        if maxVal >= _SUCCESSFUL_MATCHED_PERCENT:
            return maxLoc
    except:
        pass
    
    return None


def find_point(image: ndarray, haystack: ndarray) -> Point | None:
    matched_point = _match_one(image, haystack)
    if matched_point is not None:
        return (
            matched_point[0] + round(image.shape[1] / 2), 
            matched_point[1] + round(image.shape[0] / 2)
        )

    return None
