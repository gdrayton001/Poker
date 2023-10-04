from CPU import CPU
from PokerCalculator import *
from PokerGame import Game
from Player import Player
from tkinter import *
import PIL.Image
import PIL.ImageTk

# Hand = a repetition of the game that ends when a player has won the pot.
# Round = a repetition of a hand in which all active players have had a chance to bet and/or fold
# Turn = a repetition of a round in which a player decides to fold, limp (check or place the required bet), or raise the bet.

root = Tk()
root.title("Poker")
root.geometry("250x125")

def check(player):
    newOrder = game.nextTurn((player.order+1) % len(game.players))
    if newOrder == -1:
        endRound()
    else:
        nextTurn(newOrder)  

def endHand():
    global hand_winner_label
    global winner
    strength_label.grid_forget()
    limp_button.config(text="Next", command=nextHand)
    fold_button.config(state=DISABLED)
    bet_button.config(state=DISABLED)  
    winner = game.endHand()
    if game.handIsLive() and not game.nextRoundIsPlayable():
        card4_image = game.fourthCard.getImage()
        flop_card4_pic.config(image=card4_image)
        flop_card4_pic.image = card4_image                
        card5_image = game.fifthCard.getImage()
        flop_card5_pic.config(image=card5_image)
        flop_card5_pic.image = card5_image   
    game.awardChipsTo(winner)
    winner_text = winner[0].name
    if game.handIsLive():               
        showdown()
        if len(winner) > 1:
            for i in range(1, len(winner)):
                winner_text += " and "
                winner_text += winner[i].name
        hand_winner_label = Label(root, text=winner_text + " wins with a " + getHandRanking(winner[0].hand, game.threeCardFlop + [game.fourthCard, game.fifthCard]))
    else:
        hand_winner_label = Label(root, text=winner_text + " wins the hand.")
    hand_winner_label.grid(row=18, column=16, rowspan=2, columnspan=6)
        
def endRound():
    global pot_label
    global pot_chips_label
    print("Round Ended")
    roundEnded = game.endRound() 
    strength_label.grid_forget()
    if roundEnded > 0:
        pot_label.config(text=toString(game.pot))
    else:
        pot_label = Label(root, text=toString(game.pot))
        pot_label.grid(row=10, column=17, rowspan=2, columnspan=3) 
    chip_image = PIL.ImageTk.PhotoImage(PIL.Image.open("poker_chips.png"))
    pot_chips_label = Label(root, image=chip_image) 
    pot_chips_label.image = chip_image          
    pot_chips_label.grid(row=10, column=14, rowspan=2, columnspan=3)   
    for p in game.players:
        p.deleteChipImage()
        p.bettingIcon.grid_forget()
    if roundEnded == 3:
        endHand()        
        return
    elif roundEnded == 0:
        card1_image = game.threeCardFlop[0].getImage()
        card2_image = game.threeCardFlop[1].getImage()
        card3_image = game.threeCardFlop[2].getImage()
        flop_card1_pic.config(image=card1_image)
        flop_card2_pic.config(image=card2_image)
        flop_card3_pic.config(image=card3_image)
        flop_card1_pic.image = card1_image
        flop_card2_pic.image = card2_image
        flop_card3_pic.image = card3_image
    elif roundEnded == 1:
        card4_image = game.fourthCard.getImage()
        flop_card4_pic.config(image=card4_image)
        flop_card4_pic.image = card4_image
    else:
        card5_image = game.fifthCard.getImage()
        flop_card5_pic.config(image=card5_image)
        flop_card5_pic.image = card5_image
    nextTurn(game.getStartingPlayerOrder())

def expose_card(button, card):
    myImage = card.getImage()
    button.configure(image=myImage)
    button.image = myImage
    button.config(command=lambda: hide_card(button, card))
    strength_label.grid(row=14, column=26, rowspan=2, columnspan=2)
    
def fold(player):
    game.fold(player)
    newOrder = game.nextTurn((player.order+1) % len(game.players))
    if newOrder == -1:
        endRound()
    else:
        nextTurn(newOrder)

