import random

regen, findspot = 'Y', 'Y'
count = 0

def gridSum(grid):
    summed = 0
    for x in range(0,len(grid),1):
        summed = summed + sum(grid[x])
    return(summed)

def findParking(grid):
    checked = 0
    spotfound = False
    gridsize = len(grid)**2
    
    for i in range(0,len(grid),1):
        if spotfound == False and checked <= gridsize:
            for j in range(0,len(grid),1):
                if grid[j][i] == 0 and spotfound == False:
                    grid[j][i] = 1
                    checked += 1
                    spotfound = True
                    #print("Checked, found spot.")
                    exit
                elif grid[j][i] == 1 and spotfound == False:
                    checked += 1
                    #print("Checked, spot unavailable.")
                    continue
        else:
            exit
            
    return(grid)

def printGrid(grid):
    for x in range(0,len(grid),1):
        print("\n{}\n".format(grid[x]))
    return None

while regen == 'Y' or regen == 'y':
    n = int(input("Enter a grid size: "))
    grid = [[random.randrange(0,2,1) for x in range(1,n+1,1)]
         for x in range(1,n+1,1)]
    printGrid(grid)
    regen = input("Regenerate grid? (Y/N): ")

gridsize = int(len(grid)**2)
gridsum = gridSum(grid)

whichwhile = input("Want to do things manually? (Y/N): ")

if (whichwhile == 'N' or whichwhile == 'n'):
    while (gridsum < gridsize):
        count += 1
        grid = findParking(grid)
        gridsum = gridSum(grid)

if (whichwhile == 'Y' or whichwhile == 'y'):
    while (findspot == 'Y' or findspot == 'y'):   
        findspot = input("Find parking? (Y/N): ")
        grid = findParking(grid)
        printGrid(grid)
        gridsum = gridSum(grid)
        grid_diff = gridsize-gridsum
        count = gridsum
        print("{} spots are taken. {} remain.".format(gridsum,grid_diff))

print("\n{} spots have been filled. The parking lot is now full.".format(count))
print("\nFinal grid: ")
printGrid(grid)
