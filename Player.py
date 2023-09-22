from tkinter import *
import PIL.Image
import PIL.ImageTk

class Player:
    
    order = 0
    label = None
    chips = 0
    active = False
    hand = []
    isCPU = False
    betting = 0
    bettingIcon = None
    name = ""
    chip_image_label = None
    eligibleToWin = 0
    lost = False
    
    def __init__(self, order, label, root):
        self.order = order
        self.label = Label(root, text=label + '\n chips: ' + str(self.chips - self.betting))
        self.name = label
        self.bettingIcon = Label(root, text=str(self.betting)) 
        
    def activate(self):
        if self.lost:
            raise Exception("Cannot activate eliminated player")
        self.active = True  
        self.label.config(fg="black") 
        
    def bet(self, amount):
        if self.lost:
            raise Exception("Eliminated player cannot bet")
        if amount > self.chips - self.betting:
            raise Exception('Player cannot bet more chips than they have')
        self.betting += amount
        self.bettingIcon.config(text=str(self.betting))
        self.label.config(text=self.name + '\n chips: ' + str(self.chips - self.betting))    
        
    def clearHand(self):
        self.hand = []    
        
    def createChipImage(self, root):
        if self.lost:
            raise Exception("Cannot create chip image for eliminated player")        
        chip_image = PIL.ImageTk.PhotoImage(PIL.Image.open("poker_chips.png"))
        self.chip_image_label = Label(root, image=chip_image) 
        self.chip_image_label.image = chip_image      
        
    def deal(self, cards):
        if self.lost:
            raise Exception("Cannot deal cards to eliminated player")        
        if len(self.hand) >= 2:
            raise Exception('Player already has two cards')
        self.hand = cards 
        self.originalAmount = self.chips
        
    def deleteChipImage(self):
        try:
            self.chip_image_label.grid_forget()
        except AttributeError:
            pass    
        
    def eliminate(self):
        self.lost = True
        self.active = False
        self.label.config(fg="gray")         
        
    def fold(self):
        if self.lost:
            raise Exception("Cannot fold eliminated player")        
        self.active = False
        self.label.config(fg="gray")  
        
    def resetBet(self):
        self.betting = 0    
                                 
    def setChips(self, chips):
        if self.lost:
            raise Exception("Cannot set chips for eliminated player")        
        self.chips += chips 
        self.label.config(text=self.name + '\n chips: ' + str(self.chips - self.betting))  
        
    def setEligibleToWin(self, amount):
        if self.lost:
            raise Exception("Cannot set winning eligibilities for eliminated player")        
        self.eligibleToWin = amount
        
    def setOrder(self, order):     
        self.order = order