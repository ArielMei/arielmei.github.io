#import pygame
#import time
#
#pygame.init()
#SIDE = 600
#screen = pygame.display.set_mode((SIDE,SIDE))
#clock = pygame.time.Clock()
#
## ---------- Game Over message -----------
#font = pygame.font.SysFont('comicsansms',72)
#text = font.render('Game Over!',True,(0,128,0))
## --------------- Main loop --------------------
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running =  False
#
#    screen.fill((135,206,250))
#    screen.blit(text,((SIDE-text.get_width())/2,(SIDE-text.get_height())/2))
#
#    pygame.display.flip()
#    clock.tick(60)

# ----------------- Improved code ---------------
# Storing an image is cheaper than rendering a new one, especially if you plan on having the same text show up for more than one consecutive frame.
import pygame

def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
    
_cached_fonts = {}
def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

_cached_text = {}
def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]

text = create_text("Hello, World", font_preferences, 72, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)