def hide_card(button, card):
    button.config(image=back_of_card, command=lambda: expose_card(button, card))
    
def minusRaiseBet():
    amount_betting_label.config(text=toString(toInt(amount_betting_label.cget('text'))-game.blind))
    plus_button.config(state=NORMAL)
    submit_raised_bet_button.config(command=lambda: submitRaisedBet(game.activePlayer, toInt(amount_betting_label.cget('text'))))
    if toInt(amount_betting_label.cget('text'))-game.blind <= max(game.blind, game.betAmount):
        minus_button.config(state=DISABLED)
        
def nextHand():
    global spaces
    global chip_spaces
    global card1_pic
    global card2_pic    
    global back_of_card
    global flop_card1_pic
    global flop_card2_pic
    global flop_card3_pic
    global flop_card4_pic
    global flop_card5_pic
    global fold_button
    global limp_button
    global bet_button    
    global game_winner_label
    global strength_label
    try:
        pot_label.grid_forget()
        pot_chips_label.grid_forget()
        hand_winner_label.grid_forget()
        try:
            for l in player_labels:
                l.grid_forget()
            for hand in player_hands:
                for l in hand:
                    l.grid_forget()
        except NameError:
            pass
    except NameError:
        pass
    if game.hands > 0:
        game.resetOrders()
    gameStatus = game.nextHand()
    if gameStatus == -1:
        game_winner_label = Label(root, text=game.gameWinner().name + " has won the game.")
        game_winner_label.grid(row=18, column=16, rowspan=2, columnspan=6)
        limp_button.config(text="Play Again", command=returnHome)
        return
    allSpaces = [(18,22), (9,22), (0,22), (0,16), (0,10), (0,6), (0,0), (9,0), (12,0), (18,0), (24,0), (27,0), (36,0), (36,6), (36,10), (36,16), (36,22), (27,22)]
    spaces = [(18,22)]
    allChipSpaces = [(18,20), (9,20), (2,20), (2,16), (2,10), (2,6), (2,2), (9,2), (12,2), (18,2), (24,2), (27,2), (34,2), (34,6), (34,10), (34,16), (34,20), (27,20)]
    if len(players) % 2 == 0:
        spaces.append((18,0))
        if len(players) == 8 or len(players) == 10:
            spaces.append((9,0))
            spaces.append((27,0))  
            spaces.append((9,22))
            spaces.append((27,22))            
            if len(players) == 10:
                spaces.append((0,6))
                spaces.append((0,16))      
                spaces.append((36,6))
                spaces.append((36,16))
    elif len(players) == 7 or len(players) == 9:
        spaces.append((12,0))
        spaces.append((24,0))
    if len(players) % 2 == 1 or len(players) == 6:
        spaces.append((0,0))
        spaces.append((36,0))
        if len(players) in range(5,8):
            spaces.append((0,22))
            spaces.append((36,22)) 
    if len(players) % 4 == 0 or len(players) == 9:
        spaces.append((0,10))
        spaces.append((36,10))        
        if len(players) == 9:
            spaces.append((9,22))
            spaces.append((27,22)) 
    spaces = matchOrder(allSpaces, spaces)
    chip_spaces = correspondingList(allSpaces, spaces, allChipSpaces)
    if len(players) != len(spaces):
        raise Exception("Number of spaces found does not match number of players in the game")
    num_users_label.grid_forget()
    num_cpus_label.grid_forget()
    num_users_drop.grid_forget()
    num_cpus_drop.grid_forget()
    start_game_button.grid_forget()
    back_of_card = PIL.ImageTk.PhotoImage(PIL.Image.open("back_of_card.jpeg"))
    card1_pic = Button(root, image=back_of_card, command=lambda: expose_card(card1_pic, game.activePlayer.hand[0]))
    card2_pic = Button(root, image=back_of_card, command=lambda: expose_card(card2_pic, game.activePlayer.hand[1]))
    card1_pic.grid(row=12, column=13, columnspan=6, rowspan=6)
    card2_pic.grid(row=12, column=19, columnspan=6, rowspan=6)
    flop_card1_pic = Label(root, image=back_of_card)
    flop_card2_pic = Label(root, image=back_of_card)
    flop_card3_pic = Label(root, image=back_of_card)
    flop_card4_pic = Label(root, image=back_of_card)
    flop_card5_pic = Label(root, image=back_of_card)
    flop_card1_pic.grid(row=6, column=4, columnspan=6, rowspan=4)
    flop_card2_pic.grid(row=6, column=10, columnspan=6, rowspan=4)
    flop_card3_pic.grid(row=6, column=16, columnspan=6, rowspan=4)
    flop_card4_pic.grid(row=6, column=22, columnspan=6, rowspan=4)
    flop_card5_pic.grid(row=6, column=28, columnspan=6, rowspan=4)
    placeBetFor(game.littleBlind(), int(game.blind/2))
    placeBetFor(game.bigBlind(), game.blind)  
    placeChipsFor(game.littleBlind(), int(game.blind/2))
    placeChipsFor(game.bigBlind(), game.blind)  
    fold_button = Button(root, text="Fold", command=lambda: fold(game.activePlayer), state=NORMAL)
    limp_button = Button(root, text="Bet " + toString(min(game.betAmount-game.activePlayer.betting, game.activePlayer.chips-game.activePlayer.betting)), command=lambda: placeBet(game.activePlayer, min(game.betAmount-game.activePlayer.betting, game.activePlayer.chips-game.activePlayer.betting)), state=NORMAL)
    bet_button = Button(root, text="Raise", command=lambda: raiseBet(game.activePlayer), state=NORMAL)
    fold_button.grid(row=24, column=0, columnspan=13)
    limp_button.grid(row=24, column=13, columnspan=13)
    bet_button.grid(row=24, column=26, columnspan=13)
    for p in players:
        p.label.grid(row=spaces[p.order][1], column=spaces[p.order][0], rowspan=2, columnspan=2)  
    strength_label = Label(root, text=toString(getHandStrength(game.activePlayer.hand)) + "/10")
    
