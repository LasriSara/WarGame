from random import shuffle
from Card import Card

class Deck:
    NumArr = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "prence", "queen", "king", "As"]
    ShapeArr = ["♠", "♣", "♥", "♦"]

    def __init__(self):
        Arr = []
        for n in self.ShapeArr:
            for k in self.NumArr:
                Arr.append(Card(k, n))
        self.DeckArr = Arr

    def Mix(self):
        shuffle(self.DeckArr)

    def Printt(self):
        for n in self.DeckArr:
            print(n)

    def Pop(self):
        return self.DeckArr.pop()
