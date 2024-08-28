import pygame
import sys 
import random

pygame.init()

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

image = sys.argv[1]
img = pygame.image.load(image)
(w,h) = img.get_size()
a = pygame.display.set_mode((w*5, h*5))
a.blit(img, (0,0))

for y in range(h):
    for x in range(w):
        (r,g,b,_) = img.get_at((x,y))
        num_r = int(r//10)
        num_b = int(g//10)
        num_g = int(b//10)
        while (num_r > 0):
            pygame.draw.circle(a, r,(random.randint((w*5)-20, 5*w), (random.randint((h*5)-20, 5*h))), 1)
            num_r = num_r - 1

        while (num_g > 0):
            pygame.draw.circle(a, g,(random.randint((w*5)-20, 5*w), (random.randint((h*5)-20, 5*h))), 1)
            num_g = num_g - 1

        while (num_b > 0):
            pygame.draw.circle(a, b,(random.randint((w*5)-20, 5*w), (random.randint((h*5)-20, 5*h))), 1)
            num_b = num_b - 1
        
        
    pygame.display.update()
    pygame.time.delay(100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            exit()  
    
