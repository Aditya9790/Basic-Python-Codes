n=int(input("Enter the number of rows: "))
for i in range (n):
    for j in range (n):
        if (i-j==0 or i+j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()