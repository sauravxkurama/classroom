input: Learning Python is very Easy 
output: Easy Very is Python Learning 
s=input("Enter Some String:") 
l=s.split() 
l1=[] 
i=len(l)-1 
while i>=0: 
l1.append(l[i]) 
i=i-1 
output=' '.join(l1) 
print(output) 
