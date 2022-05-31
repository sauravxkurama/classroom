list = []
num = int(input("How many numbers:"))
for n in range(num):
    number= int(input("Enter the number:"))
    list.append(number)
even=0
odd = 0
for i in range(num):
    if (list[i]%2==0):
        even = even + list[i]
    else:
        odd = odd + list[i]
print("Sum of even:",even)
print("Sum of odd:",odd)
