from cv2 import imread, IMREAD_COLOR
from mouse import click, move, LEFT
from numpy import ndarray
from screenshot import make_screenshot
from point import find_point, Point
from game_status import GameStatus


def _is_found(image: ndarray, screenshot: ndarray) -> bool:
    found_point: Point | None = find_point(image, screenshot)

    return found_point is not None


def _find_and_click(image: ndarray, screenshot: ndarray, button: str) -> bool:
    found_point: Point | None = find_point(image, screenshot)

    if found_point != None:
        move(found_point[0], found_point[1])
        click(button)
        
        return True

    return False


def high_level_alchemy() -> None:
    game_image: ndarray = imread('images/game.png', IMREAD_COLOR)

    magic_image: ndarray = imread('high_level_alchemy/magic.png', IMREAD_COLOR)
    steel_2h_sword_image: ndarray = imread('high_level_alchemy/steel_2h_sword.png', IMREAD_COLOR)
    steel_battleaxe_image: ndarray = imread('high_level_alchemy/steel_battleaxe.png', IMREAD_COLOR)
    steel_plateskirt_image: ndarray = imread('high_level_alchemy/steel_plateskirt.png', IMREAD_COLOR)

    is_game_opened: bool = False
    
    is_magic_triggered: bool = False
    is_stack_item_found: bool = False

    game_status: GameStatus = GameStatus()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()

        if not is_game_opened:
            is_game_opened = _is_found(game_image, screenshot)

            print('game_opened', is_game_opened)
        
        if is_game_opened:
            if not is_magic_triggered and _find_and_click(magic_image, screenshot, LEFT):
                is_magic_triggered = True

                print('magic_triggered')

            elif not is_stack_item_found and (
                    _find_and_click(steel_2h_sword_image, screenshot, LEFT) 
                    or _find_and_click(steel_battleaxe_image, screenshot, LEFT)
                    or _find_and_click(steel_plateskirt_image, screenshot, LEFT)  
                ):
                is_stack_item_found = True

                print('stack_item_found')

            if is_magic_triggered and is_stack_item_found:
                is_magic_triggered = False
                is_stack_item_found = False

                print('reset')

                

if __name__ == "__main__":
    high_level_alchemy()
