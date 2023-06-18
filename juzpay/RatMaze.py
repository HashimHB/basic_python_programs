N = 4
def checkPosition(M, x, y):
    if x >= 0 and x < N:
        if y >= 0 and y < N:
            if M[x][y] == 1:
                return True
    return False
def solveMaze(M):
    sol = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
    if Rat_maze_sol(M, 0, 0, sol) == False:
        return False

    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")
    return True

def Rat_maze_sol(M, x, y, sol):
    if x == N-1 and y == N-1 and M[x][y] == 1:
        sol[x][y] = 1
        return True

    if checkPosition(M, x, y) == True:
        if sol[x][y] == 1:
            return False

        sol[x][y] = 1

        if Rat_maze_sol(M, x+1, y, sol) == True:
            return True

        if Rat_maze_sol(M, x, y+1, sol) == True:
            return True

        if Rat_maze_sol(M, x-1, y, sol) == True:
            return True

        if Rat_maze_sol(M, x, y-1, sol) == True:
            return True

        sol[x][y] = 0
        return False


M = [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 1, 1]]
print(N)
solveMaze(M)
