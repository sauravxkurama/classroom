list1 = []
list2= []
num1 = int(input("How many numbers:"))
num2 = int(input("How many numbers:"))
for n in range(num1):
    number= int(input("Enter the number:"))
    list1.append(number)
for n in range(num2):
    number= int(input("Enter the number:"))
    list2.append(number)
a = list1[0]
list1[0]=list2[num2-1]
list2[num2-1]= a
print("list1...",list1)
print("list2...",list2)
