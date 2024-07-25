from cv2 import imread, IMREAD_COLOR
from mouse import LEFT, RIGHT
from numpy import ndarray
from osrs.screenshot import make_screenshot
from osrs.match import is_found, find_and_click
from osrs.game_status import GameStatus
from osrs.character import Character


def osrs_miner() -> None:
    game_image: ndarray = imread('common/game.png', IMREAD_COLOR)

    game_status: GameStatus = GameStatus()
    character: Character = Character()

    while game_status.is_runing():
        character.check_move()

        screenshot: ndarray = make_screenshot()

        if not is_game_opened:
            is_game_opened = is_found(game_image, screenshot)

            print('game_opened', is_game_opened)
        
        if is_game_opened:
            if not character.is_moving():
               print("Is not moving")
            if character.is_moving():
                print("Is moving")
                

if __name__ == "__main__":
    osrs_miner()
