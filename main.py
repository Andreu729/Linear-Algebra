from func import *

print("matriz original")
matrix = Matrix([[3, 5, 4, 9], [2, -4, -4, -4], [2, 3, 2, 5]])
matrix.mprint()
print("=====================")
print("matriz reducida")
r_matrix = row_reduce(matrix)
pivots = row_reduce(matrix, set_option=2)
r_matrix.set_precision(2)
r_matrix.mprint()
print("=====================")
print(pivots)
