# Open and Compare

def big():
    big = open("words_big.txt")
    big_read = big.readlines()
    big_list = []
    for x in big_read:
        print(x)
        x = x.rstrip("\n")
        big_list.append(x)
    print(big_list)

def small():
    small = open ("words_small.txt")
    small_read = small.readlines()
    small_list = []
    for x in small_read:
        print(x)
        x = x.rstrip("\n")
        small_list.append(x)
    print(small_list)
        
small()
big()