ch = str(input("Enter the letter:"))
for i in range(1,6):
    for j in range(1,6):
        if ch == "A":
            if (i == 1 or j == 1 or j == 5 or i ==5// 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch == "C":
            if (i == 1 or i == 5 or j == 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch=="D":
            if (i==1 or j==1 or i==5 or j==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch=="E":
            k=round(5/2)+1
            if (i==1 or j==1 or i==5 or i==k):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch=="F":
            if (i==1 or j==1 or i==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch=="H":
            if (j==1 or i==3 or j==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch=="I":
            if (i==1 or i==5 or j==3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

for i in range(1,6):
    for j in range(1,6):
        if ch=="J":
            if (i+j==6 or j==3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
































