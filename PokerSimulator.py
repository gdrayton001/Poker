from Card import Card
from tkinter import *
from PokerCalculator import *
import random
import sqlite3

root = Tk()
root.title("Poker Probability Calculator")

conn = sqlite3.connect('poker.db')
cursor = conn.cursor()

def calculate_odds(card1, card2):
    global odds_of_flush_label
    global odds_of_four_of_a_kind_label
    global odds_of_full_house_label
    global odds_of_pair_label
    global odds_of_straight_flush_label
    global odds_of_straight_label
    global odds_of_three_of_a_kind_label
    global odds_of_two_pair_label
    pairs = 0
    twoPairs = 0
    threesOfAKind = 0
    straights = 0
    flushes = 0
    fullHouses = 0
    foursOfAKind = 0
    straightFlushes = 0
    for i in range(10000):
        hand = randomFiveCardHand([card1, card2])
        if hasStraightFlush([card1, card2] + hand):
            straightFlushes += 1
        if hasFourOfAKind([card1, card2] + hand):
            foursOfAKind += 1
        if hasFullHouse([card1, card2] + hand):
            fullHouses += 1
        if hasFlush([card1, card2] + hand):
            flushes += 1
        if hasStraight([card1, card2] + hand):
            straights += 1
        if hasThreeOfAKind([card1, card2] + hand):
            threesOfAKind += 1
        if hasTwoPair([card1, card2] + hand):
            twoPairs += 1
        if hasAPair([card1, card2] + hand):
            pairs += 1
    odds_of_pair_label = Label(root, text="The odds of a pair are about " + str((pairs/10000) * 100) + "%")
    odds_of_two_pair_label = Label(root, text="The odds of two pairs are about " + str((twoPairs/10000) * 100) + "%")
    odds_of_three_of_a_kind_label = Label(root, text="The odds of three of a kind are about " + str((threesOfAKind/10000) * 100) + "%")
    odds_of_straight_label = Label(root, text="The odds of a straight are about " + str((straights/10000) * 100) + "%")
    odds_of_flush_label = Label(root, text="The odds of a flush are about " + str((flushes/10000) * 100) + "%")
    odds_of_full_house_label = Label(root, text="The odds of a full house are about " + str((fullHouses/10000) * 100) + "%")
    odds_of_four_of_a_kind_label = Label(root, text="The odds of four of a kind are about " + str((foursOfAKind/10000) * 100) + "%")
    odds_of_straight_flush_label = Label(root, text="The odds of a straight flush are about " + str((straightFlushes/10000) * 100) + "%")
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_pair_label.grid(row=2, column=0, columnspan=6)
    odds_of_two_pair_label.grid(row=3, column=0, columnspan=6)
    odds_of_three_of_a_kind_label.grid(row=4, column=0, columnspan=6)
    odds_of_straight_label.grid(row=5, column=0, columnspan=6)
    odds_of_flush_label.grid(row=6, column=0, columnspan=6)
    odds_of_full_house_label.grid(row=7, column=0, columnspan=6)
    odds_of_four_of_a_kind_label.grid(row=8, column=0, columnspan=6)
    odds_of_straight_flush_label.grid(row=9, column=0, columnspan=6)
    exec_command_button.grid(row=10, column=0, columnspan=3)
    return_home_button.grid(row=10, column=3, columnspan=3)
    
def return_home():
    card1_rank_drop.grid_forget()
    card1_suit_drop.grid_forget()
    card2_rank_drop.grid_forget()
    card2_suit_drop.grid_forget()   
    card1_label.grid_forget()
    card1_of.grid_forget()
    card2_label.grid_forget()
    card2_of.grid_forget()
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    try:
        odds_of_flush_label.grid_forget()
        odds_of_four_of_a_kind_label.grid_forget()
        odds_of_full_house_label.grid_forget()
        odds_of_pair_label.grid_forget()
        odds_of_straight_flush_label.grid_forget()
        odds_of_straight_label.grid_forget()
        odds_of_three_of_a_kind_label.grid_forget()
        odds_of_two_pair_label.grid_forget()
    except NameError:
        pass
    try:
        odds_of_winning_label.grid_forget()
        odds_with_opps_label.grid_forget()       
    except NameError:
        pass
    try:
        num_opponents_drop.grid_forget()
        num_opponents_label.grid_forget()  
    except NameError:
        pass
    try:
        flop_card1_rank_drop.grid_forget()
        flop_card1_suit_drop.grid_forget()
        flop_card2_rank_drop.grid_forget()
        flop_card2_suit_drop.grid_forget()   
        flop_card3_rank_drop.grid_forget()
        flop_card3_suit_drop.grid_forget()
        flop_card1_label.grid_forget()
        flop_card1_of.grid_forget()
        flop_card2_label.grid_forget()
        flop_card2_of.grid_forget()
        flop_card3_label.grid_forget()
        flop_card3_of.grid_forget()  
        try:
            flop_card4_rank_drop.grid_forget()
            flop_card4_suit_drop.grid_forget()
            flop_card4_label.grid_forget()
            flop_card4_of.grid_forget()
            try:
                flop_card5_rank_drop.grid_forget()
                flop_card5_suit_drop.grid_forget()
                flop_card5_label.grid_forget()
                flop_card5_of.grid_forget()
            except NameError:
                pass
        except NameError:
            pass        
    except NameError:
        pass
    calc_init_hand_strength_button.grid(row=0, column=0)
    calc_init_hand_odds_of_winning_button.grid(row=1, column=0)
    calc_hand_and_three_flop_strength_button.grid(row=2, column=0)
    calc_hand_and_three_flop_odds_button.grid(row=3, column=0)
    calc_hand_and_four_flop_strength_button.grid(row=4, column=0)
    calc_hand_and_four_flop_odds_button.grid(row=5, column=0)
    calc_hand_and_full_flop_odds_button.grid(row=6, column=0)
    
