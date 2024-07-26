from mouse import LEFT, RIGHT
from numpy import ndarray

from osrs.screenshot import make_screenshot
from osrs.match import is_found, find_and_click
from osrs.game_status import GameStatus
from osrs.character import Character


MINING: int = 1

MOVING_TO_BANK: int = 2
MOVING_TO_MINING_SITE: int = 3


def osrs_miner() -> None:
    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()
        game_status.check_game(screenshot)
        character.check_move()
        
        if game_status.is_opened():
            if character.is_moving():
                print("Is moving")
            else:
               print("Is not moving") 
                

if __name__ == "__main__":
    osrs_miner()
