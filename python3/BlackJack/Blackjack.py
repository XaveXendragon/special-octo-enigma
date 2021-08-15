#Hopefully a simple BlackJack 21 Game

from random import choice as rc

deck = {"KS" : 10, "QS" : 10, "JS" : 10, "10S" : 10, "9S" : 9, "8S" : 8, 
        "7S" : 7, "6S" : 6, "5S" : 5, "4S" : 4, "3S" : 3, "2S" : 2, 
        "KC" : 10, "QC" : 10, "JC" : 10, "10C" : 10, "9C" : 9, "8C" : 8, 
        "7C" : 7, "6C" : 6, "5C" : 5, "4C" : 4, "3C" : 3, "2C" : 2, 
        "KH" : 10, "QH" : 10, "JH" : 10, "10H" : 10, "9H" : 9, "8H" : 8, 
        "7H" : 7, "6H" : 6, "5H" : 5, "4H" : 4, "3H" : 3, "2H" : 2, 
        "KD" : 10, "QD" : 10, "JD" : 10, "10D" : 10, "9D" : 9, "8D" : 8, 
        "7D" : 7, "6D" : 6, "5D" : 5, "4D" : 4, "3D" : 3, "2D" : 2, 
        "AS" : 0, "AC" : 0, "AH" : 0, "AD" : 0}

def start():
    print("Welcome to BlackJack!!!")
    global name
    global hand
    global hand_n
    hand = []
    hand_n = []
    name = input("Enter your name: ")
    main()

def deal():
    for x in range(0, 2):
        card = rc(list(deck))
        hand.append(card)
    main()

def resolve():
    for x in hand:
        if x =="AS":
            _input = input("(H)igh or (L)ow Ace: ")
            if _input == "H":
                deck["AS"] = 11
            if _input == "L":
                deck["AS"] = 1
        elif x =="AC":
            _input = input("(H)igh or (L)ow Ace: ")
            if _input == "H":
                deck["AC"] = 11
            if _input == "L":
                deck["AC"] = 1
        elif x =="AH":
            _input = input("(H)igh or (L)ow Ace: ")
            if _input == "H":
                deck["AH"] = 11
            if _input == "L":
                deck["AH"] = 1
        elif x =="AD":
            _input = input("(H)igh or (L)ow Ace: ")
            if _input == "H":
                deck["AD"] = 11
            if _input == "L":
                deck["AD"] = 1
        cardv = deck.get(x)
        hand_n.append(cardv)
    end()

def hit():
    for x in range(0, 1):
        hand.append(rc(list(deck)))
    main()

def main():
    print(str(name) + "'s hand")
    print(hand)
    if len(hand) == 0:
        deal()
    elif len(hand) > 0:
        _input = input("Do you want to hit? Y/N:")
        if _input == "Y":
            hit()
        elif _input == "N":
            resolve()

def end():
    print(sum(hand_n))
    if sum(hand_n) > 21:
        print("Lose")
    elif sum(hand_n) <= 21:
        print("Lose, we're shooting for 21")
    _input = input("Would you like play again? Y/N: ")
    if _input == "Y":
        start()
    elif _input == "N":
        exit

def com_play():
    pass
    
    

start()