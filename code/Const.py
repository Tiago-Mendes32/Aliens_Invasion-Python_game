import pygame

# C
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (253, 208, 23)
C_GREEN = (0, 255, 0)

# E
ENEMY_SPAWN_TIME = {
    'Level1': 4000,
    'Level2': 3500,
    'Level3': 3000,
    'Level4': 2500,
    'Level5': 2000,
    'Level6': 1500,
    'Level7': 1000,
    'Level8': 500,
}

ENTITY_DAMAGE = {
    'Spaceship1-menu': 99999,
    'Spaceship2-menu': 99999,
    'Spaceship3-menu': 99999,
    'Spaceship4-menu': 99999,
    'Spaceship5-menu': 99999,
    'Spaceship1': 3,
    'Spaceship2': 3,
    'Spaceship3': 3,
    'Spaceship4': 3,
    'Spaceship5': 3,
    'Enemy': 5,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,
    'Level4Bg3': 0,
    'Level4Bg4': 0,
    'Level4Bg5': 0,
    'Level5Bg1': 0,
    'Level5Bg2': 0,
    'Level5Bg3': 0,
    'Level5Bg4': 0,
    'Level5Bg5': 0,
    'Level6Bg1': 0,
    'Level6Bg2': 0,
    'Level6Bg3': 0,
    'Level6Bg4': 0,
    'Level6Bg5': 0,
    'Level7Bg1': 0,
    'Level7Bg2': 0,
    'Level7Bg3': 0,
    'Level7Bg4': 0,
    'Level7Bg5': 0,
    'Level8Bg1': 0,
    'Level8Bg2': 0,
    'Level8Bg3': 0,
    'Level8Bg4': 0,
    'Level8Bg5': 0,
    'Spaceship1-shoot': 1,
    'Spaceship2-shoot': 1,
    'Spaceship3-shoot': 1,
    'Spaceship4-shoot': 1,
    'Spaceship5-shoot': 1,
    'Enemy-shoot': 1
}

ENTITY_HEALTH = {
    'Spaceship1-menu': 99999,
    'Spaceship2-menu': 99999,
    'Spaceship3-menu': 99999,
    'Spaceship4-menu': 99999,
    'Spaceship5-menu': 99999,
    'Spaceship1': 3,
    'Spaceship2': 3,
    'Spaceship3': 3,
    'Spaceship4': 3,
    'Spaceship5': 3,
    'Enemy': 3,
    'Level1Bg1': 99999,
    'Level1Bg2': 99999,
    'Level1Bg3': 99999,
    'Level1Bg4': 99999,
    'Level1Bg5': 99999,
    'Level2Bg1': 99999,
    'Level2Bg2': 99999,
    'Level2Bg3': 99999,
    'Level2Bg4': 99999,
    'Level2Bg5': 99999,
    'Level3Bg1': 99999,
    'Level3Bg2': 99999,
    'Level3Bg3': 99999,
    'Level3Bg4': 99999,
    'Level3Bg5': 99999,
    'Level4Bg1': 99999,
    'Level4Bg2': 99999,
    'Level4Bg3': 99999,
    'Level4Bg4': 99999,
    'Level4Bg5': 99999,
    'Level5Bg1': 99999,
    'Level5Bg2': 99999,
    'Level5Bg3': 99999,
    'Level5Bg4': 99999,
    'Level5Bg5': 99999,
    'Level6Bg1': 99999,
    'Level6Bg2': 99999,
    'Level6Bg3': 99999,
    'Level6Bg4': 99999,
    'Level6Bg5': 99999,
    'Level7Bg1': 99999,
    'Level7Bg2': 99999,
    'Level7Bg3': 99999,
    'Level7Bg4': 99999,
    'Level7Bg5': 99999,
    'Level8Bg1': 99999,
    'Level8Bg2': 99999,
    'Level8Bg3': 99999,
    'Level8Bg4': 99999,
    'Level8Bg5': 99999,
    'Spaceship1-shoot': 1,
    'Spaceship2-shoot': 1,
    'Spaceship3-shoot': 1,
    'Spaceship4-shoot': 1,
    'Spaceship5-shoot': 1,
    'Enemy-shoot': 1
}

