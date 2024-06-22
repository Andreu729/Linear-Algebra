from func import *

print("matriz original")
matrix = Matrix([[3, 5, 4, 9], [2, -4, -4, -4], [2, 3, 2, 5]])
q = transpose(matrix)
matrix.mprint()
print("=====================")
print("matriz reducida")
r_matrix = row_reduce(matrix)
r_matrix.set_precision(2)
r_matrix.mprint()
print("=====================")
q.mprint()
