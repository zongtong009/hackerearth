a=0
b=0

temp=input()
for i in temp:
    if i =='L':
        a-=1
    elif i =='R':
        a+=1
    elif i =='U':
        b+=1
    else:
        b-=1
print(a,b)
