# https://realpython.com/pygame-a-primer/#background-and-setup
# --------------------Part 1 Basic Pygame Program --------------------
#import pygame
#
## Initialize the pygame library
#pygame.init()
#
## set up the drawing window
#screen = pygame.display.set_mode([500,500])
#
## Run until the user asked to quit
#running = True
#while running:
#    # Did the user click the window close button?
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running =  False
#    # Fill the background with white
#    screen.fill((0,255,255))
#    # Draw circle.(0,0,255) is color;(250,250)is center;75 is radius
#    pygame.draw.circle(screen,(0,0,255),(250,250),75)
#    # update the contents of the display to the screen. Without this call, nothing appears in the window!
#    pygame.display.flip()
## Exit pygame
#pygame.quit()
# ---------------------------------------------------------------

# ------------Part 2 Pygame Getkey, Surface --------------
#import pygame
## Import pygame.locals for easier access to key coordinates
#from pygame.locals import(
#    K_UP,
#    K_DOWN,
#    K_LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    KEYDOWN,
#    QUIT,)
#
#pygame.init()
#
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600
#
#screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#screen.fill((135,206,250))
#
## Create a surface and pass in a tuple containing its length and width
#surf = pygame.Surface((50,50)) # 50 pixel by 50 pixel
#surf.fill((0,0,0))             # color of surface
#rect = surf.get_rect()         # access underlying rect & store as rect
#surf_center = ((SCREEN_WIDTH - surf.get_width())/2,(SCREEN_HEIGHT - surf.get_height())/2)
#
#
#running = True
#while running:
#    for event in pygame.event.get():
#        # Did the user hit a key?
#        if event.type == KEYDOWN:
#            # Was it the Escape key? If so, stop the loop
#            if event.key == K_ESCAPE:
#                running = False
#        # Did the user click the window close button? If so stop the loop
#        elif event.type == QUIT:
#            running = False
#    # Draw surface onto another Surface
#    # blit() used to draw one image onto another
#    # puts the top-left of surf at the location given
#    screen.blit(surf,surf_center)
#    pygame.display.flip()
#----------------------------------------------------------------

#----------------- Part 3 Sprites and Sprite input ------------------
# Sprite is a picture. Sprite Class desigend to hold one or several graphical representations of any game object.
# Define a Player object by extending pygame.sprite.Sprite
# pygame.event.get_pressed() can returns a dictionary containning all the current KEYDOWN events in the queue.
# Get the set of keys pressed and check for user input

