a = input("Enter the string:")  
y = a.split()
s = list(filter(lambda y : True if int(y)%2==0 else False , y ))
print("All even no. are:",s)
