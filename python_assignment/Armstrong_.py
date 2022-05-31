n=int(input())
sum=0
order=len(str(n))
copy = n
while(n>0):
    digit=n%10
    sum += digit**order
    n=n//10
    if(sum==copy):
        print("it's an armstrong no.")
    else:
        print("it's not an armstrong no.")
