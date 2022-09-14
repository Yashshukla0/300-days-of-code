a=input()  
s=''
l=a.split(".")
for i in l:
    s+=i+"[.]"
print(s.strip("[.]"))