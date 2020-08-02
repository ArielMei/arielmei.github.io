# Learn to load image from designated path as your sprite
import pygame
import os

WIDTH = 800
HEIGHT = 600
FPS = 30


# set up assets folders
#game_folder = os.path.dirname(__file__) # current folder
game_folder = os.getcwd()          # get current path
img_folder = os.path.join(game_folder,'img')
print('game_folder is :',game_folder)
print('dir is :',img_folder)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder,'p1_jump.png')).convert()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2,HEIGHT/2)
		self.y_speed = 5

	def update(self):
		self.rect.x += 5
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 200:
			self.y_speed = -5
		if self.rect.top < 200:
			self.y_speed = 5
		if self.rect.left > WIDTH:
			self.rect.right = 0

# 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()
	screen.fill((129,135,128))
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()