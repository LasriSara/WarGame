from Deck import Deck
from Player import Player
from Card import Card

print("Hello to our game!!!!")
d = Deck()
d.Mix()
name1 = input("player1 enter  name  ")
name2 = input("player2 enter name  ")
p1 = Player(name1)
p2 = Player(name2)
count = len(d.DeckArr)
while (count != 0):
    if count % 2 == 0:
        p1.Insert(d.Pop())
    else:
        p2.Insert(d.Pop())
    count = count - 1


print(p1)
print(p2)


def game(NumArr):
    global p1, p2
    mone = 0
    while (len(p1.pile) != 0 and len(p2.pile) != 0):

        mone += 1
        if mone == 1000:
            print(f"There are no winners")
            return
        card1 = p1.Pop()
        card2 = p2.Pop()

        print(f"Card of {p1.name}: {card1}, Card of {p2.name}: {card2}, Pile1 length: {len(p1.pile)}, Pile2 length: {len(p2.pile)}")
        if NumArr.index(card1.num) > NumArr.index(card2.num):
            p1.Insert(card1)
            p1.Insert(card2)
            print(f"{p1.name} gets the cards")
        elif NumArr.index(card1.num) < NumArr.index(card2.num):
            p2.Insert(card2)
            p2.Insert(card1)
            print(f"{p2.name} gets the cards")
        else:
            tmp1 = []
            tmp2 = []
            tmp1.insert(0, card1)
            tmp2.insert(0, card2)
            while NumArr.index(card1.num) == NumArr.index(card2.num):
                print("Fight")
                for i in range(1, 5):
                    if len(p1.pile) == 0:
                        tmp1.insert(0, tmp1.pop())
                    elif len(p2.pile) == 0:
                        tmp2.insert(0, tmp2.pop())
                    else:
                        card1 = p1.Pop()
                        card2 = p2.Pop()
                        tmp1.insert(0, card1)
                        tmp2.insert(0, card2)

            if NumArr.index(card1.num) > NumArr.index(card2.num):
                p1.pile.extend(tmp1)
                p1.pile.extend(tmp2)
                print(f"Card of {p1.name}: {card1}, Card of {p2.name}: {card2}")
            else:
                p2.pile.extend(tmp1)
                p2.pile.extend(tmp2)
                print(f"Card of {p1.name}: {card1}, Card of {p2.name}: {card2}")

    if len(p2.pile) == 0:
        print(f"{p1.name} is the winner!!😃")
    else:
        print(f"{p2.name} is the winner!!😃")

game(Card.NumArr)
