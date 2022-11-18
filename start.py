import pygame
import time


pygame.init()

back = [55, 255, 255]

screen = pygame.display.set_mode([800, 600], pygame.RESIZABLE)
pygame.display.set_caption("Test drawings")

clock = pygame.time.Clock()

font1 = pygame.font.Font(None, 56)
text = font1.render("Hello", True, (255, 0, 0))

# rect1 = pygame.Rect()

textX, textY = 0, 0

start_time = time.time()
cur_time = start_time

print(start_time)

GAME_STATE = True
while GAME_STATE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATE = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                textY += 1
            if event.key == pygame.K_f:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode([800, 600])
                else:
                    pygame.display.set_mode([800, 600], pygame.FULLSCREEN)
    screen.fill(back)
    screen.blit(text, (textX, textY))

    rect1 = pygame.draw.rect(screen, (0, 0, 255), (0, 0, 50, 150))

    textX += 0.1
    new_time = time.time()

    print(int(new_time-start_time))

    pygame.display.update()
    clock.tick(60)
    #print(clock.get_fps())