#import pygame
#import time
#import random
#from pygame.locals import(
#    K_UP,
#    K_DOWN,
#    K_LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    KEYDOWN,
#    QUIT,)
#
#pygame.init()
#SIDE = 600
#screen = pygame.display.set_mode((SIDE,SIDE))
#screen.fill((0,0,0))
#clock = pygame.time.Clock()
## ------------ Player -----------
#class Player(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Player,self).__init__() # call the .__init__() method
#        self.surf = pygame.Surface((75,25)) # define and initialize .surf to hold the image
#        self.surf.fill((255,255,255)) # define the filling color
#        self.rect = self.surf.get_rect() # get and store rect
#
#    # Move the sprite based on user keypresses
#    # .move_ip() stands for move in place
#    def update(self,pressed_keys):
#        if pressed_keys[K_UP]:
#            self.rect.move_ip(0,-5)
#        if pressed_keys[K_DOWN]:
#            self.rect.move_ip(0,5)
#        if pressed_keys[K_LEFT]:
#            self.rect.move_ip(-5,0)
#        if pressed_keys[K_RIGHT]:
#            self.rect.move_ip(5,0)
#
#        # Keep playe on the screen
#        if self.rect.left < 0:
#            self.rect.left = 0
#        if self.rect.right > SIDE:
#            self.rect.right = SIDE
#        if self.rect.top <= 0:
#            self.rect.top = 0
#        if self.rect.bottom >= SIDE:
#            self.rect.bottom = SIDE
#
## ------------ Enemy -----------
#class Enemy(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Enemy,self).__init__()
#        self.surf = pygame.Surface((20,10))
#        self.surf.fill((255,255,255))
#        self.rect = self.surf.get_rect(
#            center = (random.randint(SIDE + 20, SIDE + 100),
#                      random.randint(0,SIDE),))
#        self.speed = random.randint(5,20) # define how fast the enemy moves
#
#    def update(self):
#        self.rect.move_ip(-self.speed,0)
#        if self.rect.right < 0:
#            self.kill()
#
##------------ Main loop ---------------
#player = Player()   # Create the player
#enemies = pygame.sprite.Group()    # Create groups to hold enemy sprites
#all_sprites = pygame.sprite.Group() # used for rendering
#all_sprites.add(player)
#
## Create a custom event for adding a new enemy
#ADDENEMY = pygame.USEREVENT + 1 # The last event pygame reserves is called USEREVENT
#pygame.time.set_timer(ADDENEMY,250) # Insert the new event into the event queue every 250 milliseconds
#
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running =  False
#
#        # Add a new enemy?
#        elif event.type == ADDENEMY:
#            new_enemy = Enemy()
#            enemies.add(new_enemy)
#            all_sprites.add(new_enemy)
#
#    # Get all the keys currently pressed
#    pressed_keys = pygame.key.get_pressed()
#    player.update(pressed_keys)    # Update the player sprite based on user keypresses
#    # Fill the screen with black
#    enemies.update()
#
#    screen.fill((0,0,0))
#    # Draw all sprites
#    for entity in all_sprites:
#        screen.blit(entity.surf,entity.rect)
#
#    # check if any enemies have collided with the player
#    # .spritecollideany() check "sprite collide any"
#    if pygame.sprite.spritecollideany(player,enemies):
#        player.kill() # remove it from every group to which it belongs
#        running = False
#
#    # Flip everything to the display
#    pygame.display.flip()
#    clock.tick(30)
#
#
#pygame.quit()
# ------------------- Part 4 Sprite Picture and Sound ------------------
#import pygame
#import time
#import random
#from pygame.locals import(
#    K_UP,
#    K_DOWN,
#    K_LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    KEYDOWN,
#    QUIT,)
#
#pygame.mixer.init()  # set up for sounds
#
#pygame.init()
#SIDE = 600
#screen = pygame.display.set_mode((SIDE,SIDE))
#screen.fill((135,206,250))
#clock = pygame.time.Clock()  # set up the clock for a decent framerate
## ------------ Player -----------
#class Player(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Player,self).__init__()
#        self.surf = pygame.image.load('jet.png').convert()
#        self.surf = pygame.transform.scale(self.surf, (50, 30))
#        self.surf.set_colorkey((0,0,0)) # remove bg color
#        self.rect = self.surf.get_rect()
#
#    # Move the sprite based on user keypresses
#    def update(self,pressed_keys):
#        if pressed_keys[K_UP]:
#            self.rect.move_ip(0,-5)
#        if pressed_keys[K_DOWN]:
#            self.rect.move_ip(0,5)
#        if pressed_keys[K_LEFT]:
#            self.rect.move_ip(-5,0)
#        if pressed_keys[K_RIGHT]:
#            self.rect.move_ip(5,0)
#
#
#        # Keep playe on the screen
#        if self.rect.left < 0:
#            self.rect.left = 0
#        if self.rect.right > SIDE:
#            self.rect.right = SIDE
#        if self.rect.top <= 0:
#            self.rect.top = 0
#        if self.rect.bottom >= SIDE:
#            self.rect.bottom = SIDE
#
## ------------ Enemy -----------
#class Enemy(pygame.sprite.Sprite):
#    def __init__(self):
#        super(Enemy,self).__init__()
#        self.surf = pygame.image.load('enemies.png').convert()
#        self.surf = pygame.transform.scale(self.surf,(20, 20))
#        self.surf.set_colorkey((0,0,0))
#        self.rect = self.surf.get_rect(
#            center = (random.randint(SIDE + 20, SIDE + 100),
#                      random.randint(0,SIDE),))
#        self.speed = random.randint(5,20) # define how fast the enemy moves
#
#    def update(self):
#        self.rect.move_ip(-self.speed,0)
#        if self.rect.right < 0:
#            self.kill()
#
##------------ Main ---------------
#player = Player()   # Create the player
#enemies = pygame.sprite.Group()    # Create groups to hold enemy sprites
#all_sprites = pygame.sprite.Group() # used for rendering
#all_sprites.add(player)
#
## Create a custom event for adding a new enemy
#ADDENEMY = pygame.USEREVENT + 1 # The last event pygame reserves is called USEREVENT
#pygame.time.set_timer(ADDENEMY,250) # Insert the new event into the event queue every 250 milliseconds
#
## Load background music
#pygame.mixer.music.load('bg.mp3')
#pygame.mixer.music.play(loops = -1)  # play the sound and never end
#
#die_sound = pygame.mixer.Sound('pop.wav')
## --------------- Main loop --------------------
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running =  False
#
#        # Add a new enemy?
#        elif event.type == ADDENEMY:
#            new_enemy = Enemy()
#            enemies.add(new_enemy)
#            all_sprites.add(new_enemy)
#
#    # Get all the keys currently pressed
#    pressed_keys = pygame.key.get_pressed()
#    player.update(pressed_keys)    # Update the player sprite based on user keypresses
#    # Fill the screen with black
#    enemies.update()
#
#    screen.fill((135,206,250))
#    # Draw all sprites
#    for entity in all_sprites:
#        screen.blit(entity.surf,entity.rect)
#
#    # check if any enemies have collided with the player
#    # .spritecollideany() check "sprite collide any"
#    if pygame.sprite.spritecollideany(player,enemies):
#        player.kill() # remove it from every group to which it belongs
#        die_sound.play()
#
#        running = False
#
#    # Flip everything to the display
#    pygame.display.flip()
#    clock.tick(30) # Ensure program maintains a rate of 30 frames per second
#
#pygame.mixer.music.stop() # stop and quit the mixer
#pygame.mixer.quit()
#pygame.quit()
# ----------------------- Part 5 Code Game Over Message --------------
import pygame
import time
import random
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,)

