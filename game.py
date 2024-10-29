import pygame
import sys

pygame.init()                         #initialize pygame
WIDTH = 1000 
HEIGHT = 1000
SPRITE_HEIGHT = 30  # Define the sprite height
SPRITE_WIDTH = 30   # Define the sprite width

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 820:
            self.pos.left = 0

def move(self, up=False, down=False, left=False, right=False):
  if right:
      self.pos.right += self.speed
  if left:
      self.pos.right -= self.speed
  if down:
      self.pos.top += self.speed
  if up:
      self.pos.top -= self.speed
  if self.pos.right > WIDTH:
      self.pos.left = 0
  if self.pos.top > HEIGHT-SPRITE_HEIGHT:
      self.pos.top = 0
  if self.pos.right < SPRITE_WIDTH:
      self.pos.right = WIDTH
  if self.pos.top < 0:
      self.pos.top = HEIGHT-SPRITE_HEIGHT

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('assets/player.png').convert()
entity = pygame.image.load('assets/alien.png').convert()
background = pygame.image.load('assets/background.jpg').convert()
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 10, 3)          #create the player object
for x in range(10):                    #create 10 objects</i>
    o = GameObject(entity, x*40, x)
    objects.append(o)
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(p.image, p.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)