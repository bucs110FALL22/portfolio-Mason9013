import pygame 
pygame.init()

window = pygame.display.set_mode((400,400))
window.fill("blue")
surface = pygame.display.get_surface()

print(pygame.display.get_window_size())

pygame.draw.circle(surface, "red", (200,200), 100)
pygame.display.flip

