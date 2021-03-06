import EQL
####Initialise QTable####
#Mission: go to the house without run over the human
#Game grid
Grid = [#1 = House, -1 = Human
    [0,0,1],
    [0,-1,0],
    [0,0,0]
]

#First car position coordinates
x = 0
y = 2
#Current state
state = 7
#Action list and travel coordinate
actions = [
    [-1, 0], # Up
    [1, 0], #Down
    [0, -1], # Left
    [0, 1] # Right
]

#Make QTable
Qtable = EQL.QLearning(nbAction=4)

####Train the QTable####
#100 games
for _ in range(100):
    #Reset the car position
    x = 0
    y = 2
    #Default state
    state = 7
    #While the car are not in the house
    while x != 2 or y != 0:
        #Display the grid
        print("---------------------")
        yTemp = 0
        for line in Grid:
            xTemp = 0
            for pt in line:
                print("%s\t" % (pt if yTemp != y or xTemp != x else "X"), end="")
                xTemp += 1
            yTemp += 1
            print("")
        #Choose an action
        action = Qtable.takeAction(str(state),epsilon=0.4)
        #Move the car
        y = max(0, min(y + actions[action][0],2))
        x = max(0, min(x + actions[action][1],2))
        #Calcul the position in the grid (state)
        newState = (y*3+x+1)
        #Get the reward of the position
        reward = Grid[y][x]
        print("state : ", newState)
        print("reward : ", reward)
        #Update Q function
        Qtable.updateQFunction(str(newState),str(state),reward)
        #Next state
        state = newState
#Display the QTable
for s in range(0, 9):
    print(s, Qtable.QTable[s])

#Save my QTable in myTable.npz
Qtable.saveQTable("myTable")

#Load my QTable from myTable.npz
Qtable.loadQTable("myTable")