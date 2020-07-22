num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))
num3=float(input("Enter number 3:"))
if (num1>num2) and (num1>num3):
    largestnum=num1
elif (num3>num1) and (num3>num2):
    largestnum=num3
else:largestnum=num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)