def calculate_initial_hand_strength():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget()
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root)
    return_home_button = Button(root, text="Return Home", command=return_home)
    exec_command_button.config(text="Calculate Possibilities", command=lambda: calculate_odds(Card(card1_rank.get(), card1_suit.get()), Card(card2_rank.get(), card2_suit.get())))
    card1_label.grid(row=0, column=0, columnspan=3)
    card2_label.grid(row=0, column=3, columnspan=3)
    card1_rank_drop.grid(row=1, column=0)
    card1_of.grid(row=1, column=1)
    card1_suit_drop.grid(row=1, column=2)
    card2_rank_drop.grid(row=1, column=3)
    card2_of.grid(row=1, column=4)
    card2_suit_drop.grid(row=1, column=5)    
    exec_command_button.grid(row=2, column=0, columnspan=3)
    return_home_button.grid(row=2, column=3, columnspan=3)

def calculate_winning_odds():
    global odds_of_winning_label
    global odds_with_opps_label
    try:
        odds_of_winning_label.grid_forget()
        odds_with_opps_label.grid_forget()
    except NameError:
        pass
    cursor.execute("SELECT * FROM hands")
    card1 = Card(card1_rank.get(), card1_suit.get())
    card2 = Card(card2_rank.get(), card2_suit.get())
    for hand in cursor.fetchall():
        cardA = Card(hand[0], hand[1])
        cardB = Card(hand[2], hand[3])
        if (cardA.equals(card1) and cardB.equals(card2)) or (cardB.equals(card1) and cardA.equals(card2)):
            prob = hand[4]
            break
    odds_of_winning_label = Label(root, text="Your odds of winning against one opponent at showdown are " + str(prob*100) + "%")
    odds_with_opps_label = Label(root, text="Therefore, your odds of winning against " + str(num_opponents.get()) + " opponents at showdown are " + str(chancesOfWinning(prob, num_opponents.get())*100) + "%")
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_winning_label.grid(row=2, column=0, columnspan=12)
    odds_with_opps_label.grid(row=3, column=0, columnspan=12)
    exec_command_button.grid(row=4, column=0, columnspan=6)
    return_home_button.grid(row=4, column=6, columnspan=6)  
    
def calculate_odds_of_winning():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button 
    global num_opponents
    global num_opponents_drop
    global num_opponents_label
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root)
    return_home_button = Button(root, text="Return Home", command=return_home)
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget()    
    exec_command_button.config(text="Calculate Odds of Winning", command=calculate_winning_odds)
    num_opponents = IntVar()
    num_opponents_drop = OptionMenu(root, num_opponents, *list(range(1,9)))
    num_opponents_label = Label(root, text="Number of Opponents:")
    card1_label.grid(row=0, column=0, columnspan=5)
    card2_label.grid(row=0, column=6, columnspan=5)
    num_opponents_label.grid(row=0, column=12)
    card1_rank_drop.grid(row=1, column=0, columnspan=2)
    card1_of.grid(row=1, column=2, columnspan=2)
    card1_suit_drop.grid(row=1, column=4, columnspan=2)
    card2_rank_drop.grid(row=1, column=6, columnspan=2)
    card2_of.grid(row=1, column=8, columnspan=2)
    card2_suit_drop.grid(row=1, column=10, columnspan=2)   
    num_opponents_drop.grid(row=1, column=12, columnspan=2)
    exec_command_button.grid(row=2, column=0, columnspan=6)
    return_home_button.grid(row=2, column=6, columnspan=6)
    
def calculate_hand_three_flop_strength():
    global odds_of_flush_label
    global odds_of_four_of_a_kind_label
    global odds_of_full_house_label
    global odds_of_pair_label
    global odds_of_straight_flush_label
    global odds_of_straight_label
    global odds_of_three_of_a_kind_label
    global odds_of_two_pair_label
    hand = [Card(card1_rank.get(), card1_suit.get()), Card(card2_rank.get(), card2_suit.get())]
    flop = [Card(flop_card1_rank.get(), flop_card1_suit.get()), Card(flop_card2_rank.get(), flop_card2_suit.get()), Card(flop_card3_rank.get(), flop_card3_suit.get())]
    pairs = 0
    twoPairs = 0
    threesOfAKind = 0
    straights = 0
    flushes = 0
    fullHouses = 0
    foursOfAKind = 0
    straightFlushes = 0
    counter = 0
    for i in range(len(deck)):
        if not contains(deck[i], hand+flop):
            for j in range(i+1, len(deck)):
                if not contains(deck[j], hand+flop):
                    completeHand = hand + flop + [deck[i], deck[j]]
                    if hasAPair(completeHand):
                        pairs += 1
                    if hasTwoPair(completeHand):
                        twoPairs += 1
                    if hasThreeOfAKind(completeHand):
                        threesOfAKind += 1
                    if hasStraight(completeHand):
                        straights += 1
                    if hasFlush(completeHand):
                        flushes += 1
                    if hasFullHouse(completeHand):
                        fullHouses += 1
                    if hasFourOfAKind(completeHand):
                        foursOfAKind += 1
                    if hasStraightFlush(completeHand):
                        straightFlushes += 1
                    counter += 1
    try:
        odds_of_pair_label.config(text="Your odds of a pair are " + str((pairs/counter)*100) + "%")
        odds_of_two_pair_label.config(text="Your odds of two pairs are " + str((twoPairs/counter)*100) + "%")
        odds_of_three_of_a_kind_label.config(text="Your odds of three of a kind are " + str((threesOfAKind/counter)*100) + "%")
        odds_of_straight_label.config(text="Your odds of a straight are " + str((straights/counter)*100) + "%")
        odds_of_flush_label.config(text="Your odds of a flush are " + str((flushes/counter)*100) + "%")
        odds_of_full_house_label.config(text="Your odds of a full house are " + str((fullHouses/counter)*100) + "%")
        odds_of_four_of_a_kind_label.config(text="Your odds of four of a kind are " + str((foursOfAKind/counter)*100) + "%")
        odds_of_straight_flush_label.config(text="Your odds of a straight flush are " + str((straightFlushes/counter)*100) + "%")
    except NameError:
        odds_of_pair_label = Label(root, text="Your odds of a pair are " + str((pairs/counter)*100) + "%")
        odds_of_two_pair_label = Label(root, text="Your odds of two pairs are " + str((twoPairs/counter)*100) + "%")
        odds_of_three_of_a_kind_label = Label(root, text="Your odds of three of a kind are " + str((threesOfAKind/counter)*100) + "%")
        odds_of_straight_label = Label(root, text="Your odds of a straight are " + str((straights/counter)*100) + "%")
        odds_of_flush_label = Label(root, text="Your odds of a flush are " + str((flushes/counter)*100) + "%")
        odds_of_full_house_label = Label(root, text="Your odds of a full house are " + str((fullHouses/counter)*100) + "%")
        odds_of_four_of_a_kind_label = Label(root, text="Your odds of four of a kind are " + str((foursOfAKind/counter)*100) + "%")
        odds_of_straight_flush_label = Label(root, text="Your odds of a straight flush are " + str((straightFlushes/counter)*100) + "%")
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_pair_label.grid(row=2, column=0, columnspan=30)
    odds_of_two_pair_label.grid(row=3, column=0, columnspan=30)
    odds_of_three_of_a_kind_label.grid(row=4, column=0, columnspan=30)
    odds_of_straight_label.grid(row=5, column=0, columnspan=30)
    odds_of_flush_label.grid(row=6, column=0, columnspan=30)
    odds_of_full_house_label.grid(row=7, column=0, columnspan=30)
    odds_of_four_of_a_kind_label.grid(row=8, column=0, columnspan=30)
    odds_of_straight_flush_label.grid(row=9, column=0, columnspan=30)
    exec_command_button.grid(row=10, column=0, columnspan=15)
    return_home_button.grid(row=10, column=15, columnspan=15)    
    
