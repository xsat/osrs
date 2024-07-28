from cv2 import imread, IMREAD_COLOR
from mouse import LEFT, RIGHT
from numpy import ndarray

from osrs.screenshot import make_screenshot
from osrs.match import is_found, find_and_click
from osrs.game_status import GameStatus
from osrs.character import Character


UNDEFINED_STATUS: int = 0
MINING_STATUS: int = 1
MOVING_TO_BANK_STATUS: int = 2
MOVING_TO_MINING_SITE_STATUS: int = 3

UNDEFINED_ACTION: int = 0
FROM_1_CHECKPOINT_ACTION: int = 1
FROM_2_CHECKPOINT_ACTION: int = 2
FROM_3_CHECKPOINT_ACTION: int = 3
BANK_BOOTH_ACTION: int = 4
CLAY_IN_INVENTORY_ACTION: int = 5
DEPOSIT_ALL_ACTION: int = 6


def osrs_miner() -> None:
    status: int = MOVING_TO_BANK_STATUS
    action: int = FROM_1_CHECKPOINT_ACTION

    inventory_is_too_full_image: ndarray = imread('miner/inventory_is_too_full.png', IMREAD_COLOR)
    clay_rocks_image: ndarray = imread('miner/clay_rocks.png', IMREAD_COLOR)

    from_1_checkpoint_image: ndarray = imread('miner/from_1_checkpoint.png', IMREAD_COLOR)
    from_2_checkpoint_image: ndarray = imread('miner/from_2_checkpoint.png', IMREAD_COLOR)
    from_3_checkpoint_image: ndarray = imread('miner/from_3_checkpoint.png', IMREAD_COLOR)
    bank_booth_image: ndarray = imread('miner/bank_booth.png', IMREAD_COLOR)
    tab_1_image: ndarray = imread('miner/tab_1.png', IMREAD_COLOR)
    clay_in_inventory_image: ndarray = imread('miner/clay_in_inventory.png', IMREAD_COLOR)
    deposit_all_image: ndarray = imread('miner/deposit_all.png', IMREAD_COLOR)

    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()
        game_status.check_game(screenshot)
        character.check_move()
        
        if game_status.is_opened() and not character.is_moving():
            # if is_found(inventory_is_too_full_image, screenshot):
            #     print("Inventory is too full")
            # else:
            #     print("Inventory is not full")
            
            if status == MOVING_TO_BANK_STATUS:
                if action == FROM_1_CHECKPOINT_ACTION and find_and_click(from_1_checkpoint_image, screenshot, LEFT):
                    print("from_1_checkpoint_image")
                    action = FROM_2_CHECKPOINT_ACTION

                elif action == FROM_2_CHECKPOINT_ACTION and find_and_click(from_2_checkpoint_image, screenshot, LEFT):
                    print("from_2_checkpoint_image")
                    action = FROM_3_CHECKPOINT_ACTION

                elif action == FROM_3_CHECKPOINT_ACTION and find_and_click(from_3_checkpoint_image, screenshot, LEFT):
                    print("from_3_checkpoint_image")
                    action = BANK_BOOTH_ACTION

                elif action == BANK_BOOTH_ACTION and find_and_click(bank_booth_image, screenshot, LEFT):
                    print("bank_booth")
                    action = CLAY_IN_INVENTORY_ACTION
                
                elif action == CLAY_IN_INVENTORY_ACTION and is_found(tab_1_image, screenshot) and find_and_click(clay_in_inventory_image, screenshot, RIGHT):
                    print("clay_in_inventory_image")
                    action = DEPOSIT_ALL_ACTION

                elif action == DEPOSIT_ALL_ACTION and find_and_click(deposit_all_image, screenshot, LEFT):
                    print("deposit_all")
                    action = UNDEFINED_ACTION

            # if character.is_moving():
            #     print("Is moving")
            # else:
            #    print("Is not moving") 
                

if __name__ == "__main__":
    osrs_miner()
