from Card import *
from PokerCalculator import *
import os
import PIL.Image
import PIL.ImageTk
import sqlite3
        
conn = sqlite3.connect('poker.db')
cursor = conn.cursor()

def build_database():
    try:
        cursor.execute("CREATE TABLE hands (card1_rank text, card1_suit text, card2_rank text, card2_suit text, probability real)")
    except sqlite3.OperationalError:
        print("Warning: Erasing all data from hands and rebuilding the database will likely take several days. If you still wish to do this, type 'y' and press Enter")
        consent = input()
        if consent.startswith('y'):
            cursor.execute("DELETE FROM hands")
        else:
            return
    for i in range(len(deck)):
        for j in range(i+1, len(deck)):
            myHand = [deck[i], deck[j]]
            victories = 0.0
            cursor.execute("SELECT * FROM hands")
            already_calculated = False
            for hand in cursor.fetchall():
                card1 = Card(hand[0], hand[1])
                card2 = Card(hand[2], hand[3])
                if areSimilar(myHand, [card1, card2]):
                    cursor.execute("INSERT INTO hands VALUES (:c1_val, :c1_suit, :c2_val, :c2_suit, :prob)", {'c1_val':deck[i].rank, 'c1_suit':deck[i].suit,'c2_val':deck[j].rank,'c2_suit':deck[j].suit,'prob':hand[4]})
                    already_calculated = True
            if not already_calculated:
                for k in range(10000):
                    oppHand = randomTwoCardHand(myHand)
                    flop = randomFiveCardHands(myHand + oppHand, 1)[0]
                    if wins(myHand, oppHand, flop):
                        victories += 1.0
                prob = victories / 10000.0
                cursor.execute("INSERT INTO hands VALUES (:c1_val, :c1_suit, :c2_val, :c2_suit, :prob)", {'c1_val':deck[i].rank, 'c1_suit':deck[i].suit,'c2_val':deck[j].rank,'c2_suit':deck[j].suit,'prob':prob})
            print(deck[i].rank + " of " + deck[i].suit + " and " + deck[j].rank + " of " + deck[j].suit + " wins " + str(prob*100) + "% of the time")
    conn.commit()
    conn.close()
    
def build_three_card_database():
    try:
        cursor.execute("CREATE TABLE threeHands (card1_rank text, card1_suit text, card2_rank text, card2_suit text, card3_rank text, card3_suit text)")
    except sqlite3.OperationalError:
        pass
    for i in range(len(deck)):
        for j in range(i+1, len(deck)):
            for k in range(j+1, len(deck)):
                cursor.execute("INSERT INTO threeHands VALUES (:c1_val, :c1_suit, :c2_val, :c2_suit, :c3_val, :c3_suit)", {'c1_val':deck[i].rank, 'c1_suit':deck[i].suit, 'c2_val':deck[j].rank, 'c2_suit':deck[j].suit, 'c3_val':deck[k].rank, 'c3_suit':deck[k].suit})
    conn.commit()
    conn.close()
    
def resize_image(image, scaleBy):
    im = PIL.Image.open(image)
    file = os.path.splitext(image)
    im.thumbnail((round(im.size[0]/scaleBy), round(im.size[1]/scaleBy)))
    im.save('{}_copy{}'.format(file[0], file[1]))
    
def matchSizes(image, tld):
    im = PIL.Image.open(image)
    width, height = im.size
    for f in os.listdir('.'):
        if f.endswith(tld):  
            myImage = PIL.Image.open(f)
            file = os.path.splitext(f)
            myImage.thumbnail((width, height))
            myImage.save('{}_copy{}'.format(file[0], tld))
            os.remove(f)
            os.replace('{}_copy{}'.format(file[0], tld), file[0]+tld)

matchSizes('back_of_card.jpeg', '.png')