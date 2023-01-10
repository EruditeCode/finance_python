# A program to generate alerts when stocks trade at set prices.

# Video Walkthrough Link: https://www.youtube.com/watch?v=_lWvwTvJnNU

import pygame
from sys import exit
from class_StockAlert import StockAlert

def main():
	pygame.init()
	WIDTH, HEIGHT = 400, 600
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Stock Alert Tester")
	clock = pygame.time.Clock()

	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20,20,20))

	def draw_text(text, size, x, y, color):
		font = pygame.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.left = x
		text_rect.top = y
		screen.blit(text_surface, text_rect)

	# Create the stock alert objects.
	stocks = {
		"GOOGL":["Alphabet Ltd.", 88.00],
		"AAPL":["Apple Inc.", 125.00],
		"TSLA":["Tesla Inc.", 100.00],
		"MSFT":["Microsoft Corp.", 200.00]
	}
	alerts = []
	for key in stocks.keys():
		alerts.append(StockAlert(key, stocks[key][0], stocks[key][1]))

	counter = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# DISPLAY OBJECTS
		screen.blit(bg, (0,0))
		y = 40
		for alert in alerts:
			if alert.status:
				color = (0,255,0)
			else:
				color = (100,100,100)
			pygame.draw.circle(screen, color, (50, y), 10)
			string = f"{alert.name}  Alert Price: {alert.alert_price}."
			draw_text(string, 20, 70, y-5, (255,255,255))
			y += 35

		# UPDATE OBJECTS
		if counter >= 300:
			for alert in alerts:
				alert.update()
			counter = 0
		else:
			counter += 1

		pygame.display.update()
		clock.tick(1)


if __name__ == "__main__":
	main()
