from PokerSimulator import *
import random
import time

def testHasAPair():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    random.shuffle(test1)
    random.shuffle(test2)
    assert hasAPair(test1)
    assert not hasAPair(test2)
    print("Has a Pair Successfully Tested")
    
def testHasTwoPair():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    assert not hasTwoPair(test1)
    assert not hasTwoPair(test2)
    assert hasTwoPair(test3)
    print("Has Two Pair Successfully Tested")    
    
def testHasThreeOfAKind():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    test4 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("jack", "clubs"), Card("3", "clubs")]
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    random.shuffle(test4)
    assert not hasThreeOfAKind(test1)
    assert not hasThreeOfAKind(test2)
    assert not hasThreeOfAKind(test3)
    assert hasThreeOfAKind(test4)
    print("Has Three of a Kind Successfully Tested")   
    
def testHasStraight():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    test4 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("jack", "clubs"), Card("3", "clubs")]
    test5 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("6", "clubs")]
    test6 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("ace", "clubs")]
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    random.shuffle(test4)
    random.shuffle(test5)
    random.shuffle(test6)    
    assert not hasStraight(test1)
    assert not hasStraight(test2)
    assert not hasStraight(test3)
    assert not hasStraight(test4)
    assert hasStraight(test5)
    assert hasStraight(test6)
    print("Has Straight Successfully Tested")     

def testHasFlush():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    test4 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("jack", "clubs"), Card("3", "clubs")]
    test5 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("6", "clubs")]
    test6 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("ace", "clubs")]
    test7 = [Card("2", "clubs"), Card("4", "clubs"), Card("8", "clubs"), Card("3", "clubs"), Card("ace", "clubs")]
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    random.shuffle(test4)
    random.shuffle(test5)
    random.shuffle(test6)   
    random.shuffle(test7)  
    assert not hasFlush(test1)
    assert not hasFlush(test2)
    assert not hasFlush(test3)
    assert not hasFlush(test4)
    assert not hasFlush(test5)
    assert not hasFlush(test6)
    assert hasFlush(test7)
    print("Has Flush Successfully Tested")   
    
def testHasFullHouse():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    test4 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("jack", "clubs"), Card("3", "clubs")]
    test5 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("6", "clubs")]
    test6 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("ace", "clubs")]
    test7 = [Card("2", "clubs"), Card("4", "clubs"), Card("8", "clubs"), Card("3", "clubs"), Card("ace", "clubs")]
    test8 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("3", "clubs"), Card("3", "diamonds")]
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    random.shuffle(test4)
    random.shuffle(test5)
    random.shuffle(test6)   
    random.shuffle(test7)  
    random.shuffle(test8)
    assert not hasFullHouse(test1)
    assert not hasFullHouse(test2)
    assert not hasFullHouse(test3)
    assert not hasFullHouse(test4)
    assert not hasFullHouse(test5)
    assert not hasFullHouse(test6)
    assert not hasFullHouse(test7)
    assert hasFullHouse(test8)
    print("Has Full House Successfully Tested")   
    
def testHasFourOfAKind():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    test4 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("jack", "clubs"), Card("3", "clubs")]
    test5 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("6", "clubs")]
    test6 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("ace", "clubs")]
    test7 = [Card("2", "clubs"), Card("4", "clubs"), Card("8", "clubs"), Card("3", "clubs"), Card("ace", "clubs")]
    test8 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("3", "clubs"), Card("3", "diamonds")]
    test9 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("2", "spades"), Card("3", "diamonds")]
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    random.shuffle(test4)
    random.shuffle(test5)
    random.shuffle(test6)   
    random.shuffle(test7)  
    random.shuffle(test8)
    random.shuffle(test9)
    assert not hasFourOfAKind(test1)
    assert not hasFourOfAKind(test2)
    assert not hasFourOfAKind(test3)
    assert not hasFourOfAKind(test4)
    assert not hasFourOfAKind(test5)
    assert not hasFourOfAKind(test6)
    assert not hasFourOfAKind(test7)
    assert not hasFourOfAKind(test8)
    assert hasFourOfAKind(test9)
    print("Has Four of a Kind Successfully Tested")    
    
