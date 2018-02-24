import pygame
import time
def input(events): 
	for event in events:
		if event.type == QUIT:
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()


pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE=(117, 239, 217)
PINK=(255, 127, 229)

N_COUNTDOWN = 5
FONTSIZE = 960 

pygame.display.init()
size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)


screen.fill(BLACK)        
pygame.display.update()



font = pygame.font.SysFont("DKCosmoStitch", FONTSIZE)

text_color = TURQUOISE

led_state = False

for i in range(N_COUNTDOWN):
	screen.fill(BLACK)
	text = font.render(str(N_COUNTDOWN - i), 1, text_color)
	textpos = text.get_rect()
	textpos.center = (pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)
	screen.blit(text, textpos)
	pygame.display.flip()
	if i < N_COUNTDOWN - 2:
		time.sleep(1)
	else:
		for j in range(5):
			time.sleep(.2)

