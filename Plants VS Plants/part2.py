'''
Programmed by: Fiona Hila
Programmed on: May 16, 19
Programmed for: ICS3U1-04

Purpose: option two of plants vs plants, two-player option
'''

import pygame
from pygame.locals import *
pygame.init()

def rules():
    print ("\n          HOW TO FIGHT!")
    print ("1. Player one uses 1 to defend, 2 to attack")
    print ("   Player two uses the left arrow to attack, the right arrow to defend")
    print ("2. You may select the same character")
    print ("3. To pause the game press the space bar, there you can see the rules, quit the game, or continue playing")

rules()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Plants vs Plants - Fight Your Own Kind!")

forest_bg = pygame.image.load("background.png")
forest_bg = forest_bg.convert()
screen.blit(forest_bg, (0,0))

pygame.mixer.music.load("background fighting music.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1) #repeats the song

##CHARACTER SELECTION SCREEN
def charSelect():
    global player1
    global player2
    
    #can turn into array
    whiteScreen = pygame.Surface((1025 * 0.75, 600 * 0.75))
    whiteScreen.fill((255,255,255,50)) #making it translucent
    width = 1025 * 0.10
    height = 600 * 0.15
    screen.blit(whiteScreen, (width, height))

    descFont = pygame.font.SysFont("comicsansms", 10)

    #CHARACTERS
    #Print the Grass char
    grassImage = pygame.image.load("grass.png")
    #grassImage = grassImage.convert() ##CHECK IF NEED A RECT
    grassImage.convert()
    grassName = descFont.render("Grass", True, (0,0,255))
    grassDesc = descFont.render("Attack: vines", True, (255,0,0))
    grassDesc2 = descFont.render("Defend: forcefield", True, (255,0,0)) #give them all defences
    screen.blit(grassImage, (width + 25, height + 140))
    screen.blit(grassName, (width + 25, height + 190))
    screen.blit(grassDesc, (width + 10, height + 210))
    screen.blit(grassDesc2, (width + 10, height + 230))

    #Print the Amanita Muscaria char
    mushroomImage = pygame.image.load("amanita muscaria.png")
    mushroomImage.convert()
    mushName = descFont.render("Amanita Muscaria", True, (0,0,255))
    mushDesc = descFont.render("Attack: spores", True, (255,0,0))
    muscDesc2 = descFont.render("Defend: forcefield", True, (255,0,0))
    screen.blit(mushroomImage, (width + 80, height + 15))
    screen.blit(mushName, (width + 110, height + 190))
    screen.blit(mushDesc, (width + 110, height + 210))
    screen.blit(muscDesc2 , (width + 110, height + 230))

    #Print the Bleeding Tooth Fungus char
    bleedingToothImage = pygame.image.load("bleeding tooth fungus.png")
    bleedingToothImage.convert()
    toothName = descFont.render("Bleeding Tooth Fungus", True, (0,0,255))
    toothDesc = descFont.render("Attack: blood", True, (255,0,0))
    toothDesc2 = descFont.render("Defend: forcefield", True, (255,0,0))
    screen.blit(bleedingToothImage, (width + 250, height + 15))
    screen.blit(toothName, (width + 270, height + 190))
    screen.blit(toothDesc, (width + 270, height + 210))
    screen.blit (toothDesc2, (width + 270, height + 230))

    #Print the Hydnora char
    hydnoraImage = pygame.image.load("hydnora.png")
    hydnoraImage.convert()
    hydName = descFont.render("Hydnora", True, (0,0,255))
    hydDesc = descFont.render("Attack: beetles", True, (255,0,0))
    hydDesc2 = descFont.render("Defend: forcefield", True, (255,0,0))
    screen.blit(hydnoraImage, (width + 420, height + 15))
    screen.blit(hydName, (width + 440, height + 190))
    screen.blit(hydDesc, (width + 440, height + 210))
    screen.blit(hydDesc2, (width + 440, height + 230))

    #Print the Saguaro char
    saguaroImage = pygame.image.load("saguaro.png")
    saguaroImage.convert()
    sagName = descFont.render("Saguaro", True, (0,0,255))
    sagDesc = descFont.render("Attack: cactus needles", True, (255,0,0))
    sagDesc2 = descFont.render("Defend: forcefield", True, (255,0,0))
    screen.blit(saguaroImage, (width + 590, height + 15))
    screen.blit(sagName, (width + 600, height + 190))
    screen.blit(sagDesc , (width + 600, height + 210))
    screen.blit(sagDesc2, (width + 600, height + 230))

    #Title - "Choose Your Fighter"
    titleFont = pygame.font.SysFont("comicsansms", 48) #change to more epic font
    title = titleFont.render("Choose Your Fighter", True, (255,0,0)) #change colour
    screen.blit(title, (width, height - 80))
    pygame.display.flip()
    
    player1_choose = descFont.render("Character One", True, (0,0,255))
    player2_choose = descFont.render("Character Two", True, (0,0,255))

    print ("\nFIGHER MENU\nEnter the number of the fighter you choose, the numbers are..")
    print ("\n1. Grass\n2. Amanita Muscaria\n3. Bleeding Tooth Fungus\n4. Hydnora\n5. Saguaro")
    
    #screen.blit(forest_bg, (0,0))
            
charSelect()
screen.blit(forest_bg, (0,0))

characters = ["grass.png", "amanita muscaria.png", "bleeding tooth fungus.png", "hydnora.png", "saguaro.png"]
attacks = ["vine.png", "spore.png", "blood.png", "beetle.png", "cactus needle.png"]

class Attacks(pygame.sprite.Sprite):
    def __init__(self, image, location, speed): #attackpower
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.convert() #alpha convert
        self.rect = self.image.get_rect()

        self.rect.topleft = location
        self.dir_x = 1
        self.dir_y = 0
        self.speed = speed

        def update(self):
            self.rect.move_ip(self.dir_x * self.speed, self.dir_y * self.speed)

class notMoving(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.convert()
        self.rect = self.image.get_rect()

        self.rect.topleft = location

defend1 = notMoving("blue shield.png", (250, 400)) #check cors
defend2 = notMoving("red shield.png", (750, 400))

print ("PLAYER ONE")
charChoice = int(input("Enter the number of the fighter you choose: "))
player1 = notMoving(characters[charChoice - 1], (100, 400))
print ("PLAYER TWO")
charChoice2 = int(input("Enter the number of the fighter you choose: "))
player2 = notMoving(characters[charChoice2 - 1], (800, 400))

def round2():
    p1_shield_time = 5
    p2_shield_time = 5
    p1_health = 100
    p2_health = 100

    p1Attacks = pygame.sprite.Group()
    p2Attacks = pygame.sprite.Group()

    keep_going = True
    clock = pygame.time.Clock()

    while keep_going:
        clock.tick(30)

        #attacks and defenses
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
            elif ev.type == KEYDOWN:
                if ev.key == K_1:
                    p1_shield_time = 0
                elif ev.key == K_2:
                    pygame.sprite.Sprite.add(Attacks(attacks[charChoice - 1], (100, 375), 2), p1Attacks)
                elif ev.key == K_LEFT:
                    pygame.sprite.Sprite.add(Attacks(attacks[charChoice2 - 1], (800, 375), 2), p2Attacks)
                elif ev.key == K_RIGHT:
                    p2_shield_time = 0
        #collisions
        if p1_shield_time < 5:
            pygame.sprite.spritecollide(defend1, p2Attacks, True)
        if pygame.sprite.spritecollideany(player1, p2Attacks):
            pygame.sprite.spritecollide(player1, p2Attacks, True)
            p1_health -= 1
            #play hit sound
        if p2_shield_time < 5:
            pygame.sprite.spritecollide(defend2, p1Attacks, True)
        if pygame.sprite.spritecollideany(player2, p1Attacks):
            pygame.sprite.spritecollide(player2, p1Attacks, True)
            p2_health -= 1
            #play hit sound
        screen.blit(forest_bg, (0,0))
        p1Attacks.clear(screen, forest_bg)
        p1Attacks.update()
        p2Attacks.clear(screen, forest_bg)
        p2Attacks.update()

        if p1_shield_time < 5:
            defend1.update()
            screen.blit(defend1.image, defend1.rect)
        if p2_shield_time < 5:
            defend2.update()
            screen.blit(defend2.image, defend2.rect)

        player1.update()
        player2.update()
        p1Attacks.draw(screen)
        p2Attacks.draw(screen)

        screen.blit(player1.image, player1.rect)
        screen.blit(player2.image, player2.rect)
        print ("Player One Health:", p1_health)
        print ("Player Two Health:", p2_health)
        pygame.display.flip()

        if p1_health <= 0:
            print ("Player two has won!")
            return "p1"
        elif p2_health <= 0:
            print ("Plater one has won!")
            return "p2"
            
round2()
