import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_GREEN, C_WHITE, C_YELLOW
from code.EntityFactory import EntityFactory


class SelectionMenu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Level1Bg1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 1

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            create_text(self, 60, 'Alien Invasion', C_GREEN, (WIN_WIDTH / 2, 40))
            create_text(self, 40, 'Choose your spaceship', C_YELLOW, (WIN_WIDTH / 2, 100))

            create_text(self, 100, '<', C_WHITE, ((WIN_WIDTH / 2 - 110), (WIN_HEIGHT / 2 + 60)))
            spaceship = EntityFactory.get_entity(f'Spaceship{menu_option}-menu', ((WIN_WIDTH / 2 - 60), (WIN_HEIGHT / 2)))
            create_text(self, 100, '>', C_WHITE, ((WIN_WIDTH / 2 + 110), (WIN_HEIGHT / 2 + 60)))
            if spaceship:
                self.window.blit(source=spaceship.surf, dest=spaceship.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if  menu_option == 5:
                            menu_option = 1
                        else:
                            menu_option += 1

                    if event.key == pygame.K_LEFT:
                        if menu_option == 1:
                            menu_option = 5
                        else:
                            menu_option -= 1

                    if event.key == pygame.K_RETURN:
                        return menu_option



def create_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(source=text_surf, dest=text_rect)
