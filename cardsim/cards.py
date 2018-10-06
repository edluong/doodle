from random import shuffle #needed to use the shuffle method for lists

#set up the list of suits and ranks
suits = ['Hearts','Diamonds','Clubs','Spades']
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

#initialize the deck
deck = []

#load the deck
for suit in suits:
    for rnk in rank:
        card = rnk,suit
        deck.append(card)

#print out all of the cards
for card in deck:
    print(card,end="\n")

#print the number of cards
print('\nNumber of cards:',len(deck))

#choose the top card
shuffle(deck)
print('Shuffling....')
print('After shuffling, You picked:', deck[0][0],end='')
print(' of',deck[0][1])

print("Your Texas Hold'em Poker hand would be:",deck[:2])
print("Your Omaha Poker hand would be:",deck[:4])
print("Your Five Card Poker hand would be:",deck[:5])


    
