# A program to generate alerts when stocks trade at set prices.

import pygame
from sys import exit

def main():
	pygame.init()
	WIDTH, HEIGHT = 400, 600
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Stock Alert Tester")
	clock = pygame.time.Clock()

	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20,20,20))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# DISPLAY OBJECTS
		screen.blit(bg, (0, 0))


		# UPDATE OBJECTS

		pygame.display.update()
		clock.tick(1)


if __name__ == "__main__":
	main()
