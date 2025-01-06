import os

import pygame
from enum import Enum

class Orientation(Enum):
	LEFT = 0
	LEFT_UP = 1
	UP = 2
	RIGHT_UP = 3
	RIGHT = 4
	RIGHT_DOWN = 5
	DOWN = 6
	LEFT_DOWN = 7

class TankSprite():

	hull_path = "./assets/Panzer4_export/Separated/Hull/"
	turret_path = "./assets/Panzer4_export/Separated/Turret/"

	def __init__(self):
		self.hull_sprites = self.loadSprites(self.hull_path)
		self.turret_sprites = self.loadSprites(self.turret_path)
		self.width = self.hull_sprites[Orientation.LEFT].get_width()
		self.height = self.hull_sprites[Orientation.LEFT].get_height()

	def loadSprites(self, base_path):
		sprites = {}
		for orientation in Orientation:
			file_name = f"{orientation.name}.png"
			file_path = os.path.join(base_path, file_name)
			sprites[orientation] = pygame.image.load(file_path)
		return sprites
		
	def getHullSprite(self, orientation):
		return self.hull_sprites.get(orientation)

	def getTurretSprite(self, orientation):
		return self.turret_sprites.get(orientation)
