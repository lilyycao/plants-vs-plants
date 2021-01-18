'''
PLANTS VS PLANTS INTRODUCTION
Programmed by: Lily Cao
Programmed on: 2019/05/27
Programmed for: ICS3U1-04
Description: This is the introduction for the game PLANTS VS PLANTS. This code includes the origin story,
start page, and choose level page functions.
'''

#import all necessary modules
import pygame
import time
from pygame.locals import *
pygame.init()

#set the display screen size and caption
screen = pygame.display.set_mode((1000,500))
background = pygame.Surface((1000,500)).convert()
pygame.display.set_caption("PLANTS VS PLANTS")


#list of all fonts necessary for intro
#for origin story
font = pygame.font.SysFont("raavi", 30)
font2 = pygame.font.SysFont("raavi", 30)
font2.set_bold(True)
font3 = pygame.font.SysFont("raavi", 70)
font3.set_bold(True)

#for start pages
my_font = pygame.font.SysFont("plantagenetcherokee", 74)
my_font.set_bold(True)
my_font2 = pygame.font.SysFont("plantagenetcherokee", 20)

#sets the size of the start/choose level boxes
boxSize=(200, 100)

#set up music
pygame.mixer.music.load("main menu music.mp3")
pygame.mixer.music.set_volume(1) #adjust volume

'''
this function displays the origin story of the game
and returns once the story is complete
'''
def origin():
    
    #set background colour
    background.fill((0, 0, 0))
    #create origin story text
    text1 = font.render("A long time ago, before humans, before dinosaurs...", True, (255,255,255))
    text2 = font.render("there were plants.", True, (255,255,255))
    text3 = font.render("Dangerous plants, nice plants, boss plants...", True, (255,255,255))
    text4 = font.render("One fateful day, a plant decided to disrupt the balance and tranquility of nature...", True, (255,255,255))
    text5 = font2.render("and consume insects", True, (255,255,255))
    text6 = font.render("And so, the division between the autotrophs and the heterotrophs began.", True, (255,255,255))
    text7 = font.render("The tension between the two sides has been increasing", True, (255,255,255))
    text8 = font3.render("UNTIL NOW...", True, (255,255,255))

    #set variable for text movement
    moveUp=0
    #set pygame clock
    clock = pygame.time.Clock()
    keep_going = True


    #this loop keeps the game going
    while keep_going:
        clock.tick(30)
        moveUp+=2
        for ev in pygame.event.get():
            #if close button is pressed, the loop stops and the game is killed
            if ev.type == QUIT:
                keep_going = False
                #kills game (python function)
                quit()

        #if the last piece of text (y coordinate) is not centered on the page,
        #the text continues to move up each time it is blitted
        if (1200-moveUp > 250-(text8.get_height()/2)):
            screen.blit(background, (0,0))
            #x coordinate centers the text on the page
            #y coordinate spaces the text out and allows it to move up
            screen.blit(text1, ((1000-text1.get_width())/2, 500-moveUp))
            screen.blit(text2, ((1000-text2.get_width())/2, 550-moveUp))
            screen.blit(text3, ((1000-text3.get_width())/2, 600-moveUp))
            screen.blit(text4, ((1000-text4.get_width())/2, 650-moveUp))
            screen.blit(text5, ((1000-text5.get_width())/2, 730-moveUp))
            screen.blit(text6, ((1000-text6.get_width())/2, 900-moveUp))
            screen.blit(text7, ((1000-text7.get_width())/2, 950-moveUp))
            screen.blit(text8, ((1000-text8.get_width())/2, 1200-moveUp))
            pygame.display.flip()
        else:
            #pause screen at page for dramatic effect
            time.sleep(3)
            return



'''
this function displays the start page of the game
and returns once the user has clicked "start"
'''
def startPage():
    #loads and converts background image
    background = pygame.image.load("background.png")
    background = background.convert()

    #create a green box for start button
    greenBox = pygame.Surface(boxSize).convert()
    greenBox.fill((0,255,0))

    #create title and start label
    title = my_font.render("PLANTS VS PLANTS", True, (40,200,235))
    start = my_font2.render("START", True, (50,50,50))

    #blit the display (the text is centered vertically)
    #only needs to be blitted once as nothing changes
    screen.blit(background, (0,0))
    screen.blit(greenBox, (400, 300-(greenBox.get_height()/2)))
    screen.blit(title, ((1000-title.get_width())/2, 80))
    screen.blit(start, ((1000-start.get_width())/2,300-(start.get_height()/2)))
    pygame.display.flip()

    #play music
    pygame.mixer.music.play(-1)
    
    #pygame clock
    clock = pygame.time.Clock()
    keep_going = True

    #loop keeps game going
    while keep_going:
        clock.tick(30)
        for ev in pygame.event.get():
            #stops game
            if ev.type == QUIT:
                keep_going = False
                quit()

            #if the user click someplace on the screen, get the position
            elif ev.type == MOUSEBUTTONDOWN:
                x = ev.pos[0]
                y = ev.pos[1]
                #if the position is within the "start" box, exit function
                if x>=400 and x<=600 and y>=275 and y<=375:
                    return



'''
this function displays the "choose level" page of the game
and returns with a level number once the user has chosen a level
'''
def chooseLevel():
    #loads and converts background image
    background = pygame.image.load("background.png")
    background = background.convert()

    #create 2 green boxes for "choose level" button
    greenBox1 = pygame.Surface(boxSize).convert()
    greenBox1.fill((0,255,0))
    greenBox2 = pygame.Surface(boxSize).convert()
    greenBox2.fill((0,255,0))

    #create title and level labels
    title = my_font.render("PLANTS VS PLANTS", True, (40,200,235))
    level1 = my_font2.render("FIGHT THE BOSS", True, (50,50,50))
    level2a = my_font2.render("FIGHT YOUR", True, (50,50,50))
    level2b = my_font2.render("OWN KIND", True, (50,50,50))

    #blit the display (the text is centered vertically)
    #only needs to be blitted once as nothing changes
    screen.blit(background, (0,0))
    screen.blit(greenBox1, (200,300-(greenBox1.get_height()/2)))
    screen.blit(greenBox2, (600,300-(greenBox2.get_height()/2)))
    screen.blit(title, ((1000-title.get_width())/2, 80))
    screen.blit(level1, (300-(level1.get_width()/2),300-(level1.get_height()/2)))
    screen.blit(level2a, (700-(level2a.get_width()/2),285-(level2a.get_height()/2)))
    screen.blit(level2b, (700-(level2b.get_width()/2),315-(level2b.get_height()/2)))
    pygame.display.flip()

    #set up pygame clock
    clock = pygame.time.Clock()
    keep_going = True

    #keeps loop going
    while keep_going:
        clock.tick(30)
        for ev in pygame.event.get():
            #stops game
            if ev.type == QUIT: 
                keep_going = False
                quit()
            #if user click on screen, find position                
            elif ev.type == MOUSEBUTTONDOWN:
                x = ev.pos[0]
                y = ev.pos[1]
                #user clicks box 1 (single player)
                if x>=200 and x<=400 and y>=250 and y<=350:
                    return 1
                #user click box 2 (multiplayer)
                elif x>=600 and x<=800 and y>=250 and y<=350:
                    return 2
