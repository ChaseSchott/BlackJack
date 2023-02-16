from blackjack import Deck, Player, Dealer, hit_stay
# Game Play #  
while True:
    print('\n *** Welcome to BlackJack! Get as close to 21 as you can and try not to bust!\n\
        Best of luck may the odds be in your favor! *** \n')

    deck = Deck()
    dealer = Dealer()
    dealer.draw(deck.deal()) 
    dealer.draw(deck.deal())
    print('The Dealer has')
    for card in dealer.hand[:1]:
        print('? and ' + str(card))
    print ('\n')
    
# PLAYER GAMEPLAY           
    player = Player()
    player.draw(deck.deal()) 
    player.draw(deck.deal())
    print('You have ' + (str(player.value)) + ' with these cards ')
    for card in player.hand:
        print(card)
    hit_stay(deck, player)
    if player.value > 21:              
        print('\n You Bust! Game Over!') 
        break
    
    print('\n Dealers Turn')
    print('...')
    
# DEALER GAMEPLAY
    print('The Dealer has ' + (str(dealer.value)) + ' with these cards ')
    for card in dealer.hand:
        print(str(card))
    while dealer.value < 17:
        print ('\n Dealer will draw another card \n')
        dealer.draw(deck.deal())
        print('The Dealer now has ' + (str(dealer.value)) + ' with these cards ')
        for card in dealer.hand:
            print(str(card))   
    if dealer.value > 21:
        print('\n Dealer Busts! YOU WIN! \n')
        x = input("Would You Like to Continue Playing? Enter 'Y' or 'N' ")
        if x.upper() == 'Y':
            continue
        elif x.upper() == 'N':
            print('\n''Thank You For Playing!')
        break         

# HAND VALUE COMPARISON WIN/LOSE
    if dealer.value > player.value:
        print ('\n YOU LOSE!, Better luck next time!')
    elif dealer.value == player.value:
        print('\n TIE GAME!')
        x = input("Would You Like to Continue Playing? Enter 'Y' or 'N' ")
        if x.upper() == 'Y':
            continue
        elif x.upper() == 'N':
            print('\n''Thank You For Playing!')
            break  
    else: 
        dealer.value < player.value
        print('\n YOU WIN!')
        x = input("Would You Like to Continue Playing? Enter 'Y' or 'N' ")
        if x.upper() == 'Y':
            continue
        elif x.upper() == 'N':
            print('\n Thank You For Playing!')
            break  
    break