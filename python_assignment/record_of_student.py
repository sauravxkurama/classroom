rec = {}
n = int(input("Enter the no. of students:"))
i = 1
while i<=n :
    name = input("Enter the name of the student:")
    marks = int(input("Enter the % of student:"))
    rec.update({name:marks})
    i = i + 1
key = input("Enter the name of the student:")
if key in rec:
    print('Name=',key,"Marks=",rec[key])
else:
    print("Name not found!")
