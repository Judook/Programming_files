overboard = []
row = []
underboard = []

def makegrid(a, b, row, grid) :
    for i in range(0, a) :
        row.append("█")
    for i in range(0, b) :
        grid.append(row)
        
def showgrid(grid) :
    for r in range(0, len(grid)) :
        for rr in range(0, len(grid[r])) :
            print(grid[r][rr], end="  ")
            
        print("<-" ,r ,"\n")

makegrid(9, 9, row, overboard)
#while True:
showgrid(overboard)


