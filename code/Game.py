import time

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, GAME_LEVELS, MAX_LEVEL_ENEMIES
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.SelectionMenu import SelectionMenu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        spaceship = 1
        score = {'name':'',
                 'level_arrived': '',
                 'time':'',
                 'enemies_destroyed':0}

        while True:
            start_time = time.time()
            end_time = ''
            menu = Menu(self.window)
            menu_return = menu.run()
            score_screen = Score(self.window)

            if menu_return == MENU_OPTION[0]:
                for level in GAME_LEVELS:
                        level_instance = Level(self.window, level, spaceship)
                        level_score = level_instance.run()
                        score['level_arrived'] = level_instance.name
                        score['enemies_destroyed'] += level_score

                        if level_score < MAX_LEVEL_ENEMIES[level_instance.name]:
                            end_time = time.time()
                            break

            if menu_return == MENU_OPTION[1]:
                selection_menu = SelectionMenu(self.window)
                spaceship = selection_menu.run()

            if menu_return == MENU_OPTION[2]:
                score_screen.show()

            if menu_return == MENU_OPTION[3]:
                pygame.quit()

            if end_time != '':
                score['time'] = end_time - start_time
                score_screen.save(score)
                score_screen.show()
                print(score)