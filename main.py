from func import *

imatrix = Matrix([[0, 1, 5, 5], [1, 1, 3, -3], [1, 0, 1670, -47]])
imatrix.mprint()
print("=====================")

n_matrix = row_operation(imatrix, changed_row=2, scalar=1, changer_row=1)

n_matrix.mprint()
print("=====================")
r_matrix = single_row_reduce(n_matrix, col=1, last_pivot_row=0)
r_matrix.mprint()
