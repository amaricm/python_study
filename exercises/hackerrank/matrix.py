

# #first diagonal
# >>> n = 3
# >>> [(i, n-i-1) for i in range(n)]
# #second diagonal
# >>> sum(a[i][n-i-1] for i in range(n))


def matr_sum(ma_1, ma_2):
    ma_3 = []
    if  len(ma_1) == 0:
        raise Exception("Matrix can not be empty")
                   
    for a in range(0, len(ma_1)):
        ma_3.insert(a, [])
        for b in range(0, len(ma_1[a])):
            ma_3[a].insert(b, ma_1[a][b] + ma_2[a][b])
    return ma_3

#print(matr_sum([[2,3,4], [5,8,1], [5,6,7]], [[1,1,1], [1,1,1], [1,1,1]]))

    
def is_prime(n):
    for x in range(2, n**1/2):
        if n%x == 0:
            return False
    return True

print(is_prime(12))       
