#Calculating the time for a program to run.
from time import time
start_time = time()
n = int(input("Enter a number:"))
for i in range(n):
    print(i)
end_time = time()
elapsed = end_time - start_time
print("Time elapsed is", elapsed)
print("start",start_time)
print("end",end_time)