dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)
dict1={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict1.update({keys:values})
print(dict1)

dict2={}
for i in (dict,dict1):
    dict2.update(i)
print(dict2)
