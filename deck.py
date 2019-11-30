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
