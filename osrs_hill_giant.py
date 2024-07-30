from numpy import ndarray
from cv2 import imread, IMREAD_COLOR
from mouse import click, move, LEFT, RIGHT

from osrs.screenshot import make_screenshot
from osrs.game_status import GameStatus
from osrs.character import Character
from osrs.point import find_point, Point


def _find_and_click_on_npc(image: ndarray, screenshot: ndarray, button: str) -> bool:
    _NPC_POINT_OFFSET: int = 50

    found_point: Point | None = find_point(image, screenshot)
    if found_point != None:
        move(found_point[0], found_point[1] + _NPC_POINT_OFFSET)
        click(button)
        
        return True

    return False


def _find(image: ndarray, screenshot: ndarray) -> bool:
    found_point: Point | None = find_point(image, screenshot)
    if found_point != None:
        return True

    return False


def osrs_hill_giant() -> None:
    game_status: GameStatus = GameStatus()
    character: Character = Character()

    giant_health_image: ndarray = imread('hill_giant/giant_health.png', IMREAD_COLOR)
    giant_name_image: ndarray = imread('hill_giant/giant_name.png', IMREAD_COLOR)

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()
        game_status.check_game(screenshot)
        character.check_move()

        print("Is moving: ", character.is_moving())
        
        if game_status.is_opened() and not character.is_moving():
            if not _find(giant_health_image, screenshot) and _find_and_click_on_npc(giant_name_image, screenshot, LEFT):
                print("Hill Giant is found")

                character.make_moving()
                

if __name__ == "__main__":
    osrs_hill_giant()