def calc_init_hand_three_flop_strength():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button
    global flop_card1_rank
    global flop_card1_suit
    global flop_card2_rank
    global flop_card2_suit  
    global flop_card3_rank
    global flop_card3_suit 
    global flop_card1_rank_drop
    global flop_card1_suit_drop
    global flop_card2_rank_drop
    global flop_card2_suit_drop    
    global flop_card3_rank_drop
    global flop_card3_suit_drop
    global flop_card1_label
    global flop_card1_of
    global flop_card2_label
    global flop_card2_of
    global flop_card3_label
    global flop_card3_of       
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root)
    return_home_button = Button(root, text="Return Home", command=return_home)
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()  
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget()
    exec_command_button.config(text="Calculate Odds of Pair, Three of a Kind, etc.", command=calculate_hand_three_flop_strength)
    flop_card1_rank = StringVar()
    flop_card1_suit = StringVar()
    flop_card2_rank = StringVar()
    flop_card2_suit = StringVar()
    flop_card3_rank = StringVar()
    flop_card3_suit = StringVar()
    flop_card1_rank_drop = OptionMenu(root, flop_card1_rank, *ranks)
    flop_card1_suit_drop = OptionMenu(root, flop_card1_suit, *suits)
    flop_card2_rank_drop = OptionMenu(root, flop_card2_rank, *ranks)
    flop_card2_suit_drop = OptionMenu(root, flop_card2_suit, *suits)
    flop_card3_rank_drop = OptionMenu(root, flop_card3_rank, *ranks)
    flop_card3_suit_drop = OptionMenu(root, flop_card3_suit, *suits)
    flop_card1_label = Label(root, text="Flop Card 1:")
    flop_card1_of = Label(root, text="of")
    flop_card2_label = Label(root, text="Flop Card 2:")
    flop_card2_of = Label(root, text="of")     
    flop_card3_label = Label(root, text="Flop Card 3:")
    flop_card3_of = Label(root, text="of")   
    card1_label.grid(row=0, column=0, columnspan=6)
    card2_label.grid(row=0, column=6, columnspan=6)
    flop_card1_label.grid(row=0, column=12, columnspan=6)
    flop_card2_label.grid(row=0, column=18, columnspan=6)
    flop_card3_label.grid(row=0, column=24, columnspan=6)
    card1_rank_drop.grid(row=1, column=0, columnspan=2)
    card1_of.grid(row=1, column=2, columnspan=2)
    card1_suit_drop.grid(row=1, column=4, columnspan=2)
    card2_rank_drop.grid(row=1, column=6, columnspan=2)
    card2_of.grid(row=1, column=8, columnspan=2)
    card2_suit_drop.grid(row=1, column=10, columnspan=2)
    flop_card1_rank_drop.grid(row=1, column=12, columnspan=2)
    flop_card1_of.grid(row=1, column=14, columnspan=2)
    flop_card1_suit_drop.grid(row=1, column=16, columnspan=2)
    flop_card2_rank_drop.grid(row=1, column=18, columnspan=2)
    flop_card2_of.grid(row=1, column=20, columnspan=2)
    flop_card2_suit_drop.grid(row=1, column=22, columnspan=2)    
    flop_card3_rank_drop.grid(row=1, column=24, columnspan=2)
    flop_card3_of.grid(row=1, column=26, columnspan=2)
    flop_card3_suit_drop.grid(row=1, column=28, columnspan=2)
    exec_command_button.grid(row=2, column=0, columnspan=15)
    return_home_button.grid(row=2, column=15, columnspan=15)
    
def calculate_init_hand_three_flop_odds():
    global odds_of_winning_label
    global odds_with_opps_label 
    try:
        odds_of_winning_label.grid_forget()
        odds_with_opps_label.grid_forget()
    except NameError:
        pass
    victories = 0
    for i in range(1000):
        hand = [Card(card1_rank.get(), card1_suit.get()), Card(card2_rank.get(), card2_suit.get())]
        flop = [Card(flop_card1_rank.get(), flop_card1_suit.get()), Card(flop_card2_rank.get(), flop_card2_suit.get()), Card(flop_card3_rank.get(), flop_card3_suit.get())]
        oppHand = randomTwoCardHand(hand + flop)
        completeFlop = randomTwoCardHand(hand + flop + oppHand)
        if wins(hand, oppHand, flop + completeFlop):
            victories += 1
    odds_of_winning_label = Label(root, text="Your odds of winning against one opponent at showdown are " + str(victories/10) + "%")
    odds_with_opps_label = Label(root, text="Therefore, your odds of winning against " + str(num_opponents.get()) + " opponents at showdown are " + str(chancesOfWinning(victories/1000, num_opponents.get())*100) + "%")        
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_winning_label.grid(row=2, column=0, columnspan=18)
    odds_with_opps_label.grid(row=3, column=0, columnspan=18)
    exec_command_button.grid(row=4, column=0, columnspan=9)
    return_home_button.grid(row=4, column=9, columnspan=9)
    
