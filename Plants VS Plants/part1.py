'''
PLANTS VS PLANTS PART 1
Programmed by: Lily Cao
Programmed on: 2019/05/27
Programmed for: ICS3U1-04
Description: This is the single player part of the game PLANTS VS PLANTS. This code includes the weapon and plant
sprite classes, rules, round titles, gameplay, and results functions.
'''

#import all necessary modules
import pygame
import random
import time
from pygame.locals import * 
pygame.init()

#set the display screen size, caption, and image
screen = pygame.display.set_mode((1000,500))
background = pygame.image.load("background.png")
background = background.convert()
pygame.display.set_caption("PLANTS VS PLANTS")

#lists of heros, villains, and their respective weapons
heroList =["lotus.png", "amanita muscaria.png","grass.png"]
villainList = ["venus flytrap.png", "piranha plant.png", "corpse lily.png"]
weaponH = ["peace sign.png", "spore.png", "vine.png"]
weaponV = ["digestive enzyme.png", "fire ball.png", "corpse bomb.png"]

#create sprite groups of weapons for hero and villain
heroAttack = pygame.sprite.Group()
villainAttack = pygame.sprite.Group()

#list of fonts needed for part1
my_font = pygame.font.SysFont("plantagenetcherokee", 74) #system fonts, needs font name
my_font.set_bold(True)
font = pygame.font.SysFont("raavi", 30)
font3 = pygame.font.SysFont("raavi", 60)
font3.set_bold(True)


winner = True


#create a class for attack weapons
class Attack(pygame.sprite.Sprite):
    '''
    parameters: - image refers to the image of the weapon used
                - location refers to where the weapon begins
                - attackPower refers to the speed of the weapon
    initiates and sets attributes of the sprite
    '''
    def __init__(self, image, location, attackPower):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        self.image = pygame.image.load(image)
        self.image.convert()
        #creates rect from image
        self.rect = self.image.get_rect()

        #set the position, direction, and speed of the weapon
        self.rect.topleft = location
        self.dir_x = 1
        self.dir_y = 0
        self.speed = attackPower

    '''
    defines the movement of the sprite
    '''
    def update(self):
        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)



#create a class for the stationary sprites (ie. shields, autotrophs, heterotrophs)
class Stationary(pygame.sprite.Sprite):
    '''
    parameters: - image refers to the image of the weapon used
                - location refers to where the weapon begins
    initiates and sets attributes of the sprite
    '''
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        self.image = pygame.image.load(image)
        self.image.convert()
        self.rect = self.image.get_rect()

        #set the position of the stationary sprite
        self.rect.bottomleft = location

#creates shield sprites using Stationary class
shieldH = Stationary("blue shield.png",(250,400))
shieldV = Stationary("red shield.png",(750,400))


'''
this function displays the rules of the game
and returns when complete
'''
def rules():
    #set background colour
    background.fill((0, 0, 0))
    
    #title and set of rules
    title = my_font.render("Rules", True, (255,255,255))
    rule1 = font.render("1. Press the right arrow to attack.", True, (255,255,255))
    rule2 = font.render("2. Press the left arrow to defend.", True, (255,255,255))
    rule3 = font.render("3. Kill the hereotroph before they kill you.", True, (255,255,255))
    final = font3.render("The fate of the world", True, (255,255,255))
    final2 = font3.render("lies in your hands...", True, (255,255,255))

    #blit rules
    screen.blit(background, (0,0))
    screen.blit(title, ((1000-title.get_width())/2,20))
    screen.blit(rule1, ((1000-rule1.get_width())/2,120))
    screen.blit(rule2, ((1000-rule2.get_width())/2,170))
    screen.blit(rule3, ((1000-rule3.get_width())/2,220))
    screen.blit(final, ((1000-final.get_width())/2,300))
    screen.blit(final2, ((1000-final2.get_width())/2,370))
    pygame.display.flip()

    #set pygame clock
    clock = pygame.time.Clock()
    keep_going = True
    
    while keep_going:
        clock.tick(30)
        #if user clicks quit, game ends
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
                quit()
        time.sleep(5)
        return

'''
parameter: round refers to the round number of the game
this function displays the round number of the game
and returns when complete
'''
def roundTitle(round):
    #set background colour
    background.fill((0, 0, 0))

    #text for round number
    titleText = my_font.render("Round "+str(round), True, (255,255,255))

    #blit screen
    screen.blit(background, (0,0))
    screen.blit(titleText, ((1000-titleText.get_width())/2, (250-titleText.get_height()/2)))
    pygame.display.flip()
    
    #set pygame clock
    clock = pygame.time.Clock()
    keep_going = True

    #loop
    while keep_going:
        clock.tick(30)
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keep_going = False
                quit()
        time.sleep(2)
        return
            

