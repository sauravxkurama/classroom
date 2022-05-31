a = input("Enter Your Name:")
vowel = 0
cons = 0
digit = 0 
special = 0 
fg="aeiouAEIOU"
for i in range(0,len(a)):
    chr = a[i]
    if(a[i] in fg):
        print(a[i],end="")
        vowel+=1
    else:
        cons+=1
  elif(chr>='0' or chr<='9'):
        digit += 1
  else:
        special += 1
    

print()
print("Vowel=",vowel,"Consonent=",cons,"digit=",digit,"special=",special)
