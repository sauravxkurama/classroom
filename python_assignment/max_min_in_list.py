x = int(input("Enter the no. of elements:"))
a=[]
for i in range(x):
    y = int(input("Enter the elements:"))
    a.append(y)
min = a[0]
for i in range(x):
    if(a[i]<min):
       min = a[i]
print("Minium",min)
