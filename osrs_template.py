from numpy import ndarray

from osrs.screenshot import make_screenshot
from osrs.game_status import GameStatus
from osrs.character import Character


def osrs_template() -> None:
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
    osrs_template()
