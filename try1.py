count=0
with open("books.txt","r") as file:
    for l in file:
        count+=1
    print(count)
