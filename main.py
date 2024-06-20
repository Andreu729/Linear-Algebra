from func import *

print("matriz original")
matrix = Matrix([[1, 2, 3, 4, 5], [5, -4, 3, 2, 0], [0, 0, 3, 2, 1], [0, 2, -2, 1, -1]])
matrix.mprint()
print("=====================")
print("matriz reducida")
r_matrix = row_reduce(matrix)
r_matrix.mprint()
