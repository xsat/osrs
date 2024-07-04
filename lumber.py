
from mss import mss
from mss.base import MSSBase
from cv2 import imread, IMREAD_COLOR
from mouse import click, move, on_middle_click, LEFT, RIGHT
from numpy import ndarray, allclose
from screenshot import make_screenshot
from point import find_point, Point


class Status():
    def __init__(self):
        self.__is_runing = True

    def stop(self) -> None:
        self.__is_runing = False

    def is_runing(self) -> bool:
        return self.__is_runing


def _find_and_click(image: ndarray, screenshot: ndarray, button: str) -> bool:
    found_point: Point | None = find_point(image, screenshot)
    if found_point != None:
        move(found_point[0], found_point[1])
        click(button)
        
        return True

    return False


def osrs_lumber() -> None:
    status: Status = Status()
    on_middle_click(status.stop)

    base: MSSBase = mss()
    game: Point | None = None
    game_image: ndarray = imread('images/game.png', IMREAD_COLOR)
    started_point_image: ndarray = imread('lumber/started_point.png', IMREAD_COLOR)
    first_tree_image: ndarray = imread('lumber/first_tree.png', IMREAD_COLOR)

    found_started_point: bool = False
    found_first_tree: bool = False
    last_screenshot: ndarray | None = None

    while status.is_runing():
        if game == None:
            screenshot: ndarray = make_screenshot(base)
            game: Point | None = find_point(game_image, screenshot)
        
        if game != None:
            print('Game is started', found_started_point, found_first_tree)

            print(last_screenshot, screenshot)
            
            if allclose(last_screenshot, screenshot):
                print('running')
                break

            # if not found_started_point and _find_and_click(started_point_image, screenshot, LEFT):
            #     found_started_point = True
            #     print('found_started_point')
            
            # if not found_first_tree and _find_and_click(first_tree_image, screenshot, LEFT):
            #     found_first_tree = True
            #     print('found_started_point')

            # if found_first_tree and _find_and_click(first_tree_image, screenshot, LEFT):
            #     print('Cutting tree')
            #     found_started_point = False
            #     found_first_tree = False


        last_screenshot = screenshot

if __name__ == "__main__":
    osrs_lumber()
