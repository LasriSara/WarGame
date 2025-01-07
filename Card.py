class Card:
    NumArr = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "prence", "queen", "king", "As"]
    ShapeArr = ["♠", "♣", "♥", "♦"]

    def __init__(self, n, s):
        self.num = n
        self.shape = s

    def __str__(self):
        return "%s of %s" % (self.num, self.shape)
