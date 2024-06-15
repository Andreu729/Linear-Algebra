from func import *

imatrix = Matrix([[1, 0, 5, 5], [0, 1, 3, -3], [1, 0, 1670, -47]])
imatrix.mprint()
print("=====================")
n_matrix = row_operation(imatrix, 3, 1, -1)
n_matrix.mprint()
