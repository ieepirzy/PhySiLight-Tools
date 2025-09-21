import pygame
import math
import random
import numpy as np

gamma = 6.6743*10**(-11)
dt = 0.01

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

class Body:
    def __init__(self,mass,velocity,position,radius):
        
        self.pos = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.radius = radius

        self.force = np.zeros(2)

    def UpdateForce(self, other_bodies,gamma):
        self.force = np.zeros(2)

        for other in other_bodies:
            if other is self:
                continue
        r_vec = other.pos - self.pos
        self.force = gamma*(self.mass*other.mass)/(r_vec**2) #Force calculated with newtons law of universal gravitation

    def Update(self,dt):
        acc = self.force/self.mass #F=ma
        self.velocity += acc*dt #From the ODE for motion v' = a*dt
        self.position += self.velocity*dt #From the ODE for motion x' = v*dt