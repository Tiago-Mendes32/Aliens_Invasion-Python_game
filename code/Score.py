import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from datetime import datetime
import sys

from code.Const import C_YELLOW, C_WHITE, WIN_WIDTH, SCORE_POS, C_BLACK
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Level3Bg1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def play_music(self, music_file: str):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)

    def save(self, player_score: dict):
        self.play_music('./asset/Score.mp3')
        db_proxy = DBProxy('DBScore')
        name = ''
        level_arrived = player_score['level_arrived']
        time = player_score['time']
        enemies_destroyed = player_score['enemies_destroyed']

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({
                            'name': name,
                            'enemies_destroyed': enemies_destroyed,
                            'level_arrived': level_arrived,
                            'time': time,
                            'date': get_formatted_date()
                        })
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 4 and event.unicode.isalnum():
                        name += event.unicode

            self.score_text(20, name, C_YELLOW, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        self.play_music('./asset/Score.mp3')
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, (WIN_WIDTH / 2, 50))

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for index, player_score in enumerate(list_score):
            # Ajustando os índices para corresponder à ordem correta dos campos no banco de dados
            id = player_score[0]
            name = player_score[1]
            enemies_destroyed = player_score[2]
            level_arrived = player_score[3]
            time = player_score[4]
            date = player_score[5]

            self.score_text(15,
                            f'NAME: {name} - ENEMIES DESTROYED: {enemies_destroyed} - LEVEL ARRIVED: {level_arrived} - TIME: {time:.2f}s - DATE: {date}',
                            C_BLACK, SCORE_POS[index])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    elif event.key == K_RETURN:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Open Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date} - {current_time}"
