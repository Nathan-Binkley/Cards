import random
class deck(object):
    """Class for the creation of a deck and cards"""

    def __init__(self, jokers = False):
        self.deck = []
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        for i in range(13):
            H = card("Hearts", i)
            S = card("Spades", i)
            D = card("Dimonds", i)
            C = card("Clubs", i)
            self.deck.extend([H, S, D, C]) #Store cards in the deck as objects of type cards
                                           #Updated from being a <number><SuitLetter> combination
            
            # 11 = Jack
            # 12 = Queen
            # 13 = King
        if jokers:
            self.deck.append("Joker")
            self.deck.append("Joker")

    def __del__(self):
        self.deck.clear()

    def shuffle(self, deck, evenShuffle=False):
        D = deck[::] # Copy Deck
        temp = []
        if evenShuffle:
            D1 = D[len(D)/2:]
            D2 = D[:len(D)/2]
            print("Deck 1: " + str(D1))
            print("Deck 2: " + str(D2))
            for i in range(len(D1)):
                temp.append(D1[i])
                temp.append(D2[i])
        else:
            value = random.randint(-10,10)
            D1 = D[(len(D)/2)+value:]
            D2 = D[:(len(D)/2)-value]
            low = min(len(D1), len(D2))

            for i in range(low): #for every card, put bottom from each stack on the deck, alternating stacks until one is empty
                temp.append(D1.pop(0))
                temp.append(D2.pop(0))

            while D1: #Handle remaining not accounted for in random selection appending them to the deck object
                temp.append(D1.pop())
            while D2:
                temp.append(D2.pop())
        deck = temp    # "in place" replacement    
        print("Combined: " + str(temp))

class card(object):
    def __init__(self, suit = None, number = None):
        self.suit = None
        self.number = None
