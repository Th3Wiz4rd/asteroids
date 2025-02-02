import pygame

from constants import *

from player import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)

def main():
	pygame.init()
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		updatable.update(dt)
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()