def nextTurn(newOrder): 
    if not game.handIsLive() or not game.nextRoundIsPlayable():
        endHand()
        return
    for p in game.players:
        p.label.grid_forget()    
        newSpace = spaces[(p.order-newOrder) % len(game.players)]
        p.label.grid(row=newSpace[1], column=newSpace[0])
        if p.betting > 0:
            p.deleteChipImage()
            placeChipsFor(p, p.betting)
    card1_pic.config(image=back_of_card, command=lambda: expose_card(card1_pic, game.activePlayer.hand[0]))
    card2_pic.config(image=back_of_card, command=lambda: expose_card(card2_pic, game.activePlayer.hand[1]))
    strength_label.config(text=toString(getHandStrength(game.activePlayer.hand)) + "/10")
    strength_label.grid_forget()
    if game.betAmount > game.activePlayer.betting:
        limp_button.config(text="Bet " + toString(min(game.betAmount-game.activePlayer.betting, game.activePlayer.chips-game.activePlayer.betting)), command=lambda: placeBet(game.activePlayer, min(game.betAmount-game.activePlayer.betting, game.activePlayer.chips-game.activePlayer.betting)))
    else:
        limp_button.config(text="Check", command=lambda: check(game.activePlayer), state=NORMAL)
        
def placeBet(player, amount):
    placeBetFor(player, amount)
    newOrder = game.nextTurn((player.order+1) % len(game.players))
    if newOrder == -1:
        endRound()
    else:
        nextTurn(newOrder) 
    
def placeBetFor(player, amount):
    game.placeBetFor(player, amount)
    
def placeChipsFor(player, amount):
    player.bettingIcon.grid(row=chip_spaces[(player.order - game.activePlayer.order) % len(game.players)][1]+1, column=chip_spaces[(player.order - game.activePlayer.order) % len(game.players)][0], columnspan=2)
    player.createChipImage(root)
    chip_image_label = player.chip_image_label
    chip_image_label.grid(row=chip_spaces[(player.order - game.activePlayer.order) % len(game.players)][1], column=chip_spaces[(player.order - game.activePlayer.order) % len(game.players)][0], columnspan=2) 
    
