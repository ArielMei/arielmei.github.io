import pygame
 
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 100, 100), 10)
        pygame.draw.circle(screen, (0, 128, 255), (200, 60), 50, 10)
        pygame.draw.line(screen, (255, 128, 255), (30, 30), (150, 150), 4)
        
        pygame.display.flip()


#pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height),hickness)
#pygame.draw.circle(surface, color, (x, y), radius,hickness)
#pygame.draw.line(surface, color, (startX, startY), (endX, endY), width)

