#!/usr/bin/python

#Import Library
import pygame
from pygame.locals import *
import random
import copy
from typing import List

#Load Images
icon = pygame.image.load('resources/icon.png')
cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA = pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

#Set Icon
pygame.display.set_icon(icon)

#Global Constants
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def getAmt(card):
    ''' Returns the amount the card is worth.
E.g. Ace is default 11. 10/Jack/Queen/King is 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print('getAmt broke')
        exit()

def genCard(cList, xList):
    '''Generates an card from cList, removes it from cList, and appends it to xList.
Returns if card is Ace and the card itself.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Generates two cards for dealer and user, one at a time for each.
Returns if card is Ace and the total amount of the cards per person.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 624

CARD_WIDTH = 100
CARD_HEIGHT = 140

BUTTON_WIDTH = 75
BUTTON_HEIGHT = 25

# + add buttons of what to do
# + show cards
# + show the number of cards
# + make everything abstract
# + remove all the shit
# + show you money
# add api that change the stuff
# scoreboard
# fix text rotation and position
# split cards
# show logs/chat system
# make animation


def rotate(img, pos, angle):
    w, h = img.get_size()
    img2 = pygame.Surface((w*2, h*2), pygame.SRCALPHA)
    img2.blit(img, (w-pos[0], h-pos[1]))
    return pygame.transform.rotate(img2, angle)


class Player:
    score: int
    cards: List
    name: str
    cards_sum: str


class Dealer:
    cards: List
    cards_sum: str


class Game:
    players: List[Player]
    dealer: Dealer
    wins: int
    loses: int
    restart: bool
    cards: int



def show(game: Game):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        pygame.display.update()

        # elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
        #     #gives player a card if they don't break blackjack rules
        #     card, cA = genCard(ccards, userCard)
        #     userA += cA
        #     userSum += getAmt(card)
        #     print('User: %i' % userSum)
        #     while userSum > 21 and userA > 0:
        #         userA -= 1
        #         userSum -= 10
        # elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
        #     #when player stands, the dealer plays
        #     stand = True
        #     while dealSum <= userSum and dealSum < 17:
        #         card, cA = genCard(ccards, dealCard)
        #         dealA += cA
        #         dealSum += getAmt(card)
        #         print('Dealer: %i' % dealSum)
        #         while dealSum > 21 and dealA > 0:
        #             dealA -= 1
        #             dealSum -= 10
        # elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
        #     #restarts the game, updating scores
        #     if userSum == dealSum:
        #         pass
        #     elif userSum <= 21 and len(userCard) == 5:
        #         winNum += 1
        #     elif userSum <= 21 and dealSum < userSum or dealSum > 21:
        #         winNum += 1
        #     else:
        #         loseNum += 1
        #     gameover = False
        #     stand = False
        #     userCard = []
        #     dealCard = []
        #     ccards = copy.copy(cards)
        #     userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
        #     restartB = pygame.draw.rect(background, (80, 150, 15), (SCREEN_WIDTH - BUTTON_WIDTH*4 - 20, BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT))



