import uni_vars as uv
import pygame
from cube import Cube


class Game:
	def start(self):
		self.player = Cube(uv.width / 2, uv.height / 2, 60)

	def logic(self):
		keys = pygame.key.get_pressed()
		up = keys[pygame.K_UP]
		left = keys[pygame.K_LEFT]
		right = keys[pygame.K_RIGHT]

		jump_speed = 20
		move_speed = 2

		if self.player.y_vel == 0:
			is_jumping = False
		else:
			is_jumping = True

		if up:
			if not is_jumping:
				self.player.move(0, -jump_speed)
		
		if left:
			self.player.move(-move_speed, 0)

		if right:
			self.player.move(move_speed, 0)

		if self.player.x < 0:
			self.player.x_vel = 0
			self.player.x = 0
		if self.player.x + self.player.width > uv.width:
			self.player.x_vel = 0
			self.player.x = uv.width - self.player.width

		if self.player.y < 0:
			self.player.y_vel = 0
			self.player.y = 0
		if self.player.y + self.player.height > uv.height:
			self.player.y_vel = -uv.gravity
			self.player.y = uv.height - self.player.height

		self.player.update()

	def render(self):
		self.player.render()































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
