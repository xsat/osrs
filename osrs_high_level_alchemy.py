from cv2 import imread, IMREAD_COLOR
from mouse import LEFT
from numpy import ndarray
from osrs.screenshot import make_screenshot
from osrs.match import is_found, find_and_click
from osrs.game_status import GameStatus


def osrs_high_level_alchemy() -> None:
    game_image: ndarray = imread('common/game.png', IMREAD_COLOR)

    magic_image: ndarray = imread('high_level_alchemy/magic.png', IMREAD_COLOR)
    steel_2h_sword_image: ndarray = imread('high_level_alchemy/steel_2h_sword.png', IMREAD_COLOR)
    steel_battleaxe_image: ndarray = imread('high_level_alchemy/steel_battleaxe.png', IMREAD_COLOR)
    steel_plateskirt_image: ndarray = imread('high_level_alchemy/steel_plateskirt.png', IMREAD_COLOR)
    steel_platelegs_image: ndarray = imread('high_level_alchemy/steel_platelegs.png', IMREAD_COLOR)

    is_game_opened: bool = False
    
    is_magic_triggered: bool = False
    is_stack_item_found: bool = False

    game_status: GameStatus = GameStatus()

    while game_status.is_runing():
        screenshot: ndarray = make_screenshot()

        if not is_game_opened:
            is_game_opened = is_found(game_image, screenshot)

            print('game_opened', is_game_opened)
        
        if is_game_opened:
            if not is_magic_triggered and find_and_click(magic_image, screenshot, LEFT):
                is_magic_triggered = True

                print('magic_triggered')

            elif not is_stack_item_found and (
                    find_and_click(steel_2h_sword_image, screenshot, LEFT) 
                    or find_and_click(steel_battleaxe_image, screenshot, LEFT)
                    or find_and_click(steel_plateskirt_image, screenshot, LEFT)
                    or find_and_click(steel_platelegs_image, screenshot, LEFT)  
                ):
                is_stack_item_found = True

                print('stack_item_found')

            if is_magic_triggered and is_stack_item_found:
                is_magic_triggered = False
                is_stack_item_found = False

                print('reset')

                

if __name__ == "__main__":
    osrs_high_level_alchemy()
