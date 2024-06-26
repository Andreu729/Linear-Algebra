from func import *

print("matriz original")
matrix = Matrix([[2, 2, 2], [1, 0, 0], [0, 0, 0]])
matrix.mprint()
print("=====================")
print("matriz reducida")
r_matrix = row_reduce(matrix)
r_matrix.set_precision(2)
r_matrix.mprint()
print("=====================")
print(null_space(matrix))