def calc_init_hand_three_flop_odds():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button
    global flop_card1_rank
    global flop_card1_suit
    global flop_card2_rank
    global flop_card2_suit  
    global flop_card3_rank
    global flop_card3_suit 
    global flop_card1_rank_drop
    global flop_card1_suit_drop
    global flop_card2_rank_drop
    global flop_card2_suit_drop    
    global flop_card3_rank_drop
    global flop_card3_suit_drop
    global flop_card1_label
    global flop_card1_of
    global flop_card2_label
    global flop_card2_of
    global flop_card3_label
    global flop_card3_of 
    global num_opponents
    global num_opponents_drop
    global num_opponents_label    
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root, text="Calculate Odds of Winning", command=calculate_init_hand_three_flop_odds)
    return_home_button = Button(root, text="Return Home", command=return_home)
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()  
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget() 
    flop_card1_rank = StringVar()
    flop_card1_suit = StringVar()
    flop_card2_rank = StringVar()
    flop_card2_suit = StringVar()
    flop_card3_rank = StringVar()
    flop_card3_suit = StringVar()
    flop_card1_rank_drop = OptionMenu(root, flop_card1_rank, *ranks)
    flop_card1_suit_drop = OptionMenu(root, flop_card1_suit, *suits)
    flop_card2_rank_drop = OptionMenu(root, flop_card2_rank, *ranks)
    flop_card2_suit_drop = OptionMenu(root, flop_card2_suit, *suits)
    flop_card3_rank_drop = OptionMenu(root, flop_card3_rank, *ranks)
    flop_card3_suit_drop = OptionMenu(root, flop_card3_suit, *suits)
    flop_card1_label = Label(root, text="Flop Card 1:")
    flop_card1_of = Label(root, text="of")
    flop_card2_label = Label(root, text="Flop Card 2:")
    flop_card2_of = Label(root, text="of")     
    flop_card3_label = Label(root, text="Flop Card 3:")
    flop_card3_of = Label(root, text="of")
    num_opponents = IntVar()
    num_opponents_drop = OptionMenu(root, num_opponents, *list(range(1,9)))
    num_opponents_label = Label(root, text="Number of Opponents:")
    card1_label.grid(row=0, column=0, columnspan=3)
    card2_label.grid(row=0, column=3, columnspan=3)
    flop_card1_label.grid(row=0, column=6, columnspan=3)
    flop_card2_label.grid(row=0, column=9, columnspan=3)
    flop_card3_label.grid(row=0, column=12, columnspan=3)
    num_opponents_label.grid(row=0, column=15, columnspan=3)
    card1_rank_drop.grid(row=1, column=0)
    card1_of.grid(row=1, column=1)
    card1_suit_drop.grid(row=1, column=2)
    card2_rank_drop.grid(row=1, column=3)
    card2_of.grid(row=1, column=4)
    card2_suit_drop.grid(row=1, column=5)  
    flop_card1_rank_drop.grid(row=1, column=6)
    flop_card1_of.grid(row=1, column=7)
    flop_card1_suit_drop.grid(row=1, column=8)
    flop_card2_rank_drop.grid(row=1, column=9)
    flop_card2_of.grid(row=1, column=10)
    flop_card2_suit_drop.grid(row=1, column=11)
    flop_card3_rank_drop.grid(row=1, column=12)
    flop_card3_of.grid(row=1, column=13)
    flop_card3_suit_drop.grid(row=1, column=14)
    num_opponents_drop.grid(row=1, column=15, columnspan=3)
    exec_command_button.grid(row=2, column=0, columnspan=9)
    return_home_button.grid(row=2, column=9, columnspan=9)
    
