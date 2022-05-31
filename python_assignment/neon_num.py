a=int(input('Enter a number :'))
sq=a*a
sum=0
while(sq>0):
    sum=sum+sq%10
    sq=sq//10
if(sum==a):
    print('YES IT IS NEON NUMBER')
else:
    print('NO IT IS NOT NEON NUMBER')
