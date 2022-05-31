list = []
num = int(input("How many numbers:"))
for n in range(num):
    number= int(input("Enter the number:"))
    list.append(number)
s= 0
for n in list:
    s = s + n
print("sum=",s)
