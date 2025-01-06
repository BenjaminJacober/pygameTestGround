from math import atan2, degrees, sqrt
from TankSprite import TankSprite, Orientation

class Tank:
	sprite = TankSprite()
	pos = (50, 50)
	speed = 4
	orientation = Orientation.UP
	turretOrientation = Orientation.UP
	
	def update(self, orientation, posToAimAt):
		if orientation is not None:
			self.orientation = orientation
			self.move()
		if posToAimAt is not None:
			self.turretOrientation = self.calculateTurretOrientation(posToAimAt)
	
	def calculateTurretOrientation(self, posToAimAt):
		xCenter = self.pos[0] + self.sprite.width / 2
		yCenter = self.pos[1] + self.sprite.height / 2
		dx = xCenter - posToAimAt[0]
		dy = yCenter - posToAimAt[1]
		angle = degrees(atan2(dy, dx))
		sector = int((angle + 22.5) // 45) % 8
		return Orientation(sector)
	
	def draw(self):
		return [self.sprite.getHullSprite(self.orientation), self.sprite.getTurretSprite(self.turretOrientation)]
	
	def move(self):
		movement_vectors = {
			Orientation.LEFT: (-1, 0),
			Orientation.LEFT_DOWN: (-1, 1),
			Orientation.DOWN: (0, 1),
			Orientation.RIGHT_DOWN: (1, 1),
			Orientation.RIGHT: (1, 0),
			Orientation.RIGHT_UP: (1, -1),
			Orientation.UP: (0, -1),
			Orientation.LEFT_UP: (-1, -1),
		}
		
		dx, dy = movement_vectors.get(self.orientation)
				
		if dx != 0 and dy != 0:
			normalization_factor = sqrt(2)
			dx /= normalization_factor
			dy /= normalization_factor

		dx *= self.speed
		dy *= self.speed

		self.pos = (self.pos[0] + dx, self.pos[1] + dy)