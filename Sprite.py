import pygame
from enum import Enum

class Orientation(Enum):
    LEFT = 1
    LEFT_DOWN = 2
    DOWN = 3
    RIGHT_DOWN = 4
    RIGHT = 5
    RIGHT_UP = 6
    UP = 7
    LEFT_UP = 8

class Tank_Sprite():

    tankLeft = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull1.png")#.convert_alpha()
    tankLeftDown = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull2.png")#.convert_alpha()
    tankDown = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull3.png")#.convert_alpha()
    tankRightDown = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull4.png")#.convert_alpha()
    tankRight = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull5.png")#.convert_alpha()
    tankRightUp = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull6.png")#.convert_alpha()
    tankUp = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull7.png")#.convert_alpha()
    tankLeftUp = pygame.image.load("./assets/Panzer4_export/Separated/Hull/german_panzer4_hull8.png")#.convert_alpha()

    def __init__(self, screen):
        print("garbage")
        
    def getSprite(self, hullOrientation):
        hullSprite = 0
        match hullOrientation:
            case Orientation.LEFT:
                hullSprite = Tank_Sprite.tankLeft
            case Orientation.LEFT_DOWN:
                hullSprite = Tank_Sprite.tankLeftDown
            case Orientation.DOWN:
                hullSprite = Tank_Sprite.tankDown
            case Orientation.RIGHT_DOWN:
                hullSprite = Tank_Sprite.tankRightDown
            case Orientation.RIGHT:
                hullSprite = Tank_Sprite.tankRight
            case Orientation.RIGHT_UP:
                hullSprite = Tank_Sprite.tankRightUp
            case Orientation.UP:
                hullSprite = Tank_Sprite.tankUp
            case Orientation.LEFT_UP:
                hullSprite = Tank_Sprite.tankLeftUp
        return hullSprite
