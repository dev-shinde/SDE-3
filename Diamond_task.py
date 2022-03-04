rows=int(input("enter no of rows:"))
k=rows-1
for i in range(rows):
    for s in range(k,0,-1):
        print(end=" ")
    k=k-1
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

k=rows-(rows-1)
for n in range(rows):
    for r in range(k,0,-1):
        print(end=" ")
    k=k+1
    for p in range(i):
        print("*",end=" ")
    print(" ")
    i=i-1

