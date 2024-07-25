from numpy import ndarray
from point import find_point, Point
from mouse import click, move


def is_found(image: ndarray, screenshot: ndarray) -> bool:
    found_point: Point | None = find_point(image, screenshot)

    return found_point is not None


def find_and_click(image: ndarray, screenshot: ndarray, button: str) -> bool:
    found_point: Point | None = find_point(image, screenshot)
    if found_point != None:
        move(found_point[0], found_point[1])
        click(button)
        
        return True

    return False