def calculate_init_hand_four_flop_strength():
    global odds_of_flush_label
    global odds_of_four_of_a_kind_label
    global odds_of_full_house_label
    global odds_of_pair_label
    global odds_of_straight_flush_label
    global odds_of_straight_label
    global odds_of_three_of_a_kind_label
    global odds_of_two_pair_label
    hand = [Card(card1_rank.get(), card1_suit.get()), Card(card2_rank.get(), card2_suit.get())]
    flop = [Card(flop_card1_rank.get(), flop_card1_suit.get()), Card(flop_card2_rank.get(), flop_card2_suit.get()), Card(flop_card3_rank.get(), flop_card3_suit.get()), Card(flop_card4_rank.get(), flop_card4_suit.get())]
    straightFlushes = 0
    foursOfAKind = 0
    fullHouses = 0
    flushes = 0
    straights = 0
    threesOfAKind = 0
    twoPairs = 0
    pairs = 0
    for card in deck:
        if not contains(card, hand+flop):
            if hasStraightFlush(hand+flop+[card]):
                straightFlushes += 1
            if hasFourOfAKind(hand+flop+[card]):
                foursOfAKind += 1
            if hasFullHouse(hand+flop+[card]):
                fullHouses += 1
            if hasFlush(hand+flop+[card]):
                flushes += 1
            if hasStraight(hand+flop+[card]):
                straights += 1
            if hasThreeOfAKind(hand+flop+[card]):
                threesOfAKind += 1
            if hasTwoPair(hand+flop+[card]):
                twoPairs += 1
            if hasAPair(hand+flop+[card]):
                pairs += 1
    try:
        odds_of_pair_label.config(text="Your odds of a pair are " + str((pairs/46)*100) + "%")
        odds_of_two_pair_label.config(text="Your odds of two pairs are " + str((twoPairs/46)*100) + "%")
        odds_of_three_of_a_kind_label.config(text="Your odds of three of a kind are " + str((threesOfAKind/46)*100) + "%")
        odds_of_straight_label.config(text="Your odds of a straight are " + str((straights/46)*100) + "%")
        odds_of_flush_label.config(text="Your odds of a flush are " + str((flushes/46)*100) + "%")
        odds_of_full_house_label.config(text="Your odds of a full house are " + str((fullHouses/46)*100) + "%")
        odds_of_four_of_a_kind_label.config(text="Your odds of four of a kind are " + str((foursOfAKind/46)*100) + "%")
        odds_of_straight_flush_label.config(text="Your odds of a straight flush are " + str((straightFlushes/46)*100) + "%")
    except NameError:
        odds_of_pair_label = Label(root, text="Your odds of a pair are " + str((pairs/46)*100) + "%")
        odds_of_two_pair_label = Label(root, text="Your odds of two pairs are " + str((twoPairs/46)*100) + "%")
        odds_of_three_of_a_kind_label = Label(root, text="Your odds of three of a kind are " + str((threesOfAKind/46)*100) + "%")
        odds_of_straight_label = Label(root, text="Your odds of a straight are " + str((straights/46)*100) + "%")
        odds_of_flush_label = Label(root, text="Your odds of a flush are " + str((flushes/46)*100) + "%")
        odds_of_full_house_label = Label(root, text="Your odds of a full house are " + str((fullHouses/46)*100) + "%")
        odds_of_four_of_a_kind_label = Label(root, text="Your odds of four of a kind are " + str((foursOfAKind/46)*100) + "%")
        odds_of_straight_flush_label = Label(root, text="Your odds of a straight flush are " + str((straightFlushes/46)*100) + "%")
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_pair_label.grid(row=2, column=0, columnspan=18)
    odds_of_two_pair_label.grid(row=3, column=0, columnspan=18)
    odds_of_three_of_a_kind_label.grid(row=4, column=0, columnspan=18)
    odds_of_straight_label.grid(row=5, column=0, columnspan=18)
    odds_of_flush_label.grid(row=6, column=0, columnspan=18)
    odds_of_full_house_label.grid(row=7, column=0, columnspan=18)
    odds_of_four_of_a_kind_label.grid(row=8, column=0, columnspan=18)
    odds_of_straight_flush_label.grid(row=9, column=0, columnspan=18)
    exec_command_button.grid(row=10, column=0, columnspan=9)
    return_home_button.grid(row=10, column=9, columnspan=9)     
    
def calc_init_hand_four_flop_strength():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button
    global flop_card1_rank
    global flop_card1_suit
    global flop_card2_rank
    global flop_card2_suit  
    global flop_card3_rank
    global flop_card3_suit 
    global flop_card1_rank_drop
    global flop_card1_suit_drop
    global flop_card2_rank_drop
    global flop_card2_suit_drop    
    global flop_card3_rank_drop
    global flop_card3_suit_drop
    global flop_card1_label
    global flop_card1_of
    global flop_card2_label
    global flop_card2_of
    global flop_card3_label
    global flop_card3_of 
    global num_opponents
    global flop_card4_rank
    global flop_card4_suit
    global flop_card4_rank_drop
    global flop_card4_suit_drop 
    global flop_card4_label
    global flop_card4_of  
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root, text="Calculate Odds of Pair, Three of a Kind, etc.", command=calculate_init_hand_four_flop_strength)
    return_home_button = Button(root, text="Return Home", command=return_home)
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()  
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget()    
    flop_card1_rank = StringVar()
    flop_card1_suit = StringVar()
    flop_card2_rank = StringVar()
    flop_card2_suit = StringVar()
    flop_card3_rank = StringVar()
    flop_card3_suit = StringVar()
    flop_card4_rank = StringVar()
    flop_card4_suit = StringVar()    
    flop_card1_rank_drop = OptionMenu(root, flop_card1_rank, *ranks)
    flop_card1_suit_drop = OptionMenu(root, flop_card1_suit, *suits)
    flop_card2_rank_drop = OptionMenu(root, flop_card2_rank, *ranks)
    flop_card2_suit_drop = OptionMenu(root, flop_card2_suit, *suits)
    flop_card3_rank_drop = OptionMenu(root, flop_card3_rank, *ranks)
    flop_card3_suit_drop = OptionMenu(root, flop_card3_suit, *suits)
    flop_card4_rank_drop = OptionMenu(root, flop_card4_rank, *ranks)
    flop_card4_suit_drop = OptionMenu(root, flop_card4_suit, *suits)    
    flop_card1_label = Label(root, text="Flop Card 1:")
    flop_card1_of = Label(root, text="of")
    flop_card2_label = Label(root, text="Flop Card 2:")
    flop_card2_of = Label(root, text="of")     
    flop_card3_label = Label(root, text="Flop Card 3:")
    flop_card3_of = Label(root, text="of")
    flop_card4_label = Label(root, text="Flop Card 4:")
    flop_card4_of = Label(root, text="of")    
    card1_label.grid(row=0, column=0, columnspan=3)
    card2_label.grid(row=0, column=3, columnspan=3)
    flop_card1_label.grid(row=0, column=6, columnspan=3)
    flop_card2_label.grid(row=0, column=9, columnspan=3)
    flop_card3_label.grid(row=0, column=12, columnspan=3)
    flop_card4_label.grid(row=0, column=15, columnspan=3)
    card1_rank_drop.grid(row=1, column=0)
    card1_of.grid(row=1, column=1)
    card1_suit_drop.grid(row=1, column=2)
    card2_rank_drop.grid(row=1, column=3)
    card2_of.grid(row=1, column=4)
    card2_suit_drop.grid(row=1, column=5)
    flop_card1_rank_drop.grid(row=1, column=6)
    flop_card1_of.grid(row=1, column=7)
    flop_card1_suit_drop.grid(row=1, column=8)
    flop_card2_rank_drop.grid(row=1, column=9)
    flop_card2_of.grid(row=1, column=10)
    flop_card2_suit_drop.grid(row=1, column=11)
    flop_card3_rank_drop.grid(row=1, column=12)
    flop_card3_of.grid(row=1, column=13)
    flop_card3_suit_drop.grid(row=1, column=14)
    flop_card4_rank_drop.grid(row=1, column=15)
    flop_card4_of.grid(row=1, column=16)
    flop_card4_suit_drop.grid(row=1, column=17)
    exec_command_button.grid(row=2, column=0, columnspan=9)
    return_home_button.grid(row=2, column=9, columnspan=9)
    
