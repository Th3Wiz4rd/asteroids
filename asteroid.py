from constants import *
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):



	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)


	def draw(self, screen):
		pygame.draw.circle(screen, pygame.Color("white"), (int(self.position.x), int(self.position.y)), self.radius, 2)


	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		random_angle = random.uniform(20, 50)

		a = self.velocity.rotate(random_angle)
		b = self.velocity.rotate(-random_angle)

		new_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid1.velocity = a * 1.2
		asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid2.velocity = b * 1.2

		for group in self.groups():
			group.add(asteroid1)
			group.add(asteroid2)
			