def main():
    #Local Variable
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0

    #Initialize Game
    pygame.init()
    #screen = pygame.display.set_mode((640, 480))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Restart', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))

    hitB = pygame.draw.rect(background, gray, (SCREEN_WIDTH - BUTTON_WIDTH - 10, BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT))
    standB = pygame.draw.rect(background, gray, (SCREEN_WIDTH - BUTTON_WIDTH*2 - 20, BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT))


    dealer = Dealer()
    dealer.cards = [cBack, diamond5]
    dealer.cards_sum = "6/17"

    player = Player()
    player.cards_sum = "15/8"
    player.cards = [club4, club10]
    player.name = "JacobGGman"
    player.score = 55

    game = Game()
    game.loses = 2
    game.wins = 3
    game.restart = True
    game.dealer = dealer
    game.players = [player] * 7
    game.cards = 69

    # todo:
    while True:
        #checks if game is over
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        #background needs to be redisplayed because it gets updated
        winTxt = font.render('Wins: %i' % game.wins, 1, black)
        loseTxt = font.render('Losses: %i' % game.loses, 1, black)
        cards_text = font.render('Cards: %i' % game.cards, 1, black)

        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
            #     #gives player a card if they don't break blackjack rules
            #     card, cA = genCard(ccards, userCard)
            #     userA += cA
            #     userSum += getAmt(card)
            #     print('User: %i' % userSum)
            #     while userSum > 21 and userA > 0:
            #         userA -= 1
            #         userSum -= 10
            # elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
            #     #when player stands, the dealer plays
            #     stand = True
            #     while dealSum <= userSum and dealSum < 17:
            #         card, cA = genCard(ccards, dealCard)
            #         dealA += cA
            #         dealSum += getAmt(card)
            #         print('Dealer: %i' % dealSum)
            #         while dealSum > 21 and dealA > 0:
            #             dealA -= 1
            #             dealSum -= 10
            # elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
            #     #restarts the game, updating scores
            #     if userSum == dealSum:
            #         pass
            #     elif userSum <= 21 and len(userCard) == 5:
            #         winNum += 1
            #     elif userSum <= 21 and dealSum < userSum or dealSum > 21:
            #         winNum += 1
            #     else:
            #         loseNum += 1
            #     gameover = False
            #     stand = False
            #     userCard = []
            #     dealCard = []
            #     ccards = copy.copy(cards)
            #     userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
            #     restartB = pygame.draw.rect(background, (80, 150, 15), (SCREEN_WIDTH - BUTTON_WIDTH*4 - 20, BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT))

        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (SCREEN_WIDTH - BUTTON_WIDTH - 10 + 29, BUTTON_HEIGHT + 10 + 3))
        screen.blit(standTxt, (SCREEN_WIDTH - BUTTON_WIDTH*2 - 20 + 21, BUTTON_HEIGHT + 10 + 3))
        screen.blit(winTxt, ((SCREEN_WIDTH - BUTTON_WIDTH*2 - 20 , BUTTON_HEIGHT + 40 + 3)))
        screen.blit(loseTxt, ((SCREEN_WIDTH - BUTTON_WIDTH*2 - 20, BUTTON_HEIGHT + 60 + 3)))
        screen.blit(cards_text, ((120, 10 + CARD_HEIGHT)))

        #displays dealer's cards
        for card in game.dealer.cards:
            x = SCREEN_WIDTH // 2 + game.dealer.cards.index(card) * 30 - CARD_WIDTH // 2
            screen.blit(card, (x, 10))
        screen.blit(font.render(game.dealer.cards_sum, 1, black), (SCREEN_WIDTH // 2, CARD_HEIGHT * 1.2))

        for x in range(min(game.cards, 16)):
            screen.blit(cBack, (120 + x, 10))

        number_of_players = 7
        mid_player = number_of_players // 2

        #displays player's cards


        for i in range(number_of_players):
            player = game.players[i]
            if player is None:
                continue
            score_text = font.render(player.cards_sum, 1, black)
            username_text = font.render(player.name, 1, black)
            money_text = font.render(str(player.score), 1, black)
            displays_array = player.cards + [score_text, money_text, username_text]
            for card in displays_array[::-1]:
                x = (SCREEN_WIDTH // number_of_players)*i + displays_array.index(card) * 15
                y = SCREEN_HEIGHT - CARD_HEIGHT - displays_array.index(card) * 40 - abs(mid_player - i)*50
                card = pygame.transform.rotate(card, (mid_player - i)*-10)

                screen.blit(card, (x, y))


        #when game is over, draws restart button and text, and shows the dealer's second card
        #if gameover or stand:
        if game.restart:
            screen.blit(gameoverTxt, (SCREEN_WIDTH // 2 - 60, 200))
            restartB = pygame.draw.rect(background, gray, (SCREEN_WIDTH - BUTTON_WIDTH*4 - 20, BUTTON_HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT))
            screen.blit(restartTxt, (SCREEN_WIDTH - BUTTON_WIDTH*4 - 20 + 287 - 270, BUTTON_HEIGHT + 10 + 228 - 225))
            #screen.blit(dealCard[1], (120, 10))
            
        pygame.display.update()
            

if __name__ == '__main__':
    main()