pygame.mixer.init()  # set up for sounds

pygame.init()
SIDE = 600
screen = pygame.display.set_mode((SIDE,SIDE))
screen.fill((135,206,250))
clock = pygame.time.Clock()  # set up the clock for a decent framerate
# ------------ Player -----------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.image.load('jet.png').convert()
        self.surf = pygame.transform.scale(self.surf, (50, 30))
        self.surf.set_colorkey((0,0,0)) # remove bg color
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on user keypresses
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)


        # Keep playe on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SIDE:
            self.rect.right = SIDE
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SIDE:
            self.rect.bottom = SIDE

# ------------ Enemy -----------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load('enemies.png').convert()
        self.surf = pygame.transform.scale(self.surf,(20, 20))
        self.surf.set_colorkey((0,0,0))
        self.rect = self.surf.get_rect(
            center = (random.randint(SIDE + 20, SIDE + 100),
                      random.randint(0,SIDE),))
        self.speed = random.randint(5,20) # define how fast the enemy moves
        
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
            
#------------ Main ---------------
player = Player()   # Create the player
enemies = pygame.sprite.Group()    # Create groups to hold enemy sprites
all_sprites = pygame.sprite.Group() # used for rendering
all_sprites.add(player)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1 # The last event pygame reserves is called USEREVENT
pygame.time.set_timer(ADDENEMY,250) # Insert the new event into the event queue every 250 milliseconds

# Load background music
pygame.mixer.music.load('bg.mp3')
pygame.mixer.music.play(loops = -1)  # play the sound and never end

die_sound = pygame.mixer.Sound('pop.wav')
# --------------- Main loop --------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
            
        # Add a new enemy?
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)    # Update the player sprite based on user keypresses
    # Fill the screen with black
    enemies.update()
    
    screen.fill((135,206,250))
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)
        
    # check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill() # remove it from every group to which it belongs
        die_sound.play()
        running = False
        
    # Flip everything to the display
    pygame.display.flip()
    clock.tick(30) # Ensure program maintains a rate of 30 frames per second
# ----------
pygame.mixer.music.stop() # stop and quit the mixer
pygame.mixer.quit()

# ---------- Game Over message -----------
font = pygame.font.SysFont('comicsansms',72)
text = font.render('Game Over!',True,(0,128,0))
done = False
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done =  True
    
        screen.fill((135,206,250))
        screen.blit(text,((SIDE-text.get_width())/2,(SIDE-text.get_height())/2))
    
        pygame.display.flip()
        clock.tick(30)
# --------------------------------------

pygame.quit()
