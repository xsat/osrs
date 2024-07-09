
from cv2 import imread, IMREAD_COLOR
from mouse import click, move, LEFT, RIGHT
from numpy import ndarray
from screenshot import make_screenshot
from point import find_point, Point
from game_status import GameStatus
from character import Character
# from enum import Enum


# class Action(Enum):
#     IS_GOING_TO_STARTER_POINT: int = 100
#     IS_GOING_TO_FIRST_TREE: int = 200
#     IS_CHOPPING_FIRST_TREE: int = 201
#     IS_GOING_TO_BANK: int = 300



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
    game_status: GameStatus = GameStatus()
    # on_middle_click(status.stop)

    game: Point | None = None
    game_image: ndarray = imread('images/game.png', IMREAD_COLOR)
    started_point_image: ndarray = imread('lumber/started_point.png', IMREAD_COLOR)
    first_tree_image: ndarray = imread('lumber/first_tree.png', IMREAD_COLOR)
    full_inventory_image: ndarray = imread('lumber/full_inventory.png', IMREAD_COLOR)


    is_going_to_started_point: bool = False
    is_going_to_bank: bool = False
    is_going_to_first_tree: bool = False
    is_chopping_first_tree: bool = False


    # a: Action = Action(Action.IS_GOING_TO_STARTER_POINT)

    # print(a)



    character: Character = Character()

    while game_status.is_runing():
        character.check_move()

        screenshot: ndarray = make_screenshot()

        if game == None:
            game: Point | None = find_point(game_image, screenshot)
        
        if game != None:
            print('Game is running')

            if not character.is_moving():
                if not is_going_to_started_point and _find_and_click(started_point_image, screenshot, LEFT):
                    is_going_to_started_point = True
                    print('is_going_to_started_point')

                # if not is_going_to_bank and _is_found(full_inventory_image, screenshot) and _find_and_click(first_tree_image, screenshot, LEFT):
                #     is_going_to_bank = True
                #     print('is_going_to_bank')

                if not is_going_to_first_tree and _find_and_click(first_tree_image, screenshot, LEFT):
                    is_going_to_first_tree = True
                    print('is_going_to_first_tree')

                if not is_chopping_first_tree and _find_and_click(first_tree_image, screenshot, LEFT):
                    is_chopping_first_tree = True
                    print('is_chopping_first_tree')

                # if is_going_to_started_point and is_going_to_first_tree and is_chopping_first_tree and is_going_to_bank:
                #     is_going_to_started_point = False
                #     is_going_to_first_tree = False
                #     is_chopping_first_tree = False
                #     is_going_to_bank = False

                #     print('reset')

            # if not character.is_moving():
            #     print("Not moving")
                

if __name__ == "__main__":
    osrs_lumber()
