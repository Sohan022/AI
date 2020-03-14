from random import seed,randint
from statistics import mean
import sys

# Initialize Population
def InitialPopulation(arr,n,m,k,popul):
    possInd = [[randint(0,n-1) for i in range(k)] for j in range(50)]
    for i in range(0,50):
        for j in range(0,k):
            popul[i][j] = arr[possInd[i][j]][m]

#Calculate Fitness Value
def calculateFitness(arr,n,m,k,popul,minFitness,minArr,prevRow):
    for i in range(50):        
        for j in range(n):
            minDiff = 101
            for l in range(k):
                if abs(arr[j][m] - popul[i][l]) < minDiff:
                    minDiff =  abs(arr[j][m] - popul[i][l])
            popul[i][k] += minDiff
            if minFitness > popul[i][k]:
                minFitness = popul[i][k] 
                minArr = popul[i][:-1]
                prevRow = i

#Select Maximum Fitness Value for Crossover
def selection(arr,k,selected,popul):
    possInd = [[randint(0,49) for i in range(10)] for j in range(50)]
    for i in range(50):
        maxFitness = -1
        for j in range(10):
            if maxFitness < popul[possInd[i][j]][k]:
                maxFitness = popul[possInd[i][j]][k]
                row = possInd[i][j]
        selected[i] = popul[row][:-1]

#Crossover of selected chromosome (Single Point crossover)
def crossover(selected,k):
    for i in range(25):
        rNum = randint(0,k-1)
        temp = selected[i][rNum:-1]
        selected[i][rNum:-1] = selected[49-i][rNum:-1]
        selected[49-i][rNum:-1] = temp

#Mutation
def mutation(arr,selected,n,m,k):
    for i in range(50):
        r1 = randint(0,k-1)
        r2 = randint(0,n-1)
        selected[i][r1] = arr[r2][m]


#Driver Code
n = int(input("Enter the number of students "))
k = int(input("Enter the number of groups "))
m = int(input("Enter the number of subjects "))
rows, cols = (n, m) 

#Generate random marks of student 
arr = [[randint(0,100) for i in range(cols)] for j in range(rows)]

for i in range(n):
    arr[i].append(mean(arr[i]))
#
#Declare population (50)
popul =[[0 for x in range(k+1)]for y in range(50)]

#Initialize Population
InitialPopulation(arr,n,m,k,popul)

minFitness = sys.maxsize
minArr = [0 for x in range(k)]
count = 0
minFit = sys.maxsize
minA = [0 for y in range(k)]
prevRow = 0
currRow = 0

#Calculate Fitness Value
calculateFitness(arr,n,m,k,popul,minFitness,minArr,prevRow)

while True:
    count = count + 1
    selected = [[0 for x in range(k)]for y in range(50)]

    #Select chromosome for crossover
    selection(arr,k,selected,popul)

    #crossover of selected chromosome
    crossover(selected,k)

    #Mutation
    mutation(arr,selected,n,m,k)
    
    for i in range(50):
        selected[i].append(0)

    #Calculate Fitness after mutation for new fitness decreses or increses
    calculateFitness(arr,n,m,k,selected,minFit,minA,currRow)
    
    #if new fitness is greater than older fitness or loop turns 2000 times then break
    if(count > 2000 or minFit >= minFitness):
        for i in range(n):
            minDiff = 101
            for j in range(k):
                if abs(arr[i][m] - popul[prevRow][j]) < minDiff:
                    minDiff =  abs(arr[i][m] - popul[prevRow][j])
                    col = j
            print ("Student:", i+1, "=", " [Group:", col+1, "   Group Representative:", popul[prevRow][col], "   Avg:",arr[i][m], "]","   Marks:",arr[i][:-1])
        break
    
    #copy the new fitness into old fitness
    else :
        for i in range(50):
            popul[i] = selected[i][:]
            minFitness = minFit
            prevRow = currRow
