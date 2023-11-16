import pygame
import random
import math

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Constants for the flow field
flow_field_intensity = 0.005
flow_field_scale = 0.01

# Define a Particle class
class Particle:
    def __init__(self):
        self.x = random.randrange(0, width)
        self.y = random.randrange(0, height)
        self.size = random.randint(1, 4)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]

    def update(self):
        # Apply flow field based on position
        angle = math.sin(self.y * flow_field_scale) * math.cos(self.x * flow_field_scale)
        self.velocity[0] += math.cos(angle) * flow_field_intensity
        self.velocity[1] += math.sin(angle) * flow_field_intensity

        # Update position
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Reappear on the opposite side if it goes off-screen
        if self.x < 0: self.x = width
        if self.x > width: self.x = 0
        if self.y < 0: self.y = height
        if self.y > height: self.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Create a list of particles
particles = [Particle() for _ in range(100)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw particles
    screen.fill((0, 0, 0))  # Clear screen
    for particle in particles:
        particle.update()
        particle.draw(screen)
    
    pygame.display.flip()  # Update the display

pygame.quit()
