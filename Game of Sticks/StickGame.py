from random import randint
import sys

def playerMax(n,sticks,player,alpha,beta):
    if n == 1 and player == 1: 
        return [1,1,-1,beta]
    elif n == 1 and player == 2:
        return [1,2,alpha,1]
    else:
        for j in range(1,4):
            i = 4 - j
            if n > i:
                if(player == 1):
                    arr = []
                    arr = playerMax(n-i,i,2,alpha,beta)
                    if arr[2] < arr[3]:
                        alpha = arr[3]
                    if alpha == 1 or alpha > beta:
                        break

                else:
                    arr =[]
                    arr = playerMax(n-i,i,1,alpha,beta)
                    if arr[2] < arr[3]:
                        beta = arr[2]
                    if beta == -1 or alpha > beta:
                        break
        return [i,player,alpha,beta]

#Human vs Human
def twoPlayer(n):
    print("\nTOSS...")
    tossWinner = randint(1,2)
    if tossWinner == 1:
        print("Player 1 won the toss\n")
        tl = 2
    else:
        print("Player 2 Won the toss\n")
        tl = 1
    while True:
        m = int(input("Player " + str(tossWinner) + ": How many sticks do you want to pick? "))
        while True:
            if m < 4 and m > 0 and m <= n:
                break
            m = int(input("Please, Enter a valid number: "))
        n = n - m
        if n == 0:
            print("\nPlayer " + str(tl) + " Win\n" + "Player " + str(tossWinner) + " Lose\n")
            break
        print("\nRemaining sticks: " + str(n))
        m = int(input("Player " + str(tl) + ": How many sticks do you want to pick? "))
        while True:
            if m < 4 and m > 0 and m <= n:
                break
            m = int(input("Please, Enter a valid number: "))
        n = n - m
        if n == 0:
            print("\nPlayer " + str(tossWinner) + " Win\n" + "Player " + str(tl) + " Lose\n")
            break
        print("\nRemaining sticks: " + str(n))

# Human Vs Computer
def onePlayer(n):
    print("\nTOSS...")
    tossWinner = randint(1,2)
    if tossWinner == 1:
        print("Computer won the toss\n")
    else:
        print("You won the toss\n")
    
    while True:
        if tossWinner == 1:
            arr = []
            arr = playerMax(n,0,1,-sys.maxsize,sys.maxsize)
            print ("Number of sticks computer picks: " + str(arr[0]) + "\n")
            n = n - arr[0]
            if n == 0:
                print("You Win\nComputer Lose\n")
                break
            print("Remaining sticks: " + str(n))
            m = int(input("How many sticks do you want to pick? "))
            while True:
                if m < 4 and m > 0 and m <= n:
                    break
                m = int(input("Please, Enter a valid number: "))
            n = n - m
            if n == 0:
                print("\nComputer Win\nYou Lose\n")
                break
            print("\nRemaining sticks: " + str(n))
        else:
            m = int(input("How many sticks do you want to pick? "))
            while True:
                if m < 4 and m > 0 and m <= n:
                    break
                m = int(input("Please, Enter a valid number: "))
            n = n - m
            if n == 0:
                print("\nComputer Win\nYou Lose\n")
                break
            print("\nRemaining sticks: " + str(n))
            arr = []
            arr = playerMax(n,0,1,-sys.maxsize,sys.maxsize)
            print ("Number of sticks computer picks: " + str(arr[0]) + "\n")
            n = n - arr[0]
            if n == 0:
                print("You Win\nComputer Lose\n")
                break
            print("Remaining sticks: " + str(n))

# Computer vs Computer
def onlyComputer(n):
    print("\nTOSS...")
    tossWinner = randint(1,2)
    if tossWinner == 1:
        print("Player 1 won the toss\n")
        tl = 2
    else:
        print("Player 2 Won the toss\n")
        tl = 1
    while True:
        arr1 = []
        arr1 = playerMax(n,0,1,-sys.maxsize,sys.maxsize)
        print ("Player " + str(tossWinner) + ": pick " + str(arr1[0]) + " sticks\n")
        n = n - arr1[0]
        if n == 0:
            print("\nPlayer " + str(tl) + " Win\n" + "Player " + str(tossWinner) + " Lose\n")
            break
        print("Remaining sticks: " + str(n))
        arr2 = []
        arr2 = playerMax(n,0,1,-sys.maxsize,sys.maxsize)
        print ("Player " + str(tl) + ": pick " + str(arr2[0]) + " sticks\n")
        n = n - arr2[0]
        if n == 0:
            print("\nPlayer " + str(tossWinner) + " Win\n" + "Player " + str(tl) + " Lose\n")
            break
        print("Remaining sticks: " + str(n))


#Driver Code
print("\n----------Welecome to the game to sticks----------\n")
while True:
    print("Options:\n1.Human vs Human\n2.Computer vs Human\n3.Computer vs Computer\n4.Exit")
    choose = int(input("choose above options: "))
    while True:
        if choose > 0 and choose < 5:
            break
        choose = int(input("Please, choose correct options: "))

    if choose == 4:
        break

    n = int(input("\nEnter the number of sticks: "))

    if choose == 1:
        # Human vs Human
        twoPlayer(n)
    elif choose == 2:
        # AI vs Human
        onePlayer(n)
    elif choose == 3:
        # AI vs AI
        onlyComputer(n)

    check = input ("Do you want to play again?(yes/no) ")
    print("\n")
    if check == "no":
        print("Thank You!\n")
        break
