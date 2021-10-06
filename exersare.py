C=[[1,2,3,4,5],
  [11,12,13,14,15],
  [21,22,23,24,25],
  [31,32,33,34,35],
  [41,42,43,44,45]]
for i in range(len(C)):
    print('Suma elementelor liniei',i,'=',sum(C[i]))
for i in range(len(C)):
    s_coloane=0
    for j in range(len(C[0])):
        s_coloane+=C[j][i]
    print('Suma elementelor coloanei',i,'=',s_coloane)
d_principala=[]
d_secundara=[]
for i in range(len(C)):
    for j in range(len(C[0])):
        if i==j:
            d_principala.append(C[i][j])
        if(i+j)==(len(C)-1):
            d_secundara.append(C[i][j])
print('Diagonala principala=',d_principala)
print('Diagonala secundara=',d_secundara)