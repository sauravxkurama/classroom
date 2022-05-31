x = int(input("Enter the no. of elements:"))
a=[]
for i in range(x):
    y = int(input("Enter the elements:"))
    a.append(y)
i = 0
j = x-1
while(i<j):
    t = a[i]
    a[i]=a[j]
    a[j]=t
    i = i+1
    j = j-1
print("Reversed list=")
for i in range(x):
    print(a[i])
