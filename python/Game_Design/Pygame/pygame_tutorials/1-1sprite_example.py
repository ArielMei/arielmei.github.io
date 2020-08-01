import pygame

WIDTH =  800
HEIGHT = 600
FPS = 30
# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50,50)) # create a plain rectangle for sprite image
		self.image.fill(GREEN)
		self.rect = self.image.get_rect() # get the rectangle and store them
		self.rect.center = (WIDTH/2, HEIGHT/2)

	def update(self):
		self.rect.x += 5
		if self.rect.left > WIDTH:
			self.rect.right = 0
# initialize pygame and create windown
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Sprite Example')
clock =  pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# ---  Game loop -------
running = True
while running:
	clock.tick(FPS) # keep loop running at the right speed
	# get input event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Update sprites
	all_sprites.update()
	# render sprite and screen
	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()



