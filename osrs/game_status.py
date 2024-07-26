from numpy import ndarray
from cv2 import imread, IMREAD_COLOR
from mouse import on_middle_click

from .match import is_found


class GameStatus():
    def __init__(self):
        self.__is_runing: bool = True
        self.__is_opened: bool = False

        self.__GAME_IMAGE: ndarray = imread('common/game.png', IMREAD_COLOR)

        on_middle_click(self.__stop)

    def __stop(self) -> None:
        self.__is_runing: bool = False

    def check_game(self, screenshot: ndarray) -> None:
        self.__is_opened = is_found(self.__GAME_IMAGE, screenshot)

    def is_runing(self) -> bool:
        return self.__is_runing

    def is_opened(self) -> bool:
        return self.__is_opened
