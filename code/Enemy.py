import random

from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, ENTITY_SHOOT_DELAY
from code.Entity import Entity
from code.EnemyShoot import EnemyShoot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name + '-shoot']
        self.direction_x = 1
        self.speed_x = ENTITY_SPEED[self.name]
        self.direction_y = random.choice([1, -1])

    def move(self):

        #Horizontal moviments
        if self.rect.centerx >= WIN_WIDTH / 2:
            self.rect.centerx -= self.speed_x * self.direction_x
        else:
            self.direction_x = -1
            self.rect.centerx += 1
        if self.rect.centerx == WIN_WIDTH-15:
            self.direction_x = 1

        #Vertical moviments
        self.rect.centery += 1 * self.direction_y

        if self.rect.centery == WIN_HEIGHT-15 or self.rect.centery == 15:
            self.direction_y *= -1


    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name + '-shoot']
            return EnemyShoot(name=self.name + '-shoot', position=(self.rect.centerx - 60, self.rect.centery))
