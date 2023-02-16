import random
import blackjack_gameplay
Playing = True

# Deck of Cards
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}

class Card:
    def __init__(self,ranks,suits):
        self.ranks = ranks 
        self.suits = suits
    '''    
    Created a str method to output a more readable card for the user. Also for testing.    
    '''
    def __str__(self):
        return self.ranks + ' of ' + self.suits
        
class Deck:
    '''
    In this __init__ method we need to define the Deck as an empty list so we can cycle 
    through each rank and suit and append them to the list.
    '''
    def __init__(self):
        self.Deck = []
        for rank in ranks:
            for suit in suits:
                self.Deck.append(Card(rank,suit))
    '''            
    Created another str method to make the deck of cards more readable for the user with line breaks.
    Also for testing.
    '''            
    def __str__(self):
        cards_in_deck = ''
        for cards in self.Deck:
            cards_in_deck += '\n '+cards.__str__()
        return cards_in_deck
      
# Shuffle and Deal Cards
    '''
    The deal method will randomly pick a card from the built deck. 
    With random.choice we do not have to build a shuffle method    
    '''
    def deal(self):
        single_card = random.choice(self.Deck)
        self.Deck.remove(single_card)
        return single_card
    
# Players Hand
class Player:
    '''   
    The __init__ method will need an empty list to be able to append cards to. It will also need a value counter
    for hand total.
    '''
    def __init__(self):
        self.hand = []
        self.value = 0
    '''     
    The draw method will add the card that was delt and its value to the players hand. 
    '''
    def draw(self,card):
            self.hand.append(card)          
            self.value += value[card.ranks]
            for card in self.hand:
                if card.ranks == 'A' and self.value <= 11:
                    self.value += 10
# Dealer Hand
class Dealer:
    '''   
    The __init__ method will need an empty list to be able to append cards to. It will also need a value counter
    for hand total.
    '''
    def __init__(self):
        self.hand = []
        self.value = 0
    '''     
    The draw method will add the card that was delt and its value to the dealers hand. 
    '''        
    def draw(self,card):
            self.hand.append(card)
            self.value += value[card.ranks]

# Hit or Stay
'''
The hit method will deal another card to the players hand.
'''
def hit(hand,deck):
    hand.draw(deck.deal())
  
'''
The hit_stay method will be the users input to draw and add another card to their hand if they choose. Or,
stay and end their turn if they might bust.
'''               
def hit_stay(deck,hand):
    player = blackjack_gameplay.player
    while Playing: 
        x = input("Would You like to Hit or Stay? Enter 'Hit' or 'Stay' ")
        if x.upper() == 'HIT':
            hand.draw(deck.deal())
            print('\n You now have ' + (str(player.value)) + ' with these cards ')
            for card in player.hand:
                print(card)                           
        elif x.upper() == 'STAY':
            break
        else:
            print('Invalid input, try again!')
        if player.value > 21:
            break     
