# 列表可以包含任何类型的
L = [123, 'spam', 1.23]
print(len(L))
print(L[1])
print(L[:-1])
L.append('NI')
L = L + [4,5,6]
print(L)
# remove the third item
L.pop(2)
print(L)
# ------------------------------
M = ['bb', 'cc', 'aa']
M.sort()
print(M)
M.reverse()
print(M)

# ---------------列表解析表达式
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])
col2 = [row[1] for row in matrix] # 显示第二列的数字
col3 = [row[1]+1 for row in matrix]
print(col2)
col2c = [row[1] for row in matrix if row[1]%2 == 0]
print(col2c)

# diag = [M[i][i] for i in [0, 1, 2]]

G = (sum(matrix[1]) for row in M)
print(G)
print(next(G))
print(list(map(sum, M)))