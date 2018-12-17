#Modules being used
import itertools, random

#Card Class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " of " + self.suit

    def show_card(self):
        print(str(self.value) + " of " + str(self.suit))

    def print_card(self):
        print(str(self.value) + " of " + str(self.suit))

#class Hand:
    #def __init__(self, card 1, card2):
        #self.card1 = card
        #self.card2 = card2

#suits that go into the card class
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4','5','6','7','8','9','10','Jack','queen','king']
deck = [Card(value, suit) for value in values for suit in suits]
random.shuffle(deck)
hand = []
hand.append(deck.pop())
hand.append(deck.pop())
my_card = Card(1, "hearts")
#print (hand.print_card() for i in hand)
#print (Card.show_card() for Card in deck)
for card in hand:
    card.print_card()
