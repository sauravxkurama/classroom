i = int(input("Enter the Number:"))
org = i
rev = 0
while(i>0):
    rev = (rev*10)+(i%10)
    i = i // 10
if(org==rev):
    print("Yes!")
else:
    print("NO!")
