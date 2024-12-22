#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy

from code.Spaceship import Spaceship


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        match entity_name:
            case 'Level1':
                list_bg = []
                for i in range(5): #LEVEL1 IMAGES NUMBER
                    list_bg.append(Background(f'Level1Bg{i + 1}', (0,0)))

                return list_bg

            case 'Level2':
                list_bg = []
                for i in range(5):   #LEVEL2 IMAGES NUMBER
                    list_bg.append(Background(f'Level2Bg{i + 1}', (0,0)))
                return list_bg

            case 'Level3':
                list_bg = []
                for i in range(5):   #LEVEL3 IMAGES NUMBER
                    list_bg.append(Background(f'Level3Bg{i + 1}', (0,0)))

                return list_bg

            case 'Level4':
                list_bg = []
                for i in range(5):   #LEVEL4 IMAGES NUMBER
                    list_bg.append(Background(f'Level4Bg{i + 1}', (0,0)))

                return list_bg

            case 'Level5':
                list_bg = []
                for i in range(5):   #LEVEL5 IMAGES NUMBER
                    list_bg.append(Background(f'Level5Bg{i + 1}', (0,0)))

                return list_bg

            case 'Level6':
                list_bg = []
                for i in range(5):   #LEVEL6 IMAGES NUMBER
                    list_bg.append(Background(f'Level6Bg{i + 1}', (0,0)))

                return list_bg

            case 'Level7':
                list_bg = []
                for i in range(5):   #LEVEL7 IMAGES NUMBER
                    list_bg.append(Background(f'Level7Bg{i + 1}', (0,0)))

                return list_bg

            case 'Level8':
                list_bg = []
                for i in range(5):   #LEVEL8 IMAGES NUMBER
                    list_bg.append(Background(f'Level8Bg{i + 1}', (0,0)))

                return list_bg

            case 'Enemy':
                return Enemy('Enemy', (WIN_WIDTH, WIN_HEIGHT/2))

            case 'Spaceship1':
                return Spaceship('Spaceship1', (position[0], position[1]))

            case 'Spaceship2':
                return Spaceship('Spaceship2', (position[0], position[1]))

            case 'Spaceship3':
                return Spaceship('Spaceship3', (position[0], position[1]))

            case 'Spaceship4':
                return Spaceship('Spaceship4', (position[0], position[1]))

            case 'Spaceship5':
                return Spaceship('Spaceship5', (position[0], position[1]))

            case 'Spaceship1-menu':
                return Spaceship('Spaceship1-menu', (position[0], position[1]))

            case 'Spaceship2-menu':
                return Spaceship('Spaceship2-menu', (position[0], position[1]))

            case 'Spaceship3-menu':
                return Spaceship('Spaceship3-menu', (position[0], position[1]))

            case 'Spaceship4-menu':
                return Spaceship('Spaceship4-menu', (position[0], position[1]))

            case 'Spaceship5-menu':
                return Spaceship('Spaceship5-menu', (position[0], position[1]))





