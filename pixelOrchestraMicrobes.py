import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Time
start_time = time.time()

# Constants for the flow field
# Defaults: 
# flow_field_intensity = 0.1
# flow_field_scale = 0.005
flow_field_intensity = 1
flow_field_scale = 0.05

# Define a Particle class
class Particle:
    def __init__(self):
        self.x = random.randrange(0, width)
        self.y = random.randrange(0, height)
        self.size = random.randint(1, 4)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.velocity = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]

    def update(self, dt):
        # Change in flow field over time
        time_factor = math.sin(dt)

        # Apply flow field based on position and time
        angle = (math.sin(self.y * flow_field_scale) + math.sin(self.x * flow_field_scale * time_factor)) * \
                (math.cos(self.x * flow_field_scale) + math.cos(self.y * flow_field_scale * time_factor))

        # Adjust velocity
        self.velocity[0] += math.cos(angle) * flow_field_intensity
        self.velocity[1] += math.sin(angle) * flow_field_intensity

        # Limit velocity to avoid too fast movement
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        max_speed = 2
        if speed > max_speed:
            self.velocity[0] = self.velocity[0] / speed * max_speed
            self.velocity[1] = self.velocity[1] / speed * max_speed

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
particles = [Particle() for _ in range(5000)]

# Main loop
running = True
while running:
    dt = time.time() - start_time  # Time since start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw particles
    screen.fill((0, 0, 0))  # Clear screen
    for particle in particles:
        particle.update(dt)
        particle.draw(screen)
    
    pygame.display.flip()  # Update the display

pygame.quit()
