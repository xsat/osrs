from cv2 import imread, IMREAD_COLOR
from mouse import LEFT, RIGHT
from numpy import ndarray

from osrs.screenshot import make_screenshot
from osrs.match import is_found, find_and_click
from osrs.game_status import GameStatus
from osrs.character import Character


UNDEFINED: int = 0

MINING: int = 1

MOVING_TO_BANK: int = 2
MOVING_TO_MINING_SITE: int = 3


def osrs_miner() -> None:
    status: int = UNDEFINED

    inventory_is_too_ful_image: ndarray = imread('miner/inventory_is_too_full.png', IMREAD_COLOR)
    clay_rocks_image: ndarray = imread('miner/clay_rocks.png', IMREAD_COLOR)

    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()
        game_status.check_game(screenshot)
        character.check_move()
        
        if game_status.is_opened():
            if is_found(inventory_is_too_ful_image, screenshot):
                print("Inventory is too full")
            else:
                print("Inventory is not full")
            
            if character.is_moving():
                print("Is moving")
            else:
               print("Is not moving") 
                

if __name__ == "__main__":
    osrs_miner()
