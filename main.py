import pygame
import sys
import math

from Tank import Tank
from TankSprite import Orientation

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Thing")

GREEN = (0, 102, 0)

class Game:
	tank = Tank()
	
	def handleKeyboadInput(self):
		keys = pygame.key.get_pressed()
		direction_map = {
			(True, False, False, False): Orientation.UP,
			(False, True, False, False): Orientation.DOWN,
			(False, False, True, False): Orientation.LEFT,
			(False, False, False, True): Orientation.RIGHT,
			(True, False, True, False): Orientation.LEFT_UP,
			(True, False, False, True): Orientation.RIGHT_UP,
			(False, True, True, False): Orientation.LEFT_DOWN,
			(False, True, False, True): Orientation.RIGHT_DOWN,
		}
		up, down, left, right = keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]

		orientation = direction_map.get((up, down, left, right))
		if (orientation != None):
			self.tank.update(orientation, None)
			
	def handleMouse(self):
		self.tank.update(None, pygame.mouse.get_pos())
		
	def draw(self, entities):
		for entity in entities:
			for sprite in entity.draw():
				screen.blit(sprite, entity.pos)
			
	def update(self, entities):
		for entity in entities:
			entity.update()
			
	def mainLoop(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
		
			screen.fill(GREEN)
			self.handleKeyboadInput()
			self.handleMouse()
			self.draw([self.tank])
			# self.update([self.tank])
			
			pygame.display.flip()
			pygame.time.Clock().tick(60)
		
		pygame.quit()
		sys.exit()
		
game = Game()
game.mainLoop()