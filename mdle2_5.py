def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        mtrx = []
        for j in range(m):
            mtrx.append(value)
        matrix.append(mtrx)
    return matrix


result1 = get_matrix(3,3,17)
result2 = get_matrix(5,2,30)
result3 = get_matrix(4,5,11)
print(result1)
print(result2)
print(result3)
