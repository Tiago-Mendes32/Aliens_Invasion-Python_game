import pygame
from pygame import Surface, Rect
from pygame.font import Font
import random

from code.Const import LEVEL_TIMEOUT, ENEMY_SPAWN_TIME, MAX_ENEMIES_TO_SPAWN, MAX_LEVEL_ENEMIES, WIN_HEIGHT, \
    ENTITY_HEALTH, WIN_WIDTH, C_YELLOW
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Spaceship import Spaceship


class Level:
    def __init__(self, window: Surface, name: str, spaceship: str):
        self.timeout = LEVEL_TIMEOUT
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.enemies_destroyed = 0
        self.max_enemies = MAX_LEVEL_ENEMIES[self.name]
        self.enemies_spawned = []

        self.background = pygame.image.load(f'./asset/{self.name}Bg1.png').convert()

        entities = EntityFactory.get_entity(self.name) or []
        self.entity_list.extend(entities)

        self.spaceship_entity = EntityFactory.get_entity(f'Spaceship{spaceship}', (20, WIN_HEIGHT/2))
        if self.spaceship_entity:
            self.entity_list.append(self.spaceship_entity)

        # Enemies spawn variables
        self.last_enemy_spawn_time = 0
        self.enemies_to_spawn = 1
        self.max_enemies_to_spawn = MAX_ENEMIES_TO_SPAWN[self.name]
        self.enemy_spawn_interval = ENEMY_SPAWN_TIME[self.name]

    def spawn_enemies(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_enemy_spawn_time >= self.enemy_spawn_interval:
            self.last_enemy_spawn_time = current_time

            enemy_entity = EntityFactory.get_entity('Enemy')
            if enemy_entity:
                enemy_entity.rect.centerx = self.window.get_width()
                enemy_entity.rect.centery = random.randint(
                    30, WIN_HEIGHT - 30
                )
                self.entity_list.append(enemy_entity)
                self.enemies_spawned.append(enemy_entity)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Clean screen
            self.window.fill((0, 0, 0))

            # Draw background
            self.window.blit(self.background, (0, 0))

            # Enemies spawn
            if len(self.enemies_spawned) < self.max_enemies and (
                    len(self.enemies_spawned) - self.enemies_destroyed) < self.max_enemies_to_spawn:
                self.spawn_enemies()

            # Render entities
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if isinstance(ent, Spaceship):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)
                ent.move()
                if isinstance(ent, Enemy):
                    enemy_shoot = ent.shoot()
                    if enemy_shoot:
                        self.entity_list.append(enemy_shoot)
                ent.move()

            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # printed text level
            self.level_text(20, f'Player health: {self.spaceship_entity.health}/{ENTITY_HEALTH[self.spaceship_entity.name]}', C_YELLOW, (2, 5))
            self.level_text(20, f'Current level: {self.name}', C_YELLOW, (WIN_WIDTH/2 - 30, 5))
            self.level_text(20, f'Destroyed Enemies: {self.enemies_destroyed}/{MAX_LEVEL_ENEMIES[self.name]}', C_YELLOW, (2, 30))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            self.enemies_destroyed = EntityMediator.verify_health(self.entity_list, self.enemies_destroyed)

            if self.enemies_destroyed == self.max_enemies:
                return self.enemies_destroyed
            if self.spaceship_entity.health == 0:
                return self.enemies_destroyed

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