def plusRaiseBet():
    amount_betting_label.config(text=toString(min(toInt(amount_betting_label.cget('text'))+game.blind, game.activePlayer.chips-game.activePlayer.betting)))
    minus_button.config(state=NORMAL)
    submit_raised_bet_button.config(command=lambda: submitRaisedBet(game.activePlayer, toInt(amount_betting_label.cget('text'))))
    if amount_betting_label.cget('text') == game.activePlayer.chips-game.activePlayer.betting:
        plus_button.config(state=DISABLED)
        
def raiseBet(player):
    global raise_bet_window
    global plus_button
    global amount_betting_label
    global minus_button
    global submit_raised_bet_button
    raise_bet_window = Toplevel()
    plus_button = Button(raise_bet_window, text="+", command=plusRaiseBet)
    amount_betting_label = Label(raise_bet_window, text=toString(game.betAmount + game.blind))
    minus_button = Button(raise_bet_window, text="-", command=minusRaiseBet, state=DISABLED)
    submit_raised_bet_button = Button(raise_bet_window, text="Submit", command=lambda: submitRaisedBet(game.activePlayer, game.betAmount + game.blind))
    plus_button.grid(row=0, column=0)
    amount_betting_label.grid(row=1, column=0)
    minus_button.grid(row=2, column=0)
    submit_raised_bet_button.grid(row=3, column=0)
    
def returnHome():
    return

def showdown():
    global player_labels
    global player_hands
    global hand_winner_label
    root.geometry("1000x1000")
    player_labels = []
    player_hands = []
    for p in game.activePlayers():
        player_label = Label(root, text=p.name)
        player_labels.append(player_label)
        card1_image_label = Label(root)
        card2_image_label = Label(root)
        card1_image = p.hand[0].getImage()
        card2_image = p.hand[1].getImage()  
        card1_image_label.configure(image=card1_image)
        card2_image_label.configure(image=card2_image)
        card1_image_label.image = card1_image
        card2_image_label.image = card2_image
        player_hands.append([card1_image_label, card2_image_label])
    for i in range(len(player_labels)):
        if i < 5:
            player_labels[i].grid(row=i*4, column=38, rowspan=2)
            player_hands[i][0].grid(row=i*4+2, column=38, rowspan=2)
            player_hands[i][1].grid(row=i*4+2, column=39, rowspan=2)
        else:
            player_labels[i].grid(row=(i-5)*4, column=40, rowspan=2)
            player_hands[i][0].grid(row=(i-5)*4+2, column=40, rowspan=2)
            player_hands[i][1].grid(row=(i-5)*4+2, column=41, rowspan=2)  
    
def start_game():
    global game
    global players
    root.geometry("750x500")
    players = []
    for i in range(num_users.get()):
        players.append(Player(i, "P"+toString(i+1), root))
    for i in range(num_cpus.get()):
        players.append(CPU(i+num_users.get(), "CP"+toString(i+1), root))
    if len(players) < 2:
        raise Exception("Not enough players to start a game")
    game = Game(players, 800000, 10000)
    nextHand()  

def submitRaisedBet(player, amount):
    game.raiseBet(player, amount)
    raise_bet_window.destroy()
    placeBet(player, amount)      

num_users_label = Label(root, text="Number of Players:")
num_cpus_label = Label(root, text="Number of CPUs:")
num_users = IntVar()
num_cpus = IntVar()
num_users_drop = OptionMenu(root, num_users, *list(range(1,6)))
num_cpus_drop = OptionMenu(root, num_cpus, *list(range(6)))
start_game_button = Button(root, text="Start Game", command=start_game)

num_users.set(1)

num_users_label.grid(row=0, column=0)
num_cpus_label.grid(row=0, column=1)
num_users_drop.grid(row=1, column=0)
num_cpus_drop.grid(row=1, column=1)
start_game_button.grid(row=2, column=0, columnspan=2)

root.mainloop()