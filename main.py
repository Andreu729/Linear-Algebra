from func import *

imatrix = Matrix([[1, 0, 5, 5], [0, 1, 3, -3], [1, 0, 1670, -47]])
print(imatrix.matrix)
print(imatrix.row_amount)
print(imatrix.col_amount)
print("=================")
xd = imatrix.matrix_form
imatrix.mprint()
n_matrix = column_extend(imatrix, [0, -1, 2])
n_matrix.mprint()
