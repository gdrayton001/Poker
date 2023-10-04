from Card import Card
import random
import sqlite3

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
suits = ["clubs", "diamonds", "hearts", "spades"]
deck = []

for s in suits:
    for r in ranks:
        deck.append(Card(r,s))
        
def areEqual(hand1, hand2):
    if len(hand1) != len(hand2):
        return False
    for card in hand1:
        if not contains(card, hand2):
            return False
    return True
        
def areSimilar(hand1, hand2):
    if len(hand1) != 2 or len(hand2) != 2:
        raise ValueError
    if not ((hand1[0].rank == hand2[0].rank and hand1[1].rank == hand2[1].rank) or (hand1[0].rank == hand2[1].rank and hand1[1].rank == hand2[0].rank)):
        return False
    if hand1[0].suit == hand1[1].suit:
        if hand2[0].suit != hand2[1].suit:
            return False
    else:
        if hand2[0].suit == hand2[1].suit:
            return False
    return True

def bestHand(cards):
    if len(cards) != 7:
        raise ValueError
    bestPossibleHand = []
    for i in range(7):
        for j in range(i+1,7):
            myHand = cards.copy()
            myHand.pop(j)
            myHand.pop(i)
            if len(bestPossibleHand) == 0:
                bestPossibleHand = myHand
            elif handValue(myHand) > handValue(bestPossibleHand):
                bestPossibleHand = myHand
    return bestPossibleHand

def canCoexist(hand1, hand2):
    for card in hand1:
        if contains(card, hand2):
            return False
    return True

def chancesOfWinning(winPercent, num_opponents):
    return winPercent ** num_opponents

def contains(card, cards):
    for c in cards:
        if c.equals(card):
            return True
    return False

def correspondingList(orderList, checkList, itemList):
    if len(orderList) != len(itemList):
        raise IndexError
    output = []
    for i in range(len(orderList)):
        if orderList[i] in checkList:
            output.append(itemList[i])
    return output

def getHandRanking(hand, flop):
    if len(hand) != 2 or len(flop) != 5:
        raise ValueError
    if hasStraightFlush(hand+flop):
        for suit in suits:
            if contains(Card("10", suit), hand+flop) and contains(Card("jack", suit), hand+flop) and contains(Card("queen", suit), hand+flop) and contains(Card("king", suit), hand+flop) and contains(Card("ace", suit), hand+flop):
                return "Royal Flush"
        return "Straight Flush"
    elif hasFourOfAKind(hand+flop):
        return "Four of a Kind"
    elif hasFullHouse(hand+flop):
        return "Full House"
    elif hasFlush(hand+flop):
        return "Flush"
    elif hasStraight(hand+flop):
        return "Straight"
    elif hasThreeOfAKind(hand+flop):
        return "Three of a Kind"
    elif hasTwoPair(hand+flop):
        return "Two Pair"
    elif hasAPair(hand+flop):
        return "Pair"
    return "High Card"
    
