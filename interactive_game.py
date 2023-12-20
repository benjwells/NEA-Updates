import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width, screen_height = 1920, 1080
background_image_path = "images/InGameScreen.png"
background = pygame.image.load(background_image_path)
background = pygame.transform.scale(background, (screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Interactive Game")

# Define the projectile's properties
projectile_pos = [screen_width // 2, screen_height // 2]  # Starting position of the projectile
projectile_radius = 10  # Radius of the projectile
projectile_color = pygame.Color('black')  # Color of the projectile

box_color = pygame.Color('white')
box_width, box_height = 200, 40  # Adjust these values as needed
box_spacing = 10  # Margin between the input boxes

input_boxes = [
    pygame.Rect(10, 10, box_width, box_height), 
    pygame.Rect(10, 10 + box_height + box_spacing, box_width, box_height),
    pygame.Rect(10 + box_width + box_spacing, 10, box_width, box_height),
    pygame.Rect(10 + box_width + box_spacing, 10 + box_height + box_spacing, 
    box_width, box_height)  
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen and draw the background
    screen.blit(background, (0, 0))

    for box in input_boxes:
        pygame.draw.rect(screen, input_box_color, box)

    # Draw the projectile
    pygame.draw.circle(screen, projectile_color, projectile_pos, projectile_radius)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
