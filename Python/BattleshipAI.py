# Importing modules
import random
# Setting variables
grid = []
gr = []
bullets = []
boat1 = True
boat2 = True
boat3 = True
boat4 = True
boat5 = True
largest = 0
xalpha = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j"}
xbeta = {v: k for k, v in xalpha.items()}
# Making grid
def makegrid() :
    for i in range(0, 10) :
        gr.append(0)
    for i in range(0, 10) :
        grid.append(gr.copy())
# Defining boat 5
def boat_5() :
    for a in range(0, 6) :
        for b in range(0, 10) :
            if grid[a][b] != -1 and grid[a+1][b] != -1 and grid[a+2][b] != -1 and grid[a+3][b] != -1 and grid[a+4][b] != -1 :
                grid[a][b] += 1
                grid[a+1][b] += 1
                grid[a+2][b] += 1
                grid[a+3][b] += 1
                grid[a+4][b] += 1
    for a in range(0, 10) :
        for b in range(0, 6) :
            if grid[a][b] != -1 and grid[a][b+1] != -1 and grid[a][b+2] != -1 and grid[a][b+3] != 1 and grid[a][b+4] != -1 :
                grid[a][b] += 1
                grid[a][b+1] += 1
                grid[a][b+2] += 1
                grid[a][b+3] += 1
                grid[a][b+4] += 1
# Defining boat 4
def boat_4() :
    for a in range(0, 7) :
        for b in range(0, 10) :
            if grid[a][b] != -1 and grid[a+1][b] != -1 and grid[a+2][b] != -1 and grid[a+3][b] != -1 :
                grid[a][b] += 1
                grid[a+1][b] += 1
                grid[a+2][b] += 1
                grid[a+3][b] += 1
    for a in range(0, 10) :
        for b in range(0, 7) :
            if grid[a][b] != -1 and grid[a][b+1] != -1 and grid[a][b+2] != -1 and grid[a][b+3] != -1 :
                grid[a][b] += 1
                grid[a][b+1] += 1
                grid[a][b+2] += 1
                grid[a][b+3] += 1
# Defining boat 3
def boat_3() :
    for a in range(0, 8) :
        for b in range(0, 10) :
            if grid[a][b] != -1 and grid[a+1][b] != -1 and grid[a+2][b] != -1 :
                grid[a][b] += 1
                grid[a+1][b] += 1
                grid[a+2][b] += 1
    for a in range(0, 10) :
        for b in range(0, 8) :
            if grid[a][b] != -1 and grid[a][b+1] != -1 and grid[a][b+2] != -1 :
                grid[a][b] += 1
                grid[a][b+1] += 1
                grid[a][b+2] += 1
# Defining boat 2
def boat_2() :
    for a in range(0, 9) :
        for b in range(0, 10) :
            if grid[a][b] != -1 and grid[a+1][b] != -1 :
                grid[a][b] += 1
                grid[a+1][b] += 1
    for a in range(0, 10) :
        for b in range(0, 9) :
            if grid[a][b] != -1 and grid[a][b+1] != -1 :
                grid[a][b] += 1
                grid[a][b+1] += 1
# Making grid and some stuff
makegrid()
print("          #############################")
print("          #######               #######")
print("          ####### BATTLESHIP AI #######")
print("          #######               #######")
print("          #############################")
print()
# Main Loop
while boat1 or boat2 or boat3 or boat4 or boat5 :
    big_boys = []
    largest = 0
    # Filling grid with zeros
    for a in range(0, 10) :
        for b in range(0, 10) :
            grid[a][b] = 0
    # Placing shot bullets
    for bullet in bullets :
        grid[int(bullet[0])][int(bullet[1])-1] -= 1
    # Boat check
    if boat1 :
        boat_2()
    if boat2 :
        boat_3()
    if boat3 :
        boat_3()
    if boat4 :
        boat_4()
    if boat5 :
        boat_5()
    # Finding the largest amount
    for a in range(0, 10) :
        for b in range(0, 10) :
            if grid[a][b] > largest :
                largest = grid[a][b]
    # Appending the coordinates to the big boy list
    for a in range(0, 10) :
        for b in range(0, 10) :
            if grid[a][b] == largest :
                big_boys.append([a, b])
    # Selcting a random coordinate from the big boys list
    if len(big_boys) > 1 :
        if big_boys:
            chosen_coordinates = random.choice(big_boys)
            out = xalpha[chosen_coordinates[0]] + str(chosen_coordinates[1])
        else:
            print("No valid coordinates found.")
            break
    else :
        if big_boys:
            out = xalpha[big_boys[0][0]] + str(big_boys[0][1])
        else:
            print("No valid coordinates found.")
            break
    # Printing the move
    print(out)
    # Asking input for fired bullets
    while True :
        bllt = input("Enter fired : ")
        if bllt != "x" :
            bllt = list(bllt)
            bullets.append([xbeta[bllt[0]], bllt[1]])
        else :
            break
    # Asking inputs for completely broken boats
    bts = input("Boats broken? : ")
    if bts == "x" :
        pass
    elif bts == "1" :
        boat1 = False
    elif bts == "2" :
        boat2 = False
    elif bts == "3" :
        boat3 = False
    elif bts == "4" :
        boat4 = False
    elif bts == "5" :
        boat5 = False
    # Printing a blank line
    print()

print("!!! YOU WIN !!!")