def calculate_init_hand_four_flop_odds():
    global odds_of_winning_label
    global odds_with_opps_label 
    try:
        odds_of_winning_label.grid_forget()
        odds_with_opps_label.grid_forget()
    except NameError:
        pass
    victories = 0
    hand = [Card(card1_rank.get(), card1_suit.get()), Card(card2_rank.get(), card2_suit.get())]
    flop = [Card(flop_card1_rank.get(), flop_card1_suit.get()), Card(flop_card2_rank.get(), flop_card2_suit.get()), Card(flop_card3_rank.get(), flop_card3_suit.get()), Card(flop_card4_rank.get(), flop_card4_suit.get())]
    cursor.execute("SELECT * FROM threeHands")
    hands = cursor.fetchall()
    for i in range(1000):
        threeHand = random.choice(hands)
        oppHand = [Card(threeHand[0], threeHand[1]), Card(threeHand[2], threeHand[3]), Card(threeHand[4], threeHand[5])]
        while not canCoexist(hand+flop, oppHand):
            threeHand = random.choice(hands)
            oppHand = [Card(threeHand[0], threeHand[1]), Card(threeHand[2], threeHand[3]), Card(threeHand[4], threeHand[5])]
        lastCard = random.choice(oppHand)
        oppHand.remove(lastCard)
        if wins(hand, oppHand, flop+[lastCard]):
            victories += 1
    odds_of_winning_label = Label(root, text="Your odds of winning against one opponent at showdown are " + str((victories/1000)*100) + "%")
    odds_with_opps_label = Label(root, text="Therefore, your odds of winning against " + str(num_opponents.get()) + " opponents at showdown are " + str(chancesOfWinning(victories/1000, num_opponents.get())*100) + "%")
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_winning_label.grid(row=2, column=0, columnspan=42)
    odds_with_opps_label.grid(row=3, column=0, columnspan=42)
    exec_command_button.grid(row=4, column=0, columnspan=21)
    return_home_button.grid(row=4, column=21, columnspan=21)
    
def calc_init_hand_four_flop_odds():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button
    global flop_card1_rank
    global flop_card1_suit
    global flop_card2_rank
    global flop_card2_suit  
    global flop_card3_rank
    global flop_card3_suit 
    global flop_card1_rank_drop
    global flop_card1_suit_drop
    global flop_card2_rank_drop
    global flop_card2_suit_drop    
    global flop_card3_rank_drop
    global flop_card3_suit_drop
    global flop_card1_label
    global flop_card1_of
    global flop_card2_label
    global flop_card2_of
    global flop_card3_label
    global flop_card3_of 
    global flop_card4_rank
    global flop_card4_suit
    global flop_card4_rank_drop
    global flop_card4_suit_drop 
    global flop_card4_label
    global flop_card4_of
    global num_opponents_label
    global num_opponents
    global num_opponents_drop
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root, text="Calculate Odds of Winning", command=calculate_init_hand_four_flop_odds)
    return_home_button = Button(root, text="Return Home", command=return_home)
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()  
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget() 
    flop_card1_rank = StringVar()
    flop_card1_suit = StringVar()
    flop_card2_rank = StringVar()
    flop_card2_suit = StringVar()
    flop_card3_rank = StringVar()
    flop_card3_suit = StringVar()
    flop_card4_rank = StringVar()
    flop_card4_suit = StringVar()    
    flop_card1_rank_drop = OptionMenu(root, flop_card1_rank, *ranks)
    flop_card1_suit_drop = OptionMenu(root, flop_card1_suit, *suits)
    flop_card2_rank_drop = OptionMenu(root, flop_card2_rank, *ranks)
    flop_card2_suit_drop = OptionMenu(root, flop_card2_suit, *suits)
    flop_card3_rank_drop = OptionMenu(root, flop_card3_rank, *ranks)
    flop_card3_suit_drop = OptionMenu(root, flop_card3_suit, *suits)
    flop_card4_rank_drop = OptionMenu(root, flop_card4_rank, *ranks)
    flop_card4_suit_drop = OptionMenu(root, flop_card4_suit, *suits)    
    flop_card1_label = Label(root, text="Flop Card 1:")
    flop_card1_of = Label(root, text="of")
    flop_card2_label = Label(root, text="Flop Card 2:")
    flop_card2_of = Label(root, text="of")     
    flop_card3_label = Label(root, text="Flop Card 3:")
    flop_card3_of = Label(root, text="of")
    flop_card4_label = Label(root, text="Flop Card 4:")
    flop_card4_of = Label(root, text="of")  
    num_opponents = IntVar()
    num_opponents_drop = OptionMenu(root, num_opponents, *list(range(1,9)))
    num_opponents_label = Label(root, text="Number of Opponents:")
    card1_label.grid(row=0, column=0, columnspan=6)
    card2_label.grid(row=0, column=6, columnspan=6)
    flop_card1_label.grid(row=0, column=12, columnspan=6)
    flop_card2_label.grid(row=0, column=18, columnspan=6)
    flop_card3_label.grid(row=0, column=24, columnspan=6)
    flop_card4_label.grid(row=0, column=30, columnspan=6)
    num_opponents_label.grid(row=0, column=36, columnspan=6)
    card1_rank_drop.grid(row=1, column=0, columnspan=2)
    card1_of.grid(row=1, column=2, columnspan=2)
    card1_suit_drop.grid(row=1, column=4, columnspan=2)
    card2_rank_drop.grid(row=1, column=6, columnspan=2)
    card2_of.grid(row=1, column=8, columnspan=2)
    card2_suit_drop.grid(row=1, column=10, columnspan=2)
    flop_card1_rank_drop.grid(row=1, column=12, columnspan=2)
    flop_card1_of.grid(row=1, column=14, columnspan=2)
    flop_card1_suit_drop.grid(row=1, column=16, columnspan=2)
    flop_card2_rank_drop.grid(row=1, column=18, columnspan=2)
    flop_card2_of.grid(row=1, column=20, columnspan=2)
    flop_card2_suit_drop.grid(row=1, column=22, columnspan=2)
    flop_card3_rank_drop.grid(row=1, column=24, columnspan=2)
    flop_card3_of.grid(row=1, column=26, columnspan=2)
    flop_card3_suit_drop.grid(row=1, column=28, columnspan=2)
    flop_card4_rank_drop.grid(row=1, column=30, columnspan=2)
    flop_card4_of.grid(row=1, column=32, columnspan=2)
    flop_card4_suit_drop.grid(row=1, column=34, columnspan=2)
    num_opponents_drop.grid(row=1, column=36, columnspan=6)
    exec_command_button.grid(row=2, column=0, columnspan=21)
    return_home_button.grid(row=2, column=21, columnspan=21)
    
