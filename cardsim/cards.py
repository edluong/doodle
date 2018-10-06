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
print('Number of cards:',len(deck))

    
