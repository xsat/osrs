
from mss import mss
from mss.base import MSSBase
from cv2 import imread, IMREAD_COLOR
from mouse import click, move, LEFT, RIGHT

from screenshot import make_screenshot, ndarray
from point import find_point, Point


def _find_and_click(image: ndarray, screenshot: ndarray, button: str) -> bool:
    found_point: Point | None = find_point(image, screenshot)
    if found_point != None:
        move(found_point[0], found_point[1])
        click(button)
        
        return True

    return False


def osrs() -> None:
    base: MSSBase = mss()
    game: Point | None = None
    game_image: ndarray = imread('images/game.png', IMREAD_COLOR)
    carpet_image: ndarray = imread('images/carpet.png', IMREAD_COLOR)
    npc_head_image: ndarray = imread('images/npc_head.png', IMREAD_COLOR)
    top_papers_image: ndarray = imread('images/top_papers.png', IMREAD_COLOR)
    right_papers_image: ndarray = imread('images/right_papers.png', IMREAD_COLOR)

    while True:
        if game == None:
            screenshot: ndarray = make_screenshot(base)
            game: Point | None = find_point(game_image, screenshot)
        
        if game != None:
            print('Game is started')
            # move(game[0], game[1])

            _find_and_click(npc_head_image, screenshot, RIGHT)

            # top_papers: Point | None = find_point(top_papers_image, screenshot)
            # if top_papers != None:
            #     move(top_papers[0], top_papers[1])
            #     click(LEFT)
            #     break
            
            # right_papers: Point | None = find_point(right_papers_image, screenshot)
            # if right_papers != None:
            #     move(right_papers[0], right_papers[1])
            #     click(LEFT)
            #     break

            # print(top_papers, right_papers)
            # break

            # if bookshelf != None:
            #     move(bookshelf[0], bookshelf[1])
            #     click(LEFT)
            #     break
 

if __name__ == "__main__":
    osrs() 
