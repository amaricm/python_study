# def indef_of(m, n):
#     for a in range(0 , len(m)):
#         for b in range(0 , len(m[a])):
#             if m[a][b] == n:
#                 return [a,b]
#     return [-1, -1]
# ma =[[8, 14, -6], [12,7,4], [-11,3,21]]
# print(indef_of(ma, 14))





def did_someone_win_tic_tac_toe(m):
    for a in range(0 , len(m)):
        for b in range(0, len(m[a])):
            if b+2 < len(m[a]) and m[a][b] == m[a][b+1] and m[a][b] ==m[a][b+2]:
                return "Winner"

            # if (m[a][b] == "x" and m[a][b+1] == "x" and m[a][b+2] == "x") or (m[a][b] == "o" and m[a][b+1] == "o" and m[a][b+2] == "o"):
            #     return "Winner"
            # if (m[a][b] == "x" and m[a+1][b] == "x" and m[a+2][b] == "x") or (m[a][b] == "o" and m[a+1][b] == "o" and m[a+2][b] == "o"):
            #     return "Winner"
            # if (m[0][0] == "x" and m[1][1] == "x" and m[2][2] == "x") or (m[0][0] == "o" and m[1][1] == "o" and m[2][2] == "o"):
            #     return "Winner"
  
            
    return " No Winner"

ma =[["o","x","o"], ["o","x","x"], ["x","x","x"]]
print(did_someone_win_tic_tac_toe(ma))


