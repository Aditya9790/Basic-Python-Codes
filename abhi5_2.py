# additon ,subtaction and multiplication of matrices

r1= int(input('r1'));r2=int(input('r2'))
c1=int(input('c1'));c2=int(input('c2'))
A=[[int(input('entry for A:')) for j in range(c1)] for i in range(r1)]
[[print( A[i][j],end='') for j in range(c1)]+[print()] for i in range(r1)]
B=[[int(input('entry for B:')) for j in range(c2)] for i in range(r2)]
[[print (B[i][j],end='') for j in range(c2)]+[print()] for i in range(r2)]
if r1==r2 and c1==c2:
   add=[[ A[i][j]+B[i][j] for j in range(c2)] for i in range(r2)]
   sub=[[ A[i][j]-B[i][j] for j in range(c2)] for i in range(r2)]
   print('addition is\n',add,'\n subtraction is\n',sub)
else:
    print('addition and subtraction is not possible')
if c1==r2:
    c=[]
    c=[[[ c+A[i][k]*B[k][j] for k in range(r2) ]for j in range(c2)] for i in range(r1)]
    print('multiplication is')
    [[print(c[i][j]) for j in range(c2)] for i in range(r1)]
else:
    print('multiplication is not possible')
