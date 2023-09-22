import PIL.Image
import PIL.ImageTk

class Card:
    
    rank = ""
    suit = ""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def equals(self, myCard):
        if self.rank == myCard.rank and self.suit == myCard.suit:
            return True
        return False    
    
    def getImage(self):
        return PIL.ImageTk.PhotoImage(PIL.Image.open(self.rank + "_of_" + self.suit + ".jpeg"))
    
    def getNumericalValue(self):
        try:
            return int(self.rank) - 1
        except ValueError:
            if self.rank == "jack":
                return 10
            elif self.rank == "queen":
                return 11
            elif self.rank == "king":
                return 12
            else:
                return 13    