#Modules being used
import itertools, random

#Objects
class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(0, 13):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print (card)

    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return (len(self.cards) == 0)

    def deal(self, target, number):
        for i in range(number):
            card = self.pop()
            target.add(card)

class Player(Deck):
    def __init__(self, name):
        chips = 100
        self.cards = []
        self.name = name
        self.chips = chips

    def add(self,card):
        self.cards.append(card)

    def addchips(self, amount):
        self.chips += amount

class Table(Deck):
    def __init__(self):
       self.cards = []

    def add(self,card):
        self.cards.append(card)

#Setup
pot = 0
deck = Deck()
deck.shuffle()
table = Table()
print ("The Table contains: ")
deck.deal(table, 3)
table.print_deck()
#deck.print_deck()
"""
player1 = Player("George")
player2 = Player("Henry")
player3 = Player("Guy")
player4 = Player("Okay")
player5 = Player("Predator")
player6 = Player("Prey")
player7 = Player("Random")
player8 = Player("Buddy")
player9 = Player("Human")
"""
players = [Player(count) for count in range(9)]

#Loop
for x in range(3):
    if x < 2:
        deck.deal(table, 3)
for i in range(9):
            deck.deal(players[i], 2)
            print("Player " + str(players[i].name))
            players[i].print_deck()
