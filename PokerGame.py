from CPU import CPU
from Player import Player
from PokerCalculator import *

class Game:

    players = []
    pot = 0
    blind = 0
    betAmount = 0
    activePlayer = None
    endPlayer = None
    threeCardFlop = []
    fourthCard = None
    fifthCard = None
    hands = 0
    
    def __init__(self, players, start_chips, start_blind):
        if start_blind * 4 > start_chips:
            raise Exception('Blind cannot be more than one-fourth the number of chips')
        self.players = players
        for p in self.players:
            p.setChips(start_chips)
        self.blind = start_blind
        
    def activePlayers(self):
        output = []
        for p in self.players:
            if p.active:
                output.append(p)
        return output
    
    def awardChipsTo(self, winners):
        if self.canSplit(winners):
            prize = round(self.pot/len(winners))
            for p in winners:
                p.setChips(prize)
            self.pot = 0
        else:
            outPlayer = winners[0]
            for p in winners[1:]:
                if p.eligibleToWin < outPlayer.eligibleToWin:
                    outPlayer = p
            prize = round(outPlayer.eligibleToWin/len(winners))
            for p in winners:
                p.setChips(prize)
            self.pot -= outPlayer.eligibleToWin
            otherWinners = winners.copy()
            otherWinners.remove(outPlayer)
            self.awardChipsTo(otherWinners)
        
    def bigBlind(self):
        p = self.getPlayerWithOrder(len(self.players)-1)
        while p.lost:
            p = self.getPlayerWithOrder((p.order-1)%len(self.players))
        return p
            
    def canSplit(self, winners):
        try:
            eligible = winners[0].eligibleToWin
            for p in winners[1:]:
                if p.eligibleToWin != eligible:
                    return False
        except IndexError:
            pass
        return True
            
    def collectBets(self):
        self.setPrizeEligibilities()
        self.betAmount = 0
        for p in self.playersInGame():
            self.pot += p.betting
            p.setChips(-p.betting)
            p.resetBet()
            p.label.config(text=p.name + '\n chips: ' + str(p.chips))   
            
    def endGame(self):
        return
            
    def endHand(self):
        self.collectBets()
        self.hands += 1
        if self.handIsLive():
            if not self.nextRoundIsPlayable():
                if self.threeCardFlop == []:
                    self.setThreeCardFlop()
                if self.fourthCard == None:
                    self.setFourthCard()
                if self.fifthCard == None:
                    self.setFifthCard()
            winners = self.getWinners()
        else:
            winners = [self.activePlayer]
        return winners
    
    def endRound(self):
        self.collectBets()
        self.setActivePlayer(self.getStartingPlayerOrder())
        self.setEndPlayer(self.getStartingPlayerOrder())
        if self.threeCardFlop == []:
            self.setThreeCardFlop()
            return 0
        elif self.fourthCard == None:
            self.setFourthCard()
            return 1
        elif self.fifthCard == None:
            self.setFifthCard()
            return 2
        else:
            self.endHand()
            return 3 
        
    def fold(self, player):
        player.fold()  
        
    def gameIsOver(self):
        playersLeft = 0
        for p in self.players:
            if p.chips > 0:
                playersLeft += 1
            if playersLeft > 1:
                return False
        return True
    
    def gameWinner(self):
        if not self.gameIsOver():
            raise Exception("Cannot declare winner until game is over")
        for p in self.players:
            if p.chips > 0:
                return p
    
    def getPlayerWithOrder(self, order):
        for p in self.players:
            if p.order == order:
                return p 
            
    def getStartingPlayerOrder(self):
        if self.bigBlind().active:
            return len(self.players) - 1
        for i in range(len(self.players)):
            if self.getPlayerWithOrder(i).active:
                return i  
            
    def getWinners(self):
        if self.fifthCard == None:
            raise Exception("Winner cannot be determined because the flop is not yet complete")
        if self.handIsLive():
            return self.showdown()
        else:
            return [self.activePlayer]
            
    def handIsLive(self):
        activePlayers = 0
        for p in self.players:
            if p.active:
                activePlayers += 1
            if activePlayers > 1:
                return True
        return False    
            
    def littleBlind(self):
        p = self.getPlayerWithOrder(len(self.players)-2)
        while p.lost or self.bigBlind().label == p.label:
            p = self.getPlayerWithOrder((p.order-1)%len(self.players))
        return p  
    
    def nextHand(self):
        if self.gameIsOver():
            self.endGame()
            return -1
        self.pot = 0
        if self.hands % len(self.players) == 0 and self.hands > 0:
            self.blind *= 2
        self.betAmount = self.blind
        self.threeCardFlop = []
        self.fourthCard = None
        self.fifthCard = None
        cardsDealt = []
        for p in self.players:
            p.clearHand()
            if p.chips == 0:
                p.eliminate()
            else:
                p.activate()
                p.deal(randomTwoCardHand(cardsDealt))
                cardsDealt.append(p.hand[0])
                cardsDealt.append(p.hand[1])
        startOrder = 0
        while self.getPlayerWithOrder(startOrder).lost:
            startOrder += 1
        self.setActivePlayer(startOrder)
        self.setEndPlayer(startOrder)
        
    def nextRoundIsPlayable(self):
        playersCanBet = 0
        for p in self.players:
            if p.chips > 0 and p.active:
                playersCanBet += 1
            if playersCanBet > 1:
                return True
        return False    
        
    def nextTurn(self, order):
        offset = 0
        while self.getPlayerWithOrder(order+offset).lost:
            offset += 1
        self.setActivePlayer(order+offset)
        if self.activePlayer == self.endPlayer:
            return -1
        elif not self.activePlayer.active or self.activePlayer.chips == 0:
            return self.nextTurn((order+1) % len(self.players))
        return order    
        
    def placeBetFor(self, player, amount):
        player.bet(min(player.chips, amount))
        
    def playersInGame(self):
        output = []
        for p in self.players:
            if not p.lost:
                output.append(p)
        return output
        
    def raiseBet(self, player, amount):
        self.betAmount = player.betting + amount
        self.endPlayer = player   
        
    def resetOrders(self):
        for p in self.players:
            p.setOrder((p.order+1)%len(self.players))
                
    def setActivePlayer(self, order):
        for p in self.players:
            if p.order == order:
                self.activePlayer = p
        print(self.activePlayer.name)
    
    def setEndPlayer(self, order):
        for p in self.players:
            if p.order == order:
                self.endPlayer = p 
                
    def setFifthCard(self):
        cardsDealt = []
        for p in self.playersInGame():
            cardsDealt.append(p.hand[0])
            cardsDealt.append(p.hand[1])        
        self.fifthCard = randomCard(cardsDealt + self.threeCardFlop + [self.fourthCard])     
                
    def setFourthCard(self):
        cardsDealt = []
        for p in self.playersInGame():
            cardsDealt.append(p.hand[0])
            cardsDealt.append(p.hand[1])        
        self.fourthCard = randomCard(cardsDealt + self.threeCardFlop)    
        
    def setPrizeEligibilities(self):
        for p in self.activePlayers():
            if p.chips - p.betting > 0:
                eligible = self.pot
                for q in self.players:
                    eligible += q.betting
            else:
                eligible = p.eligibleToWin
                for q in self.players:
                    eligible += min(q.betting, p.betting)
            p.setEligibleToWin(eligible)
    
    def setThreeCardFlop(self):
        cardsDealt = []
        for p in self.playersInGame():
            cardsDealt.append(p.hand[0])
            cardsDealt.append(p.hand[1])
        self.threeCardFlop = randomThreeCardHand(cardsDealt)          
        
    def showdown(self):
        hands = []
        output = []
        for p in self.activePlayers():
            hands.append(p.hand)
        for p in self.activePlayers():
            for hand in winners(self.threeCardFlop + [self.fourthCard, self.fifthCard], hands):
                if areEqual(p.hand, hand):
                    output.append(p)
        return output