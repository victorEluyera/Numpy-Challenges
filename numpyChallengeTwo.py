import numpy as np
from numpy import  random
# numpy create matrix with value range


arr=np.arange(15).reshape(3,5)

# print(arr)

# numpy get index of non zero elements

arr=np.array([0,2,3,0,9,0,0,7,6,0])

# print(np.nonzero(arr))

clearArr=np.zeros(arr)

# print(clearArr)


# numpy create identity matrix

identityMatrix=np.eye(7)

# print(identityMatrix)

# numpy create array with random values

randv=random.random(7)

# print(randv)

# numpy create matrix with random values

randMatrix=random.random((3,3))

# print(randMatrix)

# numpy matrix find min and max values

matrixMin=randMatrix.min()
matrixMax=randMatrix.max()
# print(f'Min({matrixMin}) and Max ({matrixMax})')

#numpy vector find mean value

randMatrixMean=randMatrix.mean()

# print(randMatrixMean)

#numpy array print number of dimensions


arr=np.array([[[ 0 , 1],
  [ 2 , 3],
  [ 4  ,5],
  [ 6  ,7],
  [ 8  ,9]],

 [[10 ,11],
  [12 ,13],
  [14 ,15],
  [16 ,17],
  [18 ,19]]]) #np.arange(20).reshape(2,5,2)

# print(arr.shape,arr.ndim)

#numpy create matrix of ones and zeroe

matrixOfOnes=np.ones((3,5))

matrixOfZeroes=np.zeros((3,6))

# print(matrixOfOnes)

#numpy create matrix of constant

arrCont=np.full((3,5),9)

# print(arrCont)

#numpy create matrix patterns v1

matrixPatv1=np.ones((8,5))

matrixPatv1[1:-1]=3

matrixPatv2=np.ones((8,8))

matrixPatv2[1:-1,1:-1]=0

# print(matrixPatv2)

#numpy create diagonal array


arr=np.array([9,9,9,9,9])

diagonalArr=np.diag(arr)

# print(diagonalArr)

arr=185 - np.arange(5*7)/5


saturday=arr[5::7]
sunday=arr[6::7]
print(np.add(saturday,sunday)/2)

print(arr)