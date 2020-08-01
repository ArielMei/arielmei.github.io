



#Imports
import pygame,sys,random,math
from pygame.locals import *

#Inits
pygame.init()

#A clock object for keeping track of fps
clock = pygame.time.Clock()

#The font used on the panel. 18 pixels high
font = pygame.font.Font("freesansbold.ttf",18)
TEXTCOLOR = (255,255,255)

#Set up the screen
screen = pygame.display.set_mode((1024,640))
pygame.display.set_caption("FWSIM Clone")

#List[s] of colors
COLORS = [[255,255,255], #White
          [255,64,0],    #Red
          [255,128,0],   #Orange
          [255,204,0],   #Yellow-orange
          [192,255,0],   #Yellow-green
          [64,255,0],    #Bright green
          [0,255,128],   #Sea green
          [0,255,255],   #Aqua
          [0,128,255],   #Turquoise
          [0,48,255],    #Bright blue
          [128,0,255],   #Indigo
          [255,0,255]]   #Magenta

REDWHITEBLUE = [[255,255,255], #White
                [255,64,0],    #Red
                [0,48,255]]    #Bright blue

#Random rgb color
def randcolor():
    return [random.randint(128,255),random.randint(0,255),random.randint(0,255)]

#Find in a list
def locate(item,listx):
    for i in range(0,len(listx)):
        if listx[i] == item:
            return i

#Parse the FWML

clock.tick()
        
fwml = open("Sample.fwml","r")

lines = fwml.readlines()

fwml.close()

colorpalette = lines[0]
if colorpalette == "SPECTRUM        \n":
    colorpalette = COLORS
elif colorpalette == "REDWHITEBLUE    \n":
    colorpalette = REDWHITEBLUE

ticks = []
for line in lines[1:]:
    ticks.append(int(line[0:4]))

timers = []
for line in lines[1:]:
    timers.append(int(line[5:8]))

locations = []
for line in lines[1:]:
    locations.append([int(line[9:13]),
                      int(line[14:18])])


sizes = []
for line in lines[1:]:
    sizes.append(int(line[19:22]))
    
angles = []
for line in lines[1:]:
    angles.append(int(line[23:26]))
    
colors = []
for line in lines[1:]:
    colors.append(int(line[27:30]))

densities = []
for line in lines[1:]:
    densities.append(int(line[31:34]))


#A firework    
class Firework(pygame.sprite.Sprite):

    #Init function
    def __init__(self,location,size,angle,color,timer,density):
        pygame.sprite.Sprite.__init__(self)
        
        self.location = location
        self.velocity = [math.sin(float(angle))*3,
                    -math.cos(float(angle))*3]
        self.size = size
        
        self.color = color
        self.image = pygame.surface.Surface((size,size))
        self.image.fill(color)
        
        self.angle = float(angle)

        self.ps = []

        self.timer = timer
        self.density = density

    def explode(self,exp):
        if exp == "NORMAL":
            for i in range(self.density):
                particle = Particle(self.location[:],[0,0.05],self.size,random.randint(0,360),self.color,random.randint(70,80))
                self.ps.append(particle)
              
    #Update and render
    def update(self):

        self.timer -= 1

        if self.ps:
            for p in self.ps:
                p.update()
            return

        if self.timer <= 0:
            self.explode("NORMAL")
            return

        if self.location[0] < 0 or self.location[0] > screen.get_width() or self.location[1] < 0 or self.location[1] > screen.get_height():
            return             

        self.location[0] += self.velocity[0]
        self.location[1] += self.velocity[1]
        
        screen.blit(self.image,self.location)

class Particle(pygame.sprite.Sprite):

    #Init function
    def __init__(self,location,acceleration,size,angle,color,death):
        pygame.sprite.Sprite.__init__(self)
         
        self.location = location
        self.velocity = [math.sin(float(angle))*3,
                    -math.cos(float(angle))*3]
        self.acceleration = acceleration
        self.size = size
        
        self.color = color
        self.image = pygame.surface.Surface((size,size))
        self.image.fill(color)
        
        self.angle = float(angle)
        self.life = 0
        self.death = death
 
    #Update and render
    def update(self):

        self.life += 1

        if self.life >= self.death:
            return

        if self.location[0] < 0 or self.location[0] > screen.get_width() or self.location[1] < 0 or self.location[1] > screen.get_height():
            return

        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

        self.location[0] += self.velocity[0]
        self.location[1] += self.velocity[1]
        
        screen.blit(self.image,self.location)

fireworks = []

phase = 0

loadtime = clock.tick()
print("Loading time: " + str(loadtime) + " Milliseconds")

while True:

    screen.fill((0,0,0))

    if phase in ticks:
        index = locate(phase,ticks)
        fw = Firework(locations[index],sizes[index],angles[index],colorpalette[colors[index]],timers[index],densities[index])
        fireworks.append(fw)

    for fw in fireworks:
        fw.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Render the             clock.get_fps()       2 digits                     antialiased
    screen.blit(font.render(str(round(clock.get_fps(),2))+" FPS",
                            1,
                            TEXTCOLOR),
                            (1,screen.get_height() - 20))

    pygame.display.update()
    
    phase += 1

    clock.tick(100)

    
