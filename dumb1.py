import copy

# Calculate the sum of all elements in a submatrix in constant time
# sum[i][j]: represents the sum of all elements in matrix from (0, 0) to (i, j)
# sum[i][j] = sum[i][j-1] + sum[i-1][j] + mat[i][j] - sum[i-1, j-1]
mat1 = [
    [0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4],
]

def process_sum_matrix(mat):
    """
    Returns a matrix that has sum of the matrix till position (i, j) 
    """
    rows = len(mat)
    cols = len(mat[0])
    sum_mat = [[-1 for j1 in range(cols)] for i1 in range(rows)]

    def valid_coord(i, j):
        if i < 0 or j < 0:
            return 0
        return sum_mat[i][j]

    for i in range(rows):
        for j in range(cols):
            sum_mat[i][j] = (
                mat[i][j] + 
                valid_coord(i, j-1) + 
                valid_coord(i-1, j) - 
                valid_coord(i-1, j-1)
            )

    # for part in sum_mat:
    #     print(part)

    return sum_mat

def sum_matrix_from_coords(mat, p, q, r, s):
    sum_matrix = process_sum_matrix(mat)

    def valid_coord(i, j):
        if i < 0 or j < 0:
            return 0
        return sum_matrix[i][j]

    sum_sub_matrix = (
        valid_coord(r, s) -
        valid_coord(p-1, s) -
        valid_coord(r, q-1) +
        valid_coord(p-1, q-1)
    )
    return sum_sub_matrix

def sum_matrix_from_coords2(sum_mat, p, q, r, s):

    def valid_coord(i, j):
        if i < 0 or j < 0:
            return 0
        return sum_mat[i][j]

    sum_sub_matrix = (
        valid_coord(r, s) -
        valid_coord(p-1, s) -
        valid_coord(r, q-1) +
        valid_coord(p-1, q-1)
    )
    return sum_sub_matrix


# Find max sum submatrix present in a matrix
mat2 = [
    [-5, -6, 3, 1, 0],
    [9, 7, 8, 3, 7],
    [-6, -2, -1, 2, -4],
    [-7, 5, 5, 2, -6],
    [3, 2, 9, -5, 1],
]

def fun_max_sum_submatrix(mat):
    M = len(mat)
    N = len(mat[0])
    
    max_sum = float('-inf')
    sum_mat = process_sum_matrix(mat)
    ai, aj, am, an = 0, 0, 0, 0
    for i in range(M):
        for j in range(M):
            for m in range(N):
                for n in range(N):
                    a1 = sum_matrix_from_coords2(sum_mat, i, j, m, n)
                    if a1 > max_sum:
                        max_sum = max(max_sum, a1)
                        ai, aj, am, an = i, j, m, n

    print(ai, aj, am, an)    
    return max_sum

# a1 = fun_max_sum_submatrix(mat2)
# print(a1)









































