import random as rnd
import copy

class GameOfLife():
    matrix = []
    def __init__(self,N):
        self.N = N
        GameOfLife.matrix = []

    def bulidrandommatrix(self):

        for i in range(self.N):
            row = []
            for j in range(self.N):
                if i == 0 or i == self.N - 1 or j == 0 or j == self.N - 1:
                    x =0
                else:
                    x = rnd.randint(0,1)
                row.append(x)
            GameOfLife.matrix.append(row)
        return GameOfLife.matrix

    def check8neighbours(self,i,j):
        if i == 0 or i == self.N-1 or j == 0 or j == self.N -1:
            return False
        return True

    def check8neighbourshas2or3celalive(self, i, j):
        count =0
        if GameOfLife.matrix[i][j-1] == 1:
            count += 1
        if GameOfLife.matrix[i][j+1] == 1:
            count += 1
        if GameOfLife.matrix[i-1][j-1] == 1:
            count += 1
        if GameOfLife.matrix[i-1][j] == 1:
            count += 1
        if GameOfLife.matrix[i-1][j+1] == 1:
            count += 1
        if GameOfLife.matrix[i+1][j-1] == 1:
            count += 1
        if GameOfLife.matrix[i+1][j] == 1:
            count += 1
        if GameOfLife.matrix[i+1][j+1] == 1:
            count += 1
        if count >= 2 and count <= 3:
            return True
        else:
            return False

    def updatematrix(self ,i ,j,result):
        GameOfLife.matrix[i][j] =result

    def printMatrix(self):
        for i in range(self.N):
                print(GameOfLife.matrix[i])
    def checkifcanplay(self):
        count =0
        for i in GameOfLife.matrix:
            for j in i:
                if j != 0:
                    count+=1
        if count >= 2:
            return True
        return False

    def play(self):
        if GameOfLife.checkifcanplay(self):
            matrixhelp =copy.deepcopy(GameOfLife.matrix)
            for i in range(self.N):
                for j in range(self.N):
                    if GameOfLife.check8neighbours(self,i,j):
                        if not GameOfLife.check8neighbourshas2or3celalive(self,i,j):
                            matrixhelp[i][j] = 0
                        else:
                            matrixhelp[i][j] = 1
            GameOfLife.matrix = copy.deepcopy(matrixhelp)


if __name__ == '__main__':
    g = GameOfLife(5)
    g.bulidrandommatrix()
    print('first')
    g.printMatrix()
    print('\n')
    found =0
    while True:
        if g.checkifcanplay():
            g.play()
            g.printMatrix()
            print('\n')
            found =1
        else:
            if found != 1:
                g = GameOfLife(5)
                g.bulidrandommatrix()
                print('second')
                g.printMatrix()
                print('\n')
            else:
                exit()