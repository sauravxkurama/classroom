def isanagram(str1,str2):
    str1= str1.lower()
    str2 = str2.lower()
    if(len(str1)==len(str2)):
        x= sorted(str1)
        y = sorted(str2)
        if(x==y):
            print("Yes it is anagram")
        else:
            print("No it is not anagram")
    else:
        print("No it is not anmagram")
isanagram(input(),input())
