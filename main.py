from func import *

print("matriz original")
matrix = Matrix([[2, 2, 0], [1, 0, 0], [0, 0, 0]])
matrix.mprint()
print("=====================")
print("matriz reducida")
r_matrix = row_reduce(matrix)
r_matrix.set_precision(2)
r_matrix.mprint()
print("=====================")
solution = linear_solve(matrix, b=[7, -64, 0])
print(solution)