def calculate_init_hand_full_flop_odds():
    global odds_of_winning_label
    global odds_with_opps_label 
    try:
        odds_of_winning_label.grid_forget()
        odds_with_opps_label.grid_forget()
    except NameError:
        pass
    hand = [Card(card1_rank.get(), card1_suit.get()), Card(card2_rank.get(), card2_suit.get())]
    flop = [Card(flop_card1_rank.get(), flop_card1_suit.get()), Card(flop_card2_rank.get(), flop_card2_suit.get()), Card(flop_card3_rank.get(), flop_card3_suit.get()), Card(flop_card4_rank.get(), flop_card4_suit.get()), Card(flop_card5_rank.get(), flop_card5_suit.get())] 
    victories = 0
    for i in range(len(deck)):
        for j in range(i+1, len(deck)):
            oppHand = [deck[i], deck[j]]
            if canCoexist(oppHand, hand+flop):
                if wins(hand, oppHand, flop):
                    victories += 1
    odds_of_winning_label = Label(root, text="Your odds of winning against one opponent at showdown are " + str((victories/990)*100) + "%")
    odds_with_opps_label = Label(root, text="Therefore, your odds of winning against " + str(num_opponents.get()) + " opponents at showdown are " + str(chancesOfWinning(victories/990, num_opponents.get())*100) + "%")
    exec_command_button.grid_forget()
    return_home_button.grid_forget()
    odds_of_winning_label.grid(row=2, column=0, columnspan=24)
    odds_with_opps_label.grid(row=3, column=0, columnspan=24)
    exec_command_button.grid(row=4, column=0, columnspan=24)
    return_home_button.grid(row=4, column=9, columnspan=24)    
    
