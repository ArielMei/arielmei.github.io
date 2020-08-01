import pygame,math
import sys

# ----------------- Prepare images -------------
blackboard = pygame.image.load('blackboardbackground.png')
sun = pygame.image.load('chalksun.png')
cloud = pygame.image.load('chalkcloud.png')
house =  pygame.image.load('chalkhouse.png')
flower = pygame.image.load('flower.png')
bee1 = pygame.image.load('honeybee1_small.png')
bee2 = pygame.image.load('honeybee2_small.png')

orgin = (0,0)
sun_pos = (20,20)
house_pos = (195,165)
flower_pos = (172,405)
# -----------------------------------------
pygame.init()
size=(640,480)
drawboard = pygame.display.set_mode(size)
clock = pygame.time.Clock()
cloud_x = 490
cloud_y = 30
d = 0

hx = 165
hy = 320

a = 70
butx = 100
buty = 380

honeyBeeSwitch = True
while True:
  drawboard.blit(blackboard,orgin)
  drawboard.blit(sun,sun_pos)
  drawboard.blit(house,house_pos)
  drawboard.blit(flower,flower_pos)
  drawboard.blit(cloud,(cloud_x,cloud_y))

  cloud_x = cloud_x - 1
  if cloud_x < 0:
    cloud_x = 500

  if honeyBeeSwitch == True:
    drawboard.blit(bee1,(butx,buty))
    honeyBeeSwitch = False
  else:
    drawboard.blit(bee2,(butx,buty))
    honeyBeeSwitch = True

  butx = a * math.cos(d*math.pi/180) + hx
  buty = a * math.cos(d*math.pi/180)* math.sin(d*math.pi/180) + hy
  d = d + 3
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit
      quit()
      # sys.exit()


  pygame.display.update()
  clock.tick(70)







