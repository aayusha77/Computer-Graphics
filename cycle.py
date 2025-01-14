import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bicycle Animation")

# Colors
LIGHT_GREY = (211, 211, 211)  #background
ROAD_GREY = (105, 105, 105)
WHEEL_BLACK = (0, 0, 0)
FRAME_RED = (255, 0, 0)  #frame
HANDLE_GREEN = (0, 128, 0)  #handlebar
SEAT_ORANGE = (255, 165, 0)  #seat

# Main function
def main():
    clock = pygame.time.Clock()
    x_offset = 0  

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(LIGHT_GREY)  # background

        # Draw road
        pygame.draw.rect(screen, ROAD_GREY, (0, 580, WIDTH, 140)) 

        # Draw wheels
        pygame.draw.circle(screen, WHEEL_BLACK, (150 + x_offset, 550), 50, 8)  
        pygame.draw.circle(screen, WHEEL_BLACK, (350 + x_offset, 550), 50, 8)  
        pygame.draw.circle(screen, WHEEL_BLACK, (250 + x_offset, 550), 25, 6)  

        # Draw bicycle frame (red)
        pygame.draw.line(screen, FRAME_RED, (250 + x_offset, 550), (180 + x_offset, 400), 6)  
        pygame.draw.line(screen, FRAME_RED, (150 + x_offset, 550), (250 + x_offset, 550), 6)  
        pygame.draw.line(screen, FRAME_RED, (350 + x_offset, 550), (300 + x_offset, 370), 6)  
        pygame.draw.line(screen, FRAME_RED, (300 + x_offset, 370), (150 + x_offset, 550), 6) 
        pygame.draw.line(screen, FRAME_RED, (250 + x_offset, 550), (320 + x_offset, 450), 6)  

        # seat
        pygame.draw.ellipse(screen, SEAT_ORANGE, (160 + x_offset, 390, 80, 15))  
         
        #handle

        pygame.draw.line(screen, HANDLE_GREEN, (300 + x_offset, 370), (350 + x_offset, 320), 6)  
        pygame.draw.line(screen, HANDLE_GREEN, (350 + x_offset, 320), (340 + x_offset, 330), 6)  
        pygame.draw.line(screen, HANDLE_GREEN, (300 + x_offset, 370), (260 + x_offset, 320), 6)  
        pygame.draw.line(screen, HANDLE_GREEN, (260 + x_offset, 320), (270 + x_offset, 330), 6)  

        # Update display
        pygame.display.flip()

        x_offset += 2
        if x_offset > WIDTH:
            x_offset = -400 

        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
