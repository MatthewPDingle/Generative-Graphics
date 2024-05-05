import pygame
import sys

# Constants
WINDOW_TITLE = "Generative Graphics"
WORLD_WIDTH, WORLD_HEIGHT = 10000, 10000  # World resolution
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800  # Initial screen resolution
FPS = 120  # Target frames per second
CHARACTER_SPEED = 5  # Speed in world coordinates

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

# Load assets
tile_background = pygame.image.load('assets/BackgroundGrid.png')  # Load the background image
world_character = pygame.image.load('assets/CharacterGrid.png')  # Load the character image
world_character = pygame.transform.scale(world_character, (50, 50))  # Adjust size to world coordinates

# Helper functions
def draw_tiled_background(screen, tile_background, camera_x, camera_y):
    tile_width, tile_height = tile_background.get_size()
    start_x = camera_x % tile_width
    start_y = camera_y % tile_height
    for x in range(-start_x, screen.get_width() + tile_width, tile_width):
        for y in range(-start_y, screen.get_height() + tile_height, tile_height):
            screen.blit(tile_background, (x, y))

def gameplay(screen, camera_x, camera_y):
    screen.fill((0, 0, 0))  # Clear screen with black (or any other background color)
    draw_tiled_background(screen, tile_background, camera_x, camera_y)  # Draw tiled background
    # Draw character in the center of the screen
    screen.blit(world_character, (screen.get_width() // 2 - world_character.get_width() // 2,
                                  screen.get_height() // 2 - world_character.get_height() // 2))

# Main game loop
running = True  # Initialize the running variable
camera_x, camera_y = WORLD_WIDTH // 2, WORLD_HEIGHT // 2  # Start camera in the center of the world
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # Movement logic (move the camera, keep character centered)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_x = max(0, camera_x - CHARACTER_SPEED)
    if keys[pygame.K_RIGHT]:
        camera_x = min(WORLD_WIDTH - screen.get_width(), camera_x + CHARACTER_SPEED)
    if keys[pygame.K_UP]:
        camera_y = max(0, camera_y - CHARACTER_SPEED)
    if keys[pygame.K_DOWN]:
        camera_y = min(WORLD_HEIGHT - screen.get_height(), camera_y + CHARACTER_SPEED)

    gameplay(screen, camera_x, camera_y)  # Render everything based on the new camera position

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
