class deck(object):
    """Class for the creation of a deck and cards"""

    def __init__(self, jokers = False):
        self.deck = []
        for i in range(13):
            self.deck.append(i+"S") # Spades
            self.deck.append(i+"H") # Hearts
            self.deck.append(i+"C") # Clubs
            self.deck.append(i+"D") # Diamonds
            # 11 = Jack
            # 12 = Queen
            # 13 = King
        if jokers:
            self.deck.append("Joker")
            self.deck.append("Joker")

    def __del__(self):
        deck.clear()

    def shuffle(self, deck = []):
        D = deck[::]
        temp = []
        D1 = D[len(D)/2:]
        D2 = D[:len(D)/2]
        print("Deck 1: " + str(D1))
        print("Deck 2: " + str(D2))
        for i in D1:
            temp.append(i)

        print("Combined: " + str(temp))
