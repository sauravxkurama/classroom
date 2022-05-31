
dict={}
for i in range(5):
    roll=int(input())
    name=input()
    marks=int(input())
    dict.update({roll:{name:marks}})
print(dict)
sum=0
for i in dict.values():
    for j in i:
        sum+=i[j]
print(sum)