def calc_init_hand_full_flop_odds():
    global card1_rank
    global card1_suit
    global card2_rank
    global card2_suit
    global card1_rank_drop
    global card1_suit_drop
    global card2_rank_drop
    global card2_suit_drop
    global card1_label
    global card1_of
    global card2_label
    global card2_of
    global exec_command_button
    global return_home_button
    global flop_card1_rank
    global flop_card1_suit
    global flop_card2_rank
    global flop_card2_suit  
    global flop_card3_rank
    global flop_card3_suit 
    global flop_card1_rank_drop
    global flop_card1_suit_drop
    global flop_card2_rank_drop
    global flop_card2_suit_drop    
    global flop_card3_rank_drop
    global flop_card3_suit_drop
    global flop_card1_label
    global flop_card1_of
    global flop_card2_label
    global flop_card2_of
    global flop_card3_label
    global flop_card3_of 
    global flop_card4_rank
    global flop_card4_suit
    global flop_card4_rank_drop
    global flop_card4_suit_drop 
    global flop_card4_label
    global flop_card4_of
    global flop_card5_rank
    global flop_card5_suit
    global flop_card5_rank_drop
    global flop_card5_suit_drop 
    global flop_card5_label
    global flop_card5_of    
    global num_opponents_label
    global num_opponents
    global num_opponents_drop
    card1_rank = StringVar()
    card1_suit = StringVar()
    card2_rank = StringVar()
    card2_suit = StringVar()
    card1_rank_drop = OptionMenu(root, card1_rank, *ranks)
    card1_suit_drop = OptionMenu(root, card1_suit, *suits)
    card2_rank_drop = OptionMenu(root, card2_rank, *ranks)
    card2_suit_drop = OptionMenu(root, card2_suit, *suits)
    card1_label = Label(root, text="Card 1:")
    card1_of = Label(root, text="of")
    card2_label = Label(root, text="Card 2:")
    card2_of = Label(root, text="of")   
    exec_command_button = Button(root, text="Calculate Odds of Winning", command=calculate_init_hand_full_flop_odds)
    return_home_button = Button(root, text="Return Home", command=return_home)
    calc_init_hand_strength_button.grid_forget()
    calc_init_hand_odds_of_winning_button.grid_forget()
    calc_hand_and_three_flop_strength_button.grid_forget()  
    calc_hand_and_three_flop_odds_button.grid_forget()
    calc_hand_and_four_flop_strength_button.grid_forget()
    calc_hand_and_four_flop_odds_button.grid_forget()
    calc_hand_and_full_flop_odds_button.grid_forget() 
    flop_card1_rank = StringVar()
    flop_card1_suit = StringVar()
    flop_card2_rank = StringVar()
    flop_card2_suit = StringVar()
    flop_card3_rank = StringVar()
    flop_card3_suit = StringVar()
    flop_card4_rank = StringVar()
    flop_card4_suit = StringVar()    
    flop_card5_rank = StringVar()
    flop_card5_suit = StringVar()      
    flop_card1_rank_drop = OptionMenu(root, flop_card1_rank, *ranks)
    flop_card1_suit_drop = OptionMenu(root, flop_card1_suit, *suits)
    flop_card2_rank_drop = OptionMenu(root, flop_card2_rank, *ranks)
    flop_card2_suit_drop = OptionMenu(root, flop_card2_suit, *suits)
    flop_card3_rank_drop = OptionMenu(root, flop_card3_rank, *ranks)
    flop_card3_suit_drop = OptionMenu(root, flop_card3_suit, *suits)
    flop_card4_rank_drop = OptionMenu(root, flop_card4_rank, *ranks)
    flop_card4_suit_drop = OptionMenu(root, flop_card4_suit, *suits)    
    flop_card5_rank_drop = OptionMenu(root, flop_card5_rank, *ranks)
    flop_card5_suit_drop = OptionMenu(root, flop_card5_suit, *suits)
    flop_card1_label = Label(root, text="Flop Card 1:")
    flop_card1_of = Label(root, text="of")
    flop_card2_label = Label(root, text="Flop Card 2:")
    flop_card2_of = Label(root, text="of")     
    flop_card3_label = Label(root, text="Flop Card 3:")
    flop_card3_of = Label(root, text="of")
    flop_card4_label = Label(root, text="Flop Card 4:")
    flop_card4_of = Label(root, text="of")  
    flop_card5_label = Label(root, text="Flop Card 5:")
    flop_card5_of = Label(root, text="of")      
    num_opponents = IntVar()
    num_opponents_drop = OptionMenu(root, num_opponents, *list(range(1,9)))
    num_opponents_label = Label(root, text="Number of Opponents:")
    card1_label.grid(row=0, column=0, columnspan=3)
    card2_label.grid(row=0, column=3, columnspan=3)
    flop_card1_label.grid(row=0, column=6, columnspan=3)
    flop_card2_label.grid(row=0, column=9, columnspan=3)
    flop_card3_label.grid(row=0, column=12, columnspan=3)
    flop_card4_label.grid(row=0, column=15, columnspan=3)
    flop_card5_label.grid(row=0, column=18, columnspan=3)
    num_opponents_label.grid(row=0, column=21, columnspan=3)
    card1_rank_drop.grid(row=1, column=0)
    card1_of.grid(row=1, column=1)
    card1_suit_drop.grid(row=1, column=2)
    card2_rank_drop.grid(row=1, column=3)
    card2_of.grid(row=1, column=4)
    card2_suit_drop.grid(row=1, column=5)
    flop_card1_rank_drop.grid(row=1, column=6)
    flop_card1_of.grid(row=1, column=7)
    flop_card1_suit_drop.grid(row=1, column=8)
    flop_card2_rank_drop.grid(row=1, column=9)
    flop_card2_of.grid(row=1, column=10)
    flop_card2_suit_drop.grid(row=1, column=11)
    flop_card3_rank_drop.grid(row=1, column=12)
    flop_card3_of.grid(row=1, column=13)
    flop_card3_suit_drop.grid(row=1, column=14)
    flop_card4_rank_drop.grid(row=1, column=15)
    flop_card4_of.grid(row=1, column=16)
    flop_card4_suit_drop.grid(row=1, column=17)
    flop_card5_rank_drop.grid(row=1, column=18)
    flop_card5_of.grid(row=1, column=19)
    flop_card5_suit_drop.grid(row=1, column=20)    
    num_opponents_drop.grid(row=1, column=21, columnspan=3)
    exec_command_button.grid(row=2, column=0, columnspan=12)
    return_home_button.grid(row=2, column=12, columnspan=12)    
    
def display_window():
    global calc_init_hand_strength_button
    global calc_init_hand_odds_of_winning_button
    global calc_hand_and_three_flop_strength_button
    global calc_hand_and_three_flop_odds_button
    global calc_hand_and_four_flop_strength_button
    global calc_hand_and_four_flop_odds_button
    global calc_hand_and_full_flop_odds_button
    calc_init_hand_strength_button = Button(root, text="Calculate Odds of Getting Pair, Three of a Kind, Flush, etc. Using Initial Two Card Hand", command=calculate_initial_hand_strength)
    calc_init_hand_odds_of_winning_button = Button(root, text="Calculate Odds of Winning Round Using Initial Two Card Hand", command=calculate_odds_of_winning)
    calc_hand_and_three_flop_strength_button = Button(root, text="Calculate Odds of Getting Pair, Three of a Kind, Flush, etc. Using Initial Two Card Hand and Three Card Flop", command=calc_init_hand_three_flop_strength)
    calc_hand_and_three_flop_odds_button = Button(root, text="Calculate Odds of Winning Round Using Initial Two Card Hand and Three Card Flop", command=calc_init_hand_three_flop_odds)
    calc_hand_and_four_flop_strength_button = Button(root, text="Calculate Odds of Getting Pair, Three of a Kind, Flush, etc. Using Initial Two Card Hand and Four Card Flop", command=calc_init_hand_four_flop_strength)
    calc_hand_and_four_flop_odds_button = Button(root, text="Calculate Odds of Winning Round Using Initial Two Card Hand and Four Card Flop", command=calc_init_hand_four_flop_odds)
    calc_hand_and_full_flop_odds_button = Button(root, text="Calculate Odds of Winning Round Using Initial Two Card Hand and Full Five Card Flop", command=calc_init_hand_full_flop_odds)
    calc_init_hand_strength_button.grid(row=0, column=0)
    calc_init_hand_odds_of_winning_button.grid(row=1, column=0)
    calc_hand_and_three_flop_strength_button.grid(row=2, column=0)
    calc_hand_and_three_flop_odds_button.grid(row=3, column=0)
    calc_hand_and_four_flop_strength_button.grid(row=4, column=0)
    calc_hand_and_four_flop_odds_button.grid(row=5, column=0)
    calc_hand_and_full_flop_odds_button.grid(row=6, column=0)
    root.mainloop()

display_window()