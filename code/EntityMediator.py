from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShoot
from code.Entity import Entity
from code.Spaceship import Spaceship
from code.SpaceshipShoot import SpaceshipShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right < 0:
                entity.health = 0

        if isinstance(entity, SpaceshipShoot):
            if entity.rect.left >= WIN_WIDTH:
                entity.health = 0

        if isinstance(entity, EnemyShoot):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_colision = False
        if isinstance(ent1, Enemy) and isinstance(ent2, SpaceshipShoot):
            valid_colision = True
        if isinstance(ent1, SpaceshipShoot) and isinstance(ent2, Enemy):
            valid_colision = True
        if isinstance(ent1, Spaceship) and isinstance(ent2, EnemyShoot):
            valid_colision = True
        if isinstance(ent1, EnemyShoot) and isinstance(ent2, Spaceship):
            valid_colision = True
        if isinstance(ent1, EnemyShoot) and isinstance(ent2, SpaceshipShoot):
            valid_colision = True
        if isinstance(ent1, SpaceshipShoot) and isinstance(ent2, EnemyShoot):
            valid_colision = True

        if valid_colision:
            if (ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def verify_health(entity_list: list[Entity], enemies_destroyed: int):
        to_remove = []
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    enemies_destroyed += 1
                to_remove.append(ent)
        for ent in to_remove:
            entity_list.remove(ent)
        return enemies_destroyed
