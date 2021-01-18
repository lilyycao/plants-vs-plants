'''
Programmed by: Fiona Hila
Programmed on: May 11, 19
Programmed for: ICS3U1-04

Purpose: the outro of the game "Plants vs Plants"
'''

#display game over screen, ask user if they want to play again

import pygame
from pygame.locals import *
pygame.init()

def continueGame():
    screen = pygame.display.set_mode((1000, 500))
    screen.fill((0,0,0))
    pygame.display.set_caption("Click on Your Choice")

    exitGame = pygame.Surface((300, 100)).convert()
    exitGame.fill((0,255,0))
    screen.blit(exitGame, (630, 270))

    descFont = pygame.font.SysFont("plantagenetcherokee", 45)
    exitLabel = descFont.render("EXIT", True, (0,0,0))
    screen.blit(exitLabel, (740, 300))

    playAgain = pygame.Surface((300, 100)).convert()
    playAgain.fill((0,255,0))
    screen.blit(playAgain, (120, 270))

    playLabel = descFont.render("PLAY AGAIN", True, (0,0,0))
    screen.blit(playLabel, (170, 300))

    pygame.display.flip()

    keep_going = True
    clock = pygame.time.Clock()
    while keep_going:
        clock.tick(30)
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
            elif ev.type == MOUSEBUTTONDOWN:
                x = ev.pos[0]
                y = ev.pos[1]
                if x > 120 and x < 420 and y > 270 and y < 370:
                    return True
                elif 630 < x < 930 and 270 < y < 370:
                    quit()
                    keep_going = False
                    return False