ENTITY_SHOOT_DELAY = {
    'Spaceship1-shoot': 25,
    'Spaceship2-shoot': 25,
    'Spaceship3-shoot': 25,
    'Spaceship4-shoot': 25,
    'Spaceship5-shoot': 25,
    'Spaceship1-menu-shoot': 40,
    'Spaceship2-menu-shoot': 40,
    'Spaceship3-menu-shoot': 40,
    'Spaceship4-menu-shoot': 40,
    'Spaceship5-menu-shoot': 40,
    'Enemy-shoot': 100
}

ENTITY_SPEED = {
    'Spaceship1': 3,
    'Spaceship2': 3,
    'Spaceship3': 3,
    'Spaceship4': 3,
    'Spaceship5': 3,
    'Enemy': 0.51,
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 1.5,
    'Level1Bg4': 2,
    'Level1Bg5': 2.5,
    'Level2Bg1': 0,
    'Level2Bg2': 1,
    'Level2Bg3': 1.5,
    'Level2Bg4': 2,
    'Level2Bg5': 2.5,
    'Level3Bg1': 0,
    'Level3Bg2': 1,
    'Level3Bg3': 1.5,
    'Level3Bg4': 2,
    'Level3Bg5': 2.5,
    'Level4Bg1': 0,
    'Level4Bg2': 1,
    'Level4Bg3': 1.5,
    'Level4Bg4': 2,
    'Level4Bg5': 2.5,
    'Level5Bg1': 0,
    'Level5Bg2': 1,
    'Level5Bg3': 1.5,
    'Level5Bg4': 2,
    'Level5Bg5': 2.5,
    'Level6Bg1': 0,
    'Level6Bg2': 1,
    'Level6Bg3': 1.5,
    'Level6Bg4': 2,
    'Level6Bg5': 2.5,
    'Level7Bg1': 0,
    'Level7Bg2': 1,
    'Level7Bg3': 1.5,
    'Level7Bg4': 2,
    'Level7Bg5': 2.5,
    'Level8Bg1': 0,
    'Level8Bg2': 1,
    'Level8Bg3': 1.5,
    'Level8Bg4': 2,
    'Level8Bg5': 2.5,
    'Spaceship1-shoot': 3,
    'Spaceship2-shoot': 3,
    'Spaceship3-shoot': 3,
    'Spaceship4-shoot': 3,
    'Spaceship5-shoot': 3,
    'Enemy-shoot': 1.5
}

# G
GAME_LEVELS = [
    'Level1',
    'Level2',
    'Level3',
    'Level4',
    'Level5',
    'Level6',
    'Level7',
    'Level8',
]

# L
LEVEL_TIMEOUT = 30000

# M
MAX_ENEMIES_TO_SPAWN = {
    'Level1': 4,
    'Level2': 5,
    'Level3': 6,
    'Level4': 6,
    'Level5': 8,
    'Level6': 9,
    'Level7': 10,
    'Level8': 10,
}

MAX_LEVEL_ENEMIES = {
    'Level1': 10,
    'Level2': 12,
    'Level3': 15,
    'Level4': 18,
    'Level5': 20,
    'Level6': 22,
    'Level7': 25,
    'Level8': 30,
}

MENU_OPTION = ('PLAY GAME',
               'CHOSE SPACESHIP',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = pygame.K_UP
PLAYER_KEY_DOWN = pygame.K_DOWN
PLAYER_KEY_RIGHT = pygame.K_RIGHT
PLAYER_KEY_LEFT = pygame.K_LEFT
PLAYER_KEY_SHOOT = pygame.K_RCTRL

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}
