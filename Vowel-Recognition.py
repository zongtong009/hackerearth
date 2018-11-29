# t=int(input())
# l=['A','E','I','O','U','a','e','i','o','u']
# for i in range (t):
    # ans=0
    # s=input()
    # for j in range (len(s)):
        # if s[j] in l:
            # ans+=((len(s)-j)*(j+1))
    # print (ans)
def fun1(string):
    # l=['A','E','I','O','U','a','e','i','o','u']
    s=string
    sum=0
    for i in range(len(s)):
        if s[i] in 'aeouiAEOUI':
            sum+=(len(s)-i)*(i+1)
    return sum
    
def fun2(s):
    sum = 0
    len_a = len(s)
    for i in range(len_a+1):
        for j in range(i, len_a):
            for k in s[i:][: len_a - j]:
                if k in 'aeouiAEOUI':
                    sum += 1
    return sum
    
a=int(input())
for i in range(a):
    s=input()
    print(fun(s))
    