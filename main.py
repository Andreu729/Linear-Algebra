from classf import Matrix, max_finder
imatrix = Matrix([[1, 0], [0, 1], [1, 0], [4, 5]])
print(imatrix.matrix)
print(imatrix.row_amount)
print(imatrix.col_amount)
print("=================")
a = [[111, 0], [0, 1], [-178, 0], [4, 5]]
b = max_finder(a, 1)
print(b)
