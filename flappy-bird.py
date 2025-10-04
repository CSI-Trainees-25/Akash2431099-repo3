import pygame
import random
import sys
import math

#Initialised pygame
pygame.init()
 
#Screen Dimensions
# WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

#Colors
WHITE = (255, 255, 255)
BLACK= (0,0, 0)
SKY_BLUE_TOP = (135, 206, 250)
SKY_BLUE_BOTTOM = (70, 130, 180)
GREEN = (60,180,75)
DARK_GREEN = (30,90,40)
BIRD_BODY = (255,200,0)
BIRD_BEEK = (255,140,0)
BIRD_EYE = (0,0,0)
GROUND_FLOOR = (139,69,19)

#Game Variables
FPS = 60
GRAVITY = 0.3
BIRD_JUMP_VELOCITY = -8
PIPE_SPEED = 3
PIPE_GAP = 180
PIPE_FREQUENCY = 1500

#Fonts
FONT = pygame.font.SysFont("Arial",32, bold=True)
SMALL_FONT = pygame.font.SysFont("Arial",18)

class Bird:
    def __init__(self):
        self.x=80
        self.y=HEIGHT//2
        self.velocity=0
        self.radius=15
        self.rotation=0
        self.flap.counter=0

    def flap(self):
        self.velocity=BIRD_JUMP_VELOCITY
        self.rotation=-30

    def update(self):
        self.velocity+=GRAVITY
        self.y+=self.velocity

