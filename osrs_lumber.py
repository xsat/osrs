from cv2 import imread, IMREAD_COLOR
from mouse import LEFT, RIGHT
from numpy import ndarray

from osrs.screenshot import make_screenshot
from osrs.match import is_found, find_and_click
from osrs.game_status import GameStatus
from osrs.character import Character


def osrs_lumber() -> None:
    started_point_image: ndarray = imread('lumber/started_point.png', IMREAD_COLOR)

    full_inventory_image: ndarray = imread('lumber/full_inventory.png', IMREAD_COLOR)
    bank_booth_image: ndarray = imread('lumber/bank_booth.png', IMREAD_COLOR)
    bank_booth_2_image: ndarray = imread('lumber/bank_booth_2.png', IMREAD_COLOR)
    bank_tab_1_image: ndarray = imread('lumber/bank_tab_1.png', IMREAD_COLOR)
    logs_image: ndarray = imread('lumber/logs.png', IMREAD_COLOR)
    deposit_all_image: ndarray = imread('lumber/deposit_all.png', IMREAD_COLOR)

    first_tree_image: ndarray = imread('lumber/first_tree.png', IMREAD_COLOR)

    is_going_to_started_point: bool = False

    is_going_to_open_bank: bool = False
    is_opening_bank: bool = False
    is_logs_selected: bool = False
    is_logs_deposited: bool = False

    is_going_to_first_tree: bool = False

    is_chopping_first_tree: bool = False

    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()
        game_status.check_game(screenshot)
        character.check_move()
        
        if game_status.is_opened():
            if not character.is_moving():
                if not is_going_to_started_point and find_and_click(started_point_image, screenshot, LEFT):
                    is_going_to_started_point = True
                    character.make_moving()
                    print('going_to_started_point')


                elif (not is_going_to_open_bank and is_found(full_inventory_image, screenshot)
                      and find_and_click(bank_booth_image, screenshot, LEFT)):
                    is_going_to_open_bank = True
                    character.make_moving()
                    print('going_to_open_bank')
                elif not is_opening_bank and find_and_click(bank_booth_2_image, screenshot, LEFT):
                    is_opening_bank = True
                    character.make_moving()
                    print('opening_bank')
                elif (not is_logs_selected and is_found(bank_tab_1_image, screenshot) 
                      and find_and_click(logs_image, screenshot, RIGHT)):
                    is_logs_selected = True
                    character.make_moving()
                    print('logs_selected')
                elif not is_logs_deposited and find_and_click(deposit_all_image, screenshot, LEFT):
                    is_logs_deposited = True
                    character.make_moving()
                    print('logs_deposited')


                elif not is_going_to_first_tree and find_and_click(first_tree_image, screenshot, LEFT):
                    is_going_to_first_tree = True
                    character.make_moving()
                    print('going_to_first_tree')
                elif not is_chopping_first_tree and find_and_click(first_tree_image, screenshot, LEFT):
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

            if character.is_moving():
                print("Is moving")
                

if __name__ == "__main__":
    osrs_lumber()