def getHandStrength(hand):
    if len(hand) != 2:
        raise ValueError
    conn = sqlite3.connect('poker.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT score FROM hands 
    WHERE (card1_value=:c1_rank
    AND card1_suit=:c1_suit
    AND card2_value=:c2_rank
    AND card2_suit=:c2_suit)
    OR (card1_value=:c2_rank
    AND card1_suit=:c2_suit
    AND card2_value=:c1_rank
    AND card2_suit=:c1_suit)""", 
    {'c1_rank':hand[0].rank,
     'c1_suit':hand[0].suit,
     'c2_rank':hand[1].rank,
     'c2_suit':hand[1].suit})
    score = round(float(cursor.fetchall()[0][0]))
    cursor.close()
    conn.close()    
    return score
        
def handValue(hand):
    if len(hand) != 5:
        raise ValueError
    value = 0.0
    if hasStraightFlush(hand):
        value += 800.0
    elif hasFourOfAKind(hand):
        value += 700.0
        if hand[0].rank == hand[1].rank or hand[0].rank == hand[2].rank:
            value += hand[0].getNumericalValue()
            if hand[0].rank != hand[1].rank:
                value += hand[1].getNumericalValue()/100
            elif hand[0].rank != hand[2].rank:
                value += hand[2].getNumericalValue()/100
            elif hand[0].rank != hand[3].rank:
                value += hand[3].getNumericalValue()/100  
            else:
                value += hand[4].getNumericalValue()/100  
        else:
            value += hand[1].getNumericalValue()
            value += hand[0].getNumericalValue()/100
        return value
    elif hasFullHouse(hand):
        value += 600.0
        firstVal = hand[0].rank
        occur = 1
        for card in hand[1:]:
            if card.rank == firstVal:
                occur += 1
        if occur == 3:
            value += hand[0].getNumericalValue()
        else:
            value += hand[0].getNumericalValue()/100
        for card in hand[1:]:
            if card.rank != firstVal:
                if occur == 3:
                    value += card.getNumericalValue()/100
                else:
                    value += card.getNumericalValue()
                break
        return value
    elif hasFlush(hand):
        value += 500.0
    elif hasStraight(hand):
        value += 400.0
    elif hasThreeOfAKind(hand):
        value += 300.0
        extraCards = []
        threeCard = None
        for i in range(3):
            for j in range(i+1, 5):
                if hand[i].rank == hand[j].rank:
                    threeCard = hand[i].getNumericalValue()
                    break
            if threeCard != None:
                break
        for i in range(5):
            if hand[i].getNumericalValue() != threeCard:
                extraCards.append(hand[i].getNumericalValue())
            if len(extraCards) == 2:
                break
        value += threeCard
        value += max(extraCards)/100
        value += min(extraCards)/10000
        return value
    elif hasTwoPair(hand):
        value += 200.0
        pair1 = None
        pair2 = None
        extraCard = None
        for i in range(4):
            for j in range(i+1, 5):
                if hand[i].rank == hand[j].rank:
                    if pair1 == None:
                        pair1 = hand[i].getNumericalValue()
                    elif hand[i].getNumericalValue() != pair1:
                        pair2 = hand[i].getNumericalValue()
                        break
            if pair1 != None and pair2 != None:
                break
        for card in hand:
            if card.getNumericalValue() != pair1 and card.getNumericalValue() != pair2:
                extraCard = card.getNumericalValue()
                break
        value += max(pair1, pair2)
        value += min(pair1, pair2)/100
        value += extraCard/10000
        return value
    elif hasAPair(hand):
        value += 100.0
        pair = None
        extraCards = []
        for i in range(4):
            for j in range(i+1, 5):
                if hand[i].rank == hand[j].rank:
                    pair = hand[i].getNumericalValue()
                    break
            if pair != None:
                break
        for i in range(5):
            if hand[i].getNumericalValue() != pair:
                extraCards.append(hand[i].getNumericalValue())
            if len(extraCards) == 3:
                break
        value += pair
        value += max(extraCards)/100
        extraCards.remove(max(extraCards))
        value += max(extraCards)/10000
        value += min(extraCards)/1000000
        return value
    cardValues = []
    for card in hand:
        cardValues.append(card.getNumericalValue())
    if 1 in cardValues and 2 in cardValues and 3 in cardValues and 4 in cardValues and 13 in cardValues:
        cardValues.remove(13)
        cardValues.append(0)
    divisor = 1
    for i in range(len(cardValues)):
        value += max(cardValues) / divisor
        cardValues.remove(max(cardValues))
        divisor *= 100
    return value
        
def hasAPair(hand):
    for i in range(len(hand)-1):
        for j in range(i+1, (len(hand))):
            if hand[i].rank == hand[j].rank:
                return True
    return False

def hasFlush(hand):
    for i in range(len(hand)-4):
        for j in range(i+1, len(hand)-3):
            if hand[i].suit == hand[j].suit:
                for k in range(j+1, len(hand)-2):
                    if hand[i].suit == hand[k].suit:
                        for l in range(k+1, len(hand)-1):
                            if hand[i].suit == hand[l].suit:
                                for m in range(l+1, len(hand)):
                                    if hand[i].suit == hand[m].suit:
                                        return True
    return False

def hasFourOfAKind(hand):
    for i in range(len(hand)-3):
        for j in range(i+1, len(hand)-2):
            if hand[i].rank == hand[j].rank:
                for k in range(j+1, len(hand)-1):
                    if hand[i].rank == hand[k].rank:
                        for l in range(k+1, len(hand)):
                            if hand[i].rank == hand[l].rank:
                                return True
    return False

def hasFullHouse(hand):
    for i in range(len(hand)-2):
        for j in range(i+1, len(hand)-1):
            if hand[i].rank == hand[j].rank:
                for k in range(j+1, len(hand)):
                    if hand[k].rank == hand[i].rank:
                        myHand = hand.copy()
                        myHand.pop(k)
                        myHand.pop(j)
                        myHand.pop(i)
                        if hasAPair(myHand):
                            return True
    return False

def hasStraight(hand):
    for i in range(len(hand)):
        for j in range(len(hand)):
            if i == j:
                pass
            else:
                if hand[i].getNumericalValue() == hand[j].getNumericalValue() + 1:
                    for k in range(len(hand)):
                        if k == i or k == j:
                            pass
                        else:
                            if hand[j].getNumericalValue() == hand[k].getNumericalValue() + 1:
                                for l in range(len(hand)):
                                    if l == i or l == j or l == k:
                                        pass
                                    else:
                                        if hand[k].getNumericalValue() == hand[l].getNumericalValue() + 1:
                                            for m in range(len(hand)):
                                                if m == i or m == j or m == k or m == l:
                                                    pass
                                                else:
                                                    if hand[l].getNumericalValue() == hand[m].getNumericalValue() + 1 or hand[m].getNumericalValue() == hand[l].getNumericalValue() + 12:
                                                        return True
    return False

def hasStraightFlush(hand):
    for i in range(len(hand)-4):
        flush = [hand[i]]
        for j in range(i+1, len(hand)-3):
            if hand[i].suit == hand[j].suit:
                flush.append(hand[j])
                for k in range(j+1, len(hand)-2):
                    if hand[i].suit == hand[k].suit:
                        flush.append(hand[k])
                        for l in range(k+1, len(hand)-1):
                            if hand[i].suit == hand[l].suit:
                                flush.append(hand[l])
                                for m in range(l+1, len(hand)):
                                    if hand[i].suit == hand[m].suit: 
                                        flush.append(hand[m])
                                        if hasStraight(flush):
                                            return True
    return False

def hasThreeOfAKind(hand):
    for i in range(len(hand)-2):
        for j in range(i+1, len(hand)-1):
            if hand[i].rank == hand[j].rank:
                for k in range(j+1, len(hand)):
                    if hand[i].rank == hand[k].rank:
                        return True
    return False

def hasTwoPair(hand):
    for i in range(len(hand)-1):
        for j in range(i+1, len(hand)):
            if hand[i].rank == hand[j].rank:
                myHand = hand.copy()
                myHand.pop(j)
                myHand.pop(i)
                if hasAPair(myHand):
                    return True
    return False

def matchOrder(orderList, myList):
    index = 0
    for item in orderList:
        if item in myList:
            myList.remove(item)
            myList.insert(index, item)
            index += 1
    return myList

def randomCard(cards):
    card = random.choice(deck)
    while contains(card, cards):
        card = random.choice(deck)
    return card

def randomFiveCardHand(cards):
    fiveHandCombination = []
    card1 = random.choice(deck)
    while contains(card1, cards):
        card1 = random.choice(deck)
    fiveHandCombination.append(card1)
    card2 = random.choice(deck)
    while contains(card2, cards + fiveHandCombination):
        card2 = random.choice(deck)
    fiveHandCombination.append(card2)
    card3 = random.choice(deck)
    while contains(card3, cards + fiveHandCombination):
        card3 = random.choice(deck)
    fiveHandCombination.append(card3)
    card4 = random.choice(deck)
    while contains(card4, cards + fiveHandCombination):
        card4 = random.choice(deck)
    fiveHandCombination.append(card4)
    card5 = random.choice(deck)
    while contains(card5, cards + fiveHandCombination):
        card5 = random.choice(deck)
    fiveHandCombination.append(card5)
    return fiveHandCombination

def randomThreeCardHand(cards):
    threeHandCombination = []
    card1 = random.choice(deck)
    while contains(card1, cards):
        card1 = random.choice(deck)
    threeHandCombination.append(card1)
    card2 = random.choice(deck)
    while contains(card2, cards + threeHandCombination):
        card2 = random.choice(deck)
    threeHandCombination.append(card2)
    card3 = random.choice(deck)
    while contains(card3, cards + threeHandCombination):
        card3 = random.choice(deck)
    threeHandCombination.append(card3)  
    return threeHandCombination

def randomTwoCardHand(cards):
    hand = []
    card1 = random.choice(deck)
    while contains(card1, cards):
        card1 = random.choice(deck)
    hand.append(card1)
    card2 = random.choice(deck)
    while contains(card2, cards + hand):
        card2 = random.choice(deck)
    hand.append(card2)
    return hand

def ties(myHand, oppHand, flop):
    if len(myHand) != 2 or len(oppHand) != 2 or len(flop) != 5:
        raise ValueError
    if handValue(bestHand(oppHand+flop)) == handValue(bestHand(myHand+flop)):
        return True
    return False

def toInt(amount):
    if not (amount.endswith('K') or amount.endswith('M')):
        raise ValueError
    amount = amount.replace('K', '000')
    amount = amount.replace('M', '000')
    return int(amount)

def toString(amount):
    output = str(amount)
    if len(output) in range(3,7):
        output = output[:-3] + "K"
    elif len(output) > 6:
        output = output[:-6] + "M"
    return output

def wins(myHand, oppHand, flop):
    if len(myHand) != 2 or len(oppHand) != 2 or len(flop) != 5:
        raise ValueError
    if handValue(bestHand(oppHand+flop)) > handValue(bestHand(myHand+flop)):
        return False
    return True

def winners(flop, hands):
    if len(flop) != 5:
        raise ValueError
    output = []
    for hand in hands:
        if len(output) == 0:
            output.append(hand)
        elif ties(hand, output[0], flop):
            output.append(hand)
        elif wins(hand, output[0], flop):
            output.clear()
            output.append(hand)
    return output