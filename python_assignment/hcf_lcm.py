a = int(input('enter the first number'))
b = int (input('enter the second number'))
if (a>b):
        small = b
else:
         small = a
for i in range (1 ,small +1):
            if ( a% i==0  and b% i ==0):
            hcf = i
            break 


lcm =(a*b)//hcf
print ("LCM=",lcm  "HCF=",hcf) 
