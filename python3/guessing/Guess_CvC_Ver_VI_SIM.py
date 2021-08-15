#Guess CvC Ver VI
#Simulating the Computer's ability to guess correctly?

import random, statistics
from matplotlib import pyplot as plt

source = []
effi_list = []
x_coord = []

def gene(low, high):
    for x in range(low, high):
        source.append(x)

def guess1():
    guess = random.choice(source)
    return guess

def guess2():
    guess = random.choice(source)
#    print(guess)
    source.remove(guess)
    return guess

def main():
    gene(1, 1001)
    global effi
    computer1 = guess1()
    computer2 = guess2()
    while True:
        if computer2 == computer1:
#            print("Comgrats!!! Your guessed correctly: " + str(computer2))
#            print("Only " + str(len(source)) + " guesses left")
            effi = round(len(source)/1000 * 100, 2)
#            print("Efficiency: " + str(effi) + "%")
            break
        else:
            computer2 = guess2()
    
def stat():
    for x in range(100):
        main()
        source.clear()
        effi_list.append(effi)
        
    overall_effi = round(statistics.mean(effi_list), 2)
    print("Overall efficiency: " + str(overall_effi) + "%")
    
    med = statistics.median(effi_list)
    print("Median: " + str(med))
    
    grp_med = statistics.median_grouped(effi_list)
    print("Grouped Median: " + str(grp_med))
    
    low_med = statistics.median_low(effi_list)
    print("Median Low: " + str(low_med))
    
    high_med = statistics.median_high(effi_list)
    print("Median High: " + str(high_med))
    
    sdev = statistics.stdev(effi_list)
    print("Standard Dev: " + str(sdev))
    
    sdev_pop = statistics.pstdev(effi_list)
    print("Standard Dev Population: " + str(sdev_pop))
    
#    svar = statistics.variance(effi_list)
#    print("Variance: " + str(svar))
    
#    svar_pop = statistics.pvariance(effi_list)
#    print("Variance Population: " + str(svar_pop))

def graph():
    for x in range(1, 101):
        x_coord.append(x)

    w = 75
    h = 25
    d = 100
    plt.figure(figsize=(w, h), dpi=d)
    plt.axis([0, 100, 0, 100])
    plt.scatter(x_coord, effi_list, c='r', s=100)
    plt.plot(x_coord, effi_list, c='r')
    plt.show()
#    plt.savefig("out.png")

main()
stat()
graph()

#print(x_coord)
#print(effi_list)