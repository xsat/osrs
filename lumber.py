
from mss import mss
from mss.base import MSSBase
from cv2 import imread, IMREAD_COLOR
from mouse import click, move, LEFT, RIGHT

from screenshot import make_screenshot, ndarray
from point import find_point, Point


def _find_and_click(image: ndarray, screenshot: ndarray, button: str) -> bool:
    found_point: Point | None = find_point(image, screenshot)
    if found_point != None:
        move(found_point[0], found_point[1])
        click(button)
        
        return True

    return False


def osrs_lumber() -> None:
    base: MSSBase = mss()
    game: Point | None = None
    game_image: ndarray = imread('images/game.png', IMREAD_COLOR)
    started_point_image: ndarray = imread('lumber/started_point.png', IMREAD_COLOR)
    first_tree_image: ndarray = imread('lumber/first_tree.png', IMREAD_COLOR)

    while True:
        if game == None:
            screenshot: ndarray = make_screenshot(base)
            game: Point | None = find_point(game_image, screenshot)
        
        if game != None:
            print('Game is started')

            if _find_and_click(started_point_image, screenshot, LEFT):
                print('started_point_image')
                if _find_and_click(first_tree_image, screenshot, LEFT):
                    print('first_tree_image')
                break
 

if __name__ == "__main__":
    osrs_lumber()
