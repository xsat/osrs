from mouse import on_middle_click


class GameStatus():
    def __init__(self):
        self.__is_runing: bool = True

        on_middle_click(self.__stop)

    def __stop(self) -> None:
        self.__is_runing: bool = False

    def is_runing(self) -> bool:
        return self.__is_runing
