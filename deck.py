import random
class deck(object):
    """Class for the creation of a deck and cards"""

    def __init__(self, jokers = False):
        self.deck = []
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        for i in range(13):
            self.deck.append(str(i)+"S") # Spades
            self.deck.append(str(i)+"H") # Hearts
            self.deck.append(str(i)+"C") # Clubs
            self.deck.append(str(i)+"D") # Diamonds
            # 11 = Jack
            # 12 = Queen
            # 13 = King
        if jokers:
            self.deck.append("Joker")
            self.deck.append("Joker")

    def __del__(self):
        self.deck.clear()

    def shuffle(self, deck, evenShuffle=False):
        D = deck[::]
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

        

        print("Combined: " + str(temp))

class card(object):
    def __init__(self):
        self.suit = None
        self.number = None
