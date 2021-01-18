'''
PLANTS VS PLANTS
Programmed by: Lily Cao and Fiona Hila
Programmed on: 2019/05/27
Programmed for: ICS3U1-04
Description: This is a game created using pygame. Users use the left and right arrows to attack and defend against
carnivorous plants. There are two sections to this game: single player and multiplayer. In single player, the
user battles against the computer in a total of three rounds, each more difficult than the last. In multiplayer,
the game is against two different users, both attacking and defending at the same time. In both versions, the game
ends when one of the players dies (health equals to 0).
'''
#import all necessary modules
import intro
import part1
import outro

#variables for results and game continuation
winner = True
game = True

#call intro
intro.origin()

while game == True:
    #call functions
    intro.startPage()

    #if single player level is chosen
    if intro.chooseLevel() == 1:
        part1.rules()
        
        #3 rounds of games played
        for i in range (1,4):
            if winner == True:
                part1.roundTitle(i)
                #if hero lost the game
                if part1.playGame(i) == False:
                    #exit the loop, results show lose page
                    winner = False
        part1.results(winner)
    elif intro.chooseLevel() == 2:
        #enter multiplayer code here
        continue
    if outro.continueGame() == False:
        game = False
