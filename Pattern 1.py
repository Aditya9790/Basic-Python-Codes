n=int(input("Enter the number:"))
for i in range(n):
    print("*"*(i+1),end=" ")
    print()

for j in range(n-1):
    print("*"*(n-1-j),end=" ")
    print()
