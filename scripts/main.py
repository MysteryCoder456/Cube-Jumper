import uni_vars as uv
import pygame


class Game:
	def start(self):
		pass
	
	def logic(self):
		pass

	def render(self):
		pass































def main():
	game = Game()
	game.start()

	while uv.running:
		uv.clock.tick(uv.FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				uv.running = False

		game.logic()
		uv.win.fill(uv.background)
		game.render()
		pygame.display.update()


if __name__ == "__main__":
	main()
	quit()
