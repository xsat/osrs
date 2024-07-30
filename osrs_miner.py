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
# FROM_1_CHECKPOINT_ACTION: int = 1
# FROM_2_CHECKPOINT_ACTION: int = 2
# FROM_3_CHECKPOINT_ACTION: int = 3
# BANK_BOOTH_ACTION: int = 4
# CLAY_IN_INVENTORY_ACTION: int = 5
# DEPOSIT_ALL_ACTION: int = 6

FIRST_CHECKPOINT_ACTION: int = 1
SECOND_CHECKPOINT_ACTION: int = 2
THIRD_CHECKPOINT_ACTION: int = 3
BANK_ACTION: int = 4
MINING_SITE_ACTION: int = 5

def osrs_miner() -> None:
    status: int = MOVING_TO_MINING_SITE_STATUS
    action: int = SECOND_CHECKPOINT_ACTION

    # inventory_is_too_full_image: ndarray = imread('miner/inventory_is_too_full.png', IMREAD_COLOR)
    # clay_rocks_image: ndarray = imread('miner/clay_rocks.png', IMREAD_COLOR)

    # from_1_checkpoint_image: ndarray = imread('miner/from_1_checkpoint.png', IMREAD_COLOR)
    # from_2_checkpoint_image: ndarray = imread('miner/from_2_checkpoint.png', IMREAD_COLOR)
    # from_3_checkpoint_image: ndarray = imread('miner/from_3_checkpoint.png', IMREAD_COLOR)
    # bank_booth_image: ndarray = imread('miner/bank_booth.png', IMREAD_COLOR)
    # tab_1_image: ndarray = imread('miner/tab_1.png', IMREAD_COLOR)
    # clay_in_inventory_image: ndarray = imread('miner/clay_in_inventory.png', IMREAD_COLOR)
    # deposit_all_image: ndarray = imread('miner/deposit_all.png', IMREAD_COLOR)

    first_checkpoint_on_map: ndarray = imread('miner/first_checkpoint_on_map.png', IMREAD_COLOR)
    second_checkpoint_on_map: ndarray = imread('miner/second_checkpoint_on_map.png', IMREAD_COLOR)
    # third_checkpoint_on_map: ndarray = imread('miner/third_checkpoint_on_map.png', IMREAD_COLOR)
    bank_on_map: ndarray = imread('miner/bank_on_map.png', IMREAD_COLOR)
    mining_site_on_map: ndarray = imread('miner/mining_site_on_map.png', IMREAD_COLOR)

    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()
        game_status.check_game(screenshot)
        character.check_move()
        
        if game_status.is_opened() and not character.is_moving():
            print("NOT MOVING")

            # if is_found(inventory_is_too_full_image, screenshot):
            #     print("Inventory is too full")
            # else:
            #     print("Inventory is not full")
            
            if status == MOVING_TO_BANK_STATUS:
                if action == FIRST_CHECKPOINT_ACTION and find_and_click(first_checkpoint_on_map, screenshot, LEFT):
                    print("MOVING_TO_BANK_STATUS            FIRST_CHECKPOINT_ACTION")
                    character.make_moving()

                    action = SECOND_CHECKPOINT_ACTION
                elif action == SECOND_CHECKPOINT_ACTION and find_and_click(second_checkpoint_on_map, screenshot, LEFT):
                    print("MOVING_TO_BANK_STATUS            SECOND_CHECKPOINT_ACTION")
                    character.make_moving()
                    
                    action = BANK_ACTION
                elif action == BANK_ACTION and find_and_click(bank_on_map, screenshot, LEFT):
                    print("MOVING_TO_BANK_STATUS            BANK_ACTION")
                    character.make_moving()
                    
                    action = SECOND_CHECKPOINT_ACTION
                    status = MOVING_TO_MINING_SITE_STATUS
            elif status == MOVING_TO_MINING_SITE_STATUS:
                if action == SECOND_CHECKPOINT_ACTION and find_and_click(second_checkpoint_on_map, screenshot, LEFT):
                    print("MOVING_TO_MINING_SITE_STATUS     SECOND_CHECKPOINT_ACTION")
                    character.make_moving()

                    action = FIRST_CHECKPOINT_ACTION
                elif action == FIRST_CHECKPOINT_ACTION and find_and_click(first_checkpoint_on_map, screenshot, LEFT):
                    print("MOVING_TO_MINING_SITE_STATUS     FIRST_CHECKPOINT_ACTION")
                    character.make_moving()

                    action = MINING_SITE_ACTION
                elif action == MINING_SITE_ACTION and find_and_click(mining_site_on_map, screenshot, LEFT):
                    print("MOVING_TO_MINING_SITE_STATUS     MINING_SITE_ACTION")
                    character.make_moving()

                    action = FIRST_CHECKPOINT_ACTION
                    status = UNDEFINED_STATUS

if __name__ == "__main__":
    osrs_miner()
