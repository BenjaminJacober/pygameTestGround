import pygame
import sys

from Sprite import Orientation, Tank_Sprite

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Thing")

BLACK = (0, 0, 0)

class Game:
    square_size = 50
    square_x = (screen_width - square_size) // 2
    square_y = (screen_height - square_size) // 2
    speed = 5
    tank = Tank_Sprite(screen)
    orientation = Orientation.LEFT    
    # def __init__(self):

    def handleKeyboadInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.square_y -= self.speed
            self.orientation = Orientation.UP
        if keys[pygame.K_DOWN]:
            self.square_y += self.speed
            self.orientation = Orientation.DOWN
        if keys[pygame.K_LEFT]:
            self.square_x -= self.speed
            self.orientation = Orientation.LEFT
        if keys[pygame.K_RIGHT]:
            self.square_x += self.speed
            self.orientation = Orientation.RIGHT
            
    def mainLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            self.handleKeyboadInput()
        
            screen.fill(BLACK)
            sprite = self.tank.getSprite(self.orientation)
            screen.blit(sprite, (self.square_x, self.square_y))
        
            pygame.display.flip()
            pygame.time.Clock().tick(60)
        
        pygame.quit()
        sys.exit()
        
game = Game()
game.mainLoop()