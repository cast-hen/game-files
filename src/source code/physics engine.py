import pygame
from pygame import RESIZABLE

pygame.init()

#global variables
WIDTH = 1366
HEIGHT = 690
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
clock = pygame.time.Clock()
fps = 60
gravity = 0.6
jump_height = -25
speed = 10
running = True

#texturestest
texture = pygame.image.load(r"C:\Users\12880\OneDrive - Atheneum College Hageveld\2024-2025\infomatica\game files\game assets\images\texturetest.png")
player_texture = pygame.image.load(r"C:\Users\12880\OneDrive - Atheneum College Hageveld\2024-2025\infomatica\game files\game assets\images\BozeJantje.png")

#objecten class
class Objects:
    def __init__(self, xpos, ypos, width, height, color, mass, xspeed, yspeed):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.mass = mass
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.Rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.on_ground = False

    def update_pos(self, platforms):
        self.xpos += self.xspeed
        self.Rect.topleft = (self.xpos, self.ypos)


        for platform in platforms:
            if self.Rect.colliderect(platform.Rect):
                if self.xspeed > 0:
                    self.xpos = platform.xpos - self.width
                elif self.xspeed < 0:
                    self.xpos = platform.xpos + platform.width
                self.xspeed = 0
                self.Rect.topleft = (self.xpos, self.ypos)


        self.yspeed += self.mass * gravity


        self.ypos += self.yspeed
        self.Rect.topleft = (self.xpos, self.ypos)
        self.on_ground = False

        #platformcollision
        for platform in platforms:
            if self.Rect.colliderect(platform.Rect):
                if self.yspeed > 0:  # Falling
                    self.ypos = platform.ypos - self.height
                    self.yspeed = 0
                    self.on_ground = True
                elif self.yspeed < 0:  # Hitting ceiling
                    self.ypos = platform.ypos + platform.height
                    self.yspeed = 0
                self.Rect.topleft = (self.xpos, self.ypos)

        #wall en floor collision
        if self.ypos + self.height >= HEIGHT - 4:
            self.ypos = HEIGHT - self.height - 4
            self.yspeed = 0
            self.on_ground = True
            self.Rect.topleft = (self.xpos, self.ypos)
        if self.xpos < 0:
            self.xpos = 0
        elif self.xpos + self.width > WIDTH:
            self.xpos = WIDTH - self.width
        self.Rect.topleft = (self.xpos, self.ypos)

    def draw(self, surface):
        self.Rect = pygame.draw.rect(surface, self.color, (self.xpos, self.ypos, self.width, self.height))

#maakt vloer
def draw_floor():
    pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WIDTH, HEIGHT), 10)

#objects
player = Objects(300, 650, 50, 50, 'green', 2, 0, 0)
cube1 = Objects(580, 500, 60, 60, 'black', 1, 0, 0)
cube2 = Objects(690, 646, 600, 40, 'black', 1, 0, 0)
cube3 = Objects(0, 400, 400, 60, 'black', 1, 0, 0)
cube4 = Objects(600, 200, 80, 80, 'orange', 1, 0, 0)

#voeg hier nieuwe platformen to zodat ze collision krijgen.
platforms = [cube1, cube2, cube3, cube4]

#texturecropping
texture1 = texture.subsurface(pygame.Rect(0, 0, cube4.width, cube4.height))
texture2 = texture.subsurface(pygame.Rect(0, 0, cube3.width, cube3.height))
texture3 = texture.subsurface(pygame.Rect(0, 0, cube1.width, cube1.height))
texture4 = texture.subsurface(pygame.Rect(0, 0, cube2.width, cube2.height))

#random ahhh movement fix, couldn't bother om een betere oplossing te vinden.
keys = {"left": False, "right": False}

#game loop
while running:
    clock.tick(fps)
    screen.fill((135, 206, 250))
    draw_floor()
    player.update_pos(platforms)
    player.draw(screen)
    cube1.draw(screen)
    cube2.draw(screen)
    cube3.draw(screen)
    cube4.draw(screen)
    screen.blit(texture1, cube4.Rect.topleft)
    screen.blit(texture2, cube3.Rect.topleft)
    screen.blit(texture3, cube1.Rect.topleft)
    screen.blit(texture4, cube2.Rect.topleft)
    player.xspeed = speed * (keys["right"] - keys["left"])

#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                keys["right"] = True
            elif event.key == pygame.K_a:
                keys["left"] = True
            elif event.key == pygame.K_w and player.on_ground:
                player.yspeed = jump_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keys["right"] = False
            elif event.key == pygame.K_a:
                keys["left"] = False

    pygame.display.flip()

pygame.quit()