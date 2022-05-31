d={}
x=int(input())
for i  in range (x):
    k=int(input())
    v=int(input())
    d.update({k:v})
sum=0
for i in d.keys():
    sum+=i
print(sum)
