import pygame

size = (600,400)

class nextcostume(pygame.sprite.Sprite):
  def __init__(self):
    super(nextcostume,self).__init__()

    self.images =[]
    self.images.append(pygame.image.load('img/walk1.png'))
    self.images.append(pygame.image.load('img/walk2.png'))
    self.images.append(pygame.image.load('img/walk3.png'))
    self.images.append(pygame.image.load('img/walk4.png'))
    self.images.append(pygame.image.load('img/walk5.png'))
    self.images.append(pygame.image.load('img/walk6.png'))
    self.images.append(pygame.image.load('img/walk7.png'))
    self.images.append(pygame.image.load('img/walk8.png'))
    self.images.append(pygame.image.load('img/walk9.png'))
    self.images.append(pygame.image.load('img/walk10.png'))

    self.index = 0
    self.image = self.images[self.index]
    self.rect = pygame.Rect(5,5,150,198)

  def update(self):
    self.index += 1
    if self.index >=  len(self.images):
      self.index = 0
    self.image = self.images[self.index]
    

# -------- Main loop -----------------
pygame.init()
screen = pygame.display.set_mode(size)

my_sprite = nextcostume()
my_group = pygame.sprite.Group(my_sprite)
clock =  pygame.time.Clock()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit() # insure to close the window, same as sys.exit()
  
  my_group.update()
  screen.fill((0,0,0))  # out of the loop will occur many overlap
  my_group.draw(screen) # can't work without this sentence on PC

  pygame.display.update()
  clock.tick(10)



