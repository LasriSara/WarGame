class Player:
    def __init__(self, name):
        self.name = name
        self.pile = []

    def Pop(self):
        return self.pile.pop()

    def Insert(self, card):
        return self.pile.insert(0, card)

    def __str__(self):
        return "Name: %s, Num of card: %d " % (self.name, len(self.pile))