'''
parameter: roundNumber refers to the round number of the game
this function allows users to play the game,
using the left and right arrows as attack and defense.
It returns True if hero wins, and False when villain wins
'''
def playGame(roundNumber):
    #load and convert image
    background = pygame.image.load("background.png")
    background = background.convert()
    screen.blit(background, (0,0))

    #sets attack sound effect
    hit = pygame.mixer.Sound("attack sound.wav")
    hit.set_volume(1.0)

    #sets background music
    pygame.mixer.music.load("background fighting music.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    
    #set hero and villain
    hero = Stationary(heroList[roundNumber-1],(100,400))
    villain = Stationary(villainList[roundNumber-1],(800,400))

    #shield counters (how long shield stays on screen)
    heroShieldTime = 5
    villainShieldTime = 5

    #health levels
    heroHealth = 100
    villainHealth = 100

    #sets clock
    keep_going = True
    clock = pygame.time.Clock()

    #while loop keeps game going
    while keep_going:
        clock.tick(30)
        #shields are inactivated
        heroShieldTime+=1
        villainShieldTime+=1

        #text for hero and villain health level
        heroScore = font.render(str(heroHealth), True, (255,255,255))
        villainScore = font.render(str(villainHealth), True, (255,255,255))

        
        for ev in pygame.event.get():
            #if user clicks quit, game stops
            if ev.type == QUIT:
                keep_going = False
                quit()
            #if user hits a key
            elif ev.type == KEYDOWN:
                #if user hits right arrow
                if ev.key == K_RIGHT:
                    #user weapon sprite added to group, starts to attack
                    pygame.sprite.Sprite.add(Attack(weaponH[roundNumber-1],(100,375),6+roundNumber*2),heroAttack)
                #if user hits left arrow
                elif ev.key == K_LEFT:
                    #user shield is activated
                    heroShieldTime = 0

        '''
        villain's attacks and defends 
        '''
        if random.randint(1,16-roundNumber*2) == 1:
            #villain weapon sprite added to group, attacks
            pygame.sprite.Sprite.add(Attack(weaponV[roundNumber-1],(800,350),-6-roundNumber*2),villainAttack)
        
        if random.randint(1,25-roundNumber*5) == 2:
            #villain shield activated
            villainShieldTime = 0


        '''
        checking for collisions
        '''
        #if hero's shield is active, and villain weapon hits, weapon is destroyed
        if heroShieldTime<5:
            pygame.sprite.spritecollide(shieldH, villainAttack, True)

        #if weapon hits hero, hero loses a life, weapon destroyed, sound effect plays
        if pygame.sprite.spritecollideany(hero, villainAttack):
            pygame.sprite.spritecollide(hero, villainAttack, True)
            heroHealth-=1
            hit.play()

        #if villain's shield is active, and hero weapon hits, weapon is destroyed
        if villainShieldTime<5:
            pygame.sprite.spritecollide(shieldV, heroAttack, True)
            
        #if weapon hits villain, villain loses a life, weapon destroyed, sound effect plays
        if pygame.sprite.spritecollideany(villain, heroAttack):
            pygame.sprite.spritecollide(villain, heroAttack, True)
            villainHealth-=1
            hit.play()
        
        #updates screen
        screen.blit(background, (0,0))
        heroAttack.clear(screen, background)
        heroAttack.update()
        villainAttack.clear(screen, background)
        villainAttack.update()
        
        #blits only if shield is active
        if heroShieldTime<5:
            shieldH.update()
            screen.blit(shieldH.image, shieldH.rect)
        if villainShieldTime<5:
            shieldV.update()
            screen.blit(shieldV.image, shieldV.rect)
        
        hero.update()
        villain.update()
        heroAttack.draw(screen)
        villainAttack.draw(screen)
        
        screen.blit(hero.image, hero.rect)
        screen.blit(villain.image, villain.rect)
        screen.blit(heroScore, (120, 425))
        screen.blit(villainScore, (825, 425))
        pygame.display.flip()

        #check if health is 0
        if villainHealth<=0:
            return True
        elif heroHealth <=0:
            return False

'''
parameter: win refers to whether or not the user has won the game
this function displays the results of the game
and returns once complete
'''
def results(win):
    #set background colour
    background.fill((0, 0, 0))
    screen.blit(background, (0,0))

    #pause for dramatic effect
    time.sleep(1)

    if win == True:
        #winning text
        text1 = font.render("The heterotrophs have been defeated.", True, (255,255,255))
        text2 = font.render("It is your duty to ensure no plants will ever consume flesh ever again...", True, (255,255,255))
        text3 = font3.render("Your mission begins now.", True, (255,255,255))


        #blits winning text
        screen.blit(background, (0,0))
        screen.blit(text1, ((1000-text1.get_width())/2, 75))
        screen.blit(text2, ((1000-text2.get_width())/2, 150))
        screen.blit(text3, ((1000-text3.get_width())/2, 325))
        pygame.display.flip()

    elif win == False:
        #losing text
        text1 = font.render("The autotrophs have been defeated.", True, (255,255,255))
        text2 = font.render("The heterotrophs have decided to further disrupt the balance...", True, (255,255,255))
        text3 = font.render("And consume other plants.", True, (255,255,255))
        text4 = font3.render("You have failed your mission.", True, (255,255,255))

        #blits losing text
        screen.blit(background, (0,0))
        screen.blit(text1, ((1000-text1.get_width())/2, 50))
        screen.blit(text2, ((1000-text2.get_width())/2, 150))
        screen.blit(text3, ((1000-text3.get_width())/2, 200))
        screen.blit(text4, ((1000-text4.get_width())/2, 350))
        pygame.display.flip()

    #to let user read the results
    time.sleep(5)