def testHasStraightFlush():
    test1 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test2 = [Card("2", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("3", "clubs")]
    test3 = [Card("2", "clubs"), Card("2", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("3", "clubs")]
    test4 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("jack", "clubs"), Card("3", "clubs")]
    test5 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("6", "clubs")]
    test6 = [Card("2", "clubs"), Card("3", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("ace", "clubs")]
    test7 = [Card("2", "clubs"), Card("4", "clubs"), Card("8", "clubs"), Card("3", "clubs"), Card("ace", "clubs")]
    test8 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("3", "clubs"), Card("3", "diamonds")]
    test9 = [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("2", "spades"), Card("3", "diamonds")]
    test10 = [Card("2", "clubs"), Card("3", "clubs"), Card("4", "clubs"), Card("5", "clubs"), Card("6", "clubs")]
    test11 = [Card("2", "clubs"), Card("3", "clubs"), Card("4", "clubs"), Card("5", "clubs"), Card("ace", "clubs")]    
    random.shuffle(test1)
    random.shuffle(test2)
    random.shuffle(test3)
    random.shuffle(test4)
    random.shuffle(test5)
    random.shuffle(test6)   
    random.shuffle(test7)  
    random.shuffle(test8)
    random.shuffle(test9)
    random.shuffle(test10)
    random.shuffle(test11)    
    assert not hasStraightFlush(test1)
    assert not hasStraightFlush(test2)
    assert not hasStraightFlush(test3)
    assert not hasStraightFlush(test4)
    assert not hasStraightFlush(test5)
    assert not hasStraightFlush(test6)
    assert not hasStraightFlush(test7)
    assert not hasStraightFlush(test8)
    assert not hasStraightFlush(test9)
    assert hasStraightFlush(test10)
    assert hasStraightFlush(test11)
    print("Has Straight Flush Successfully Tested")     
    
