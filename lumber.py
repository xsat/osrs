
from cv2 import imread, IMREAD_COLOR
from mouse import click, move, LEFT, RIGHT
from numpy import ndarray
from screenshot import make_screenshot
from point import find_point, Point
from game_status import GameStatus
from character import Character


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


def osrs_lumber() -> None:
    game_image: ndarray = imread('images/game.png', IMREAD_COLOR)
    full_inventory_image: ndarray = imread('lumber/full_inventory.png', IMREAD_COLOR)
    bank_booth_image: ndarray = imread('lumber/bank_booth.png', IMREAD_COLOR)
    started_point_image: ndarray = imread('lumber/started_point.png', IMREAD_COLOR)
    first_tree_image: ndarray = imread('lumber/first_tree.png', IMREAD_COLOR)

    is_game_opened: bool = False
    is_going_to_started_point: bool = False
    is_going_to_open_bank: bool = False
    
    is_going_to_first_tree: bool = False
    is_chopping_first_tree: bool = False

    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        character.check_move()

        screenshot: ndarray = make_screenshot()

        if not is_game_opened:
            is_game_opened = _is_found(game_image, screenshot)

            print('game_opened', is_game_opened)
        
        if is_game_opened:
            if not character.is_moving():
                if not is_going_to_started_point and _find_and_click(started_point_image, screenshot, LEFT):
                    is_going_to_started_point = True
                    character.make_moving()
                    print('going_to_started_point')
                elif (not is_going_to_open_bank and _is_found(full_inventory_image, screenshot)
                      and _find_and_click(bank_booth_image, screenshot, LEFT)):
                    is_going_to_open_bank = True
                    character.make_moving()
                    print('going_to_open_bank')
                elif not is_going_to_first_tree and _find_and_click(first_tree_image, screenshot, LEFT):
                    is_going_to_first_tree = True
                    character.make_moving()
                    print('going_to_first_tree')
                elif not is_chopping_first_tree and _find_and_click(first_tree_image, screenshot, LEFT):
                    is_chopping_first_tree = True
                    character.make_moving()
                    print('chopping_first_tree')

                # if is_going_to_started_point and is_going_to_first_tree and is_chopping_first_tree and is_going_to_bank:
                #     is_going_to_started_point = False
                #     is_going_to_first_tree = False
                #     is_chopping_first_tree = False
                #     is_going_to_bank = False
                #     character.make_moving()
                #     print('reset')

            # if not character.is_moving():
            #     print("Not moving")
                

if __name__ == "__main__":
    osrs_lumber()
