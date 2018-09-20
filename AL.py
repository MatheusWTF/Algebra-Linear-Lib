#####################################################
#                    IMPORTS                        #
#####################################################
from math import cos, sin, pi

#####################################################
#                    CLASSES                        #
#####################################################
class Matrix:
    def __init__(self, nrow, ncol, listVal ):
        self.cols = ncol
        self.rows = nrow
        self.angle = 0

        self.matrix = []
        if (self.rows * self.cols) == len(listVal):
            for y in range(self.rows):
                row = []
                for x in range(self.cols):
                    ind = (y*self.cols) + x
                    row.append(listVal[ind])
                self.matrix.append(row)

    def matmul(self, b):
        if self.cols != b.rows:
            print("Rows of B do not match Cols of Matrix!")
            return self
        else:
            listRes = []
            for i in range(self.rows):
                for j in range(b.cols):
                    sum = 0
                    for k in range(b.rows):
                        sum += self.matrix[i][k] * b.matrix[k][j]
                    listRes.append(sum)
            return Matrix(self.rows, b.cols, listRes)
        
    def mult(self, b):
        res = []
        for row in self.matrix:
            for val in row:
                res.append(val*b)
        return Matrix(self.rows, self.cols, res)
    
    def transpose(self):
        res = [ [0] * self.rows] * self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                res[j][i] = self.matrix[i][j]
        return Matrix(self.cols, self.rows, res)
    
    def toString(self):
        res = '{} x {} Matrix\n'.format(self.rows, self.cols)
        res += '-------------------\n'
        for i in range(self.rows):
            for j in range(self.cols):
                res += '{} '.format(str(self.matrix[i][j]).rjust(5, " "))
            res += '\n'
        res += '-------------------\n'
        return res

#####################################################
#                   INSTANCES                       #
#####################################################
Project3D = Matrix(3, 4, [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0])
Project2D = Matrix(2, 3, [1, 0, 0, 0, 1, 0])

#####################################################
#                   FUNCTIONS                       #
#####################################################
### Mapping Numbers
def twoPoints(inMin, inMax, outMin, outMax):
    def f(x):
        return (x - inMin)/(inMax - inMin) * (outMax - outMin) + outMin
    return f

### Rotation 3D Matrix around X axis
def RotationX(degree):
    angle = degree * (pi/180)
    return Matrix(3, 3, [1, 0, 0, 0, cos(angle), -sin(angle), 0, sin(angle), cos(angle)])

### Rotation 3D Matrix around Y axis
def RotationY(degree):
    angle = degree * (pi/180)
    return Matrix(3, 3, [cos(angle), 0, sin(angle), 0, 1, 0, -sin(angle), 0, cos(angle)])

### Rotation 3D Matrix around Z axis
def RotationZ(degree):
    angle = degree * (pi/180)
    return Matrix(3, 3, [cos(angle), -sin(angle), 0, sin(angle), cos(angle), 0, 0, 0, 1])

### Create Projection Matrix for 4D Rotations
def makeProjection4D(distance, ma):
    weight = 1 / (distance - ma.matrix[3][0])
    return Matrix(3, 4, [weight, 0, 0, 0, 0, weight, 0, 0, 0, 0, weight, 0])

### Rotation 3D Matrix around WX axis
def RotationXW(degree):
    angle = degree * (pi/180)
    return Matrix(4, 4, [cos(angle), 0, 0, -sin(angle), 0, 1, 0, 0, 0, 0, 1, 0, sin(angle), 0, 0, cos(angle)])
