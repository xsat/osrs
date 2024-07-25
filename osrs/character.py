from numpy import ndarray

from .compare import is_same
from .screenshot import make_small_screenshot


class Character():
    __MIN_MOVE_CHECKS: int = 3

    def __init__(self):
        self.__in_a_row_move_cheaks: int = 0 # This logic fix move detection on character animation in standing.
        self.__current_screenshot: ndarray | None = None
        self.__last_screenshot: ndarray | None = None

    def __is_not_same_screenshots(self) -> bool:
        if self.__current_screenshot is None or self.__last_screenshot is None:
            return True
        
        return not is_same(self.__current_screenshot, self.__last_screenshot)

    def check_move(self) -> None:
        small_screenshot: ndarray = make_small_screenshot()

        self.__current_screenshot = small_screenshot

        if self.__is_not_same_screenshots():
            self.__in_a_row_move_cheaks += 1
        else:
            self.__in_a_row_move_cheaks = 0

        self.__last_screenshot = small_screenshot

    def make_moving(self) -> None:
        self.__in_a_row_move_cheaks = self.__MIN_MOVE_CHECKS

    def is_moving(self) -> bool:
        return self.__in_a_row_move_cheaks >= self.__MIN_MOVE_CHECKS