def testHandValue():
    hands = [[Card("5", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("king", "diamonds"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("king", "diamonds"), Card("8", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("king", "diamonds"), Card("7", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("king", "diamonds"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("8", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("7", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("ace", "clubs"), Card("ace", "diamonds"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("4", "hearts"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("ace", "clubs"), Card("4", "clubs"), Card("2", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("6", "clubs"), Card("4", "clubs"), Card("2", "clubs")],
    [Card("5", "clubs"), Card("3", "diamonds"), Card("6", "clubs"), Card("4", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("king", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("jack", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("5", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("6", "clubs"), Card("4", "clubs"), Card("ace", "clubs"), Card("queen", "clubs"), Card("8", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("jack", "clubs"), Card("jack", "diamonds")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("queen", "clubs"), Card("queen", "diamonds")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("4", "hearts"), Card("jack", "clubs"), Card("jack", "diamonds")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("4", "hearts"), Card("queen", "clubs"), Card("queen", "diamonds")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("3", "spades"), Card("7", "clubs")],
    [Card("3", "clubs"), Card("3", "diamonds"), Card("3", "hearts"), Card("3", "spades"), Card("8", "clubs")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("4", "hearts"), Card("4", "spades"), Card("7", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("ace", "clubs"), Card("4", "clubs"), Card("2", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("6", "clubs"), Card("4", "clubs"), Card("2", "clubs")],
    [Card("5", "clubs"), Card("3", "clubs"), Card("6", "clubs"), Card("4", "clubs"), Card("7", "clubs")]]
    #for h in hands:
        #random.shuffle(h)
    for i in range(len(hands)-1):
        assert handValue(hands[i]) < handValue(hands[i+1])
    print("Hand Value Successfully Tested")

def testBestHand():
    hands = [[Card("5", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs"), Card("2", "diamonds"), Card("3", "diamonds")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("7", "clubs"), Card("5", "diamonds"), Card("3", "diamonds")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("3", "clubs"), Card("3", "diamonds"), Card("king", "clubs"), Card("jack", "clubs"), Card("10", "diamonds")],
    [Card("4", "clubs"), Card("4", "diamonds"), Card("4", "hearts"), Card("king", "clubs"), Card("jack", "clubs"), Card("10", "diamonds"), Card("3", "diamonds")],
    [Card("4", "clubs"), Card("6", "diamonds"), Card("5", "hearts"), Card("7", "diamonds"), Card("3", "diamonds"), Card("ace", "clubs"), Card("ace", "hearts")],
    [Card("4", "clubs"), Card("6", "diamonds"), Card("5", "hearts"), Card("7", "diamonds"), Card("3", "diamonds"), Card("ace", "clubs"), Card("2", "hearts")],
    [Card("4", "clubs"), Card("2", "clubs"), Card("5", "clubs"), Card("7", "clubs"), Card("3", "clubs"), Card("7", "diamonds"), Card("7", "hearts")],
    [Card("4", "clubs"), Card("2", "clubs"), Card("5", "clubs"), Card("7", "clubs"), Card("3", "clubs"), Card("ace", "diamonds"), Card("3", "diamonds")],
    [Card("4", "clubs"), Card("8", "clubs"), Card("5", "clubs"), Card("7", "clubs"), Card("9", "clubs"), Card("2", "clubs"), Card("3", "clubs")],
    [Card("king", "clubs"), Card("king", "diamonds"), Card("king", "hearts"), Card("4", "clubs"), Card("4", "diamonds"), Card("ace", "diamonds"), Card("queen", "diamonds")],
    [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("2", "spades"), Card("ace", "clubs"), Card("king", "clubs"), Card("queen", "clubs")],
    [Card("2", "clubs"), Card("2", "diamonds"), Card("2", "hearts"), Card("2", "spades"), Card("ace", "clubs"), Card("king", "clubs"), Card("king", "diamonds")],
    [Card("4", "clubs"), Card("6", "clubs"), Card("5", "clubs"), Card("7", "clubs"), Card("3", "clubs"), Card("7", "diamonds"), Card("7", "hearts")],
    [Card("4", "clubs"), Card("6", "clubs"), Card("5", "clubs"), Card("7", "clubs"), Card("3", "clubs"), Card("9", "clubs"), Card("10", "clubs")],    
    [Card("8", "clubs"), Card("6", "clubs"), Card("5", "clubs"), Card("7", "clubs"), Card("9", "clubs"), Card("4", "clubs"), Card("3", "clubs")]]
    for hand in hands:
        extraCard1 = hand[5]
        extraCard2 = hand[6]
        random.shuffle(hand)
        assert extraCard1 not in bestHand(hand) and extraCard2 not in bestHand(hand)
    print("Best Hand Successfully Tested")
    
def testHasAPairEfficiency():
    hand = randomFiveCardHand([])
    start = time.time()
    hasAPair(hand)
    end = time.time()
    print((end-start)*1000000)

def testHasTwoPairEfficiency(hand):
    global cyberseconds
    cyberseconds = 0    
    for i in range(len(hand)-3):
        cyberseconds += 1
        for j in range(i+1, (len(hand))):
            cyberseconds += 1
            if hand[i].rank == hand[j].rank:
                myHand = hand.copy()
                myHand.remove(hand[j])
                myHand.remove(hand[i])
                if testHasAPairEfficiency(hand, called=True):
                    return True
                else:
                    return False
    return False
    
#testHasAPair()
testHasTwoPair()
#testHasThreeOfAKind()
#testHasStraight()
#testHasFlush()
#testHasFullHouse()
#testHasFourOfAKind()
#testHasStraightFlush()
#testHandValue()
#testBestHand()

#testHasAPairEfficiency()