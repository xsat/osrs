from numpy import ndarray
from cv2 import matchTemplate, minMaxLoc, TM_CCOEFF_NORMED
from cv2.typing import Point


_SUCCESSFUL_MATCHED_PERCENT: float = .7


def _match_one(image: ndarray, haystack: ndarray, matched_percent: float) -> Point | None:
    try:
        result: ndarray = matchTemplate(image, haystack, TM_CCOEFF_NORMED)
        _, maxVal, _, maxLoc = minMaxLoc(result)
        if maxVal >= matched_percent:
            return maxLoc
    except:
        pass
    
    return None


def find_point(image: ndarray, haystack: ndarray, matched_percent: float = _SUCCESSFUL_MATCHED_PERCENT) -> Point | None:
    matched_point = _match_one(image, haystack, matched_percent)
    if matched_point is not None:
        return (
            matched_point[0] + round(image.shape[1] / 2), 
            matched_point[1] + round(image.shape[0] / 2)
        )

    return None
