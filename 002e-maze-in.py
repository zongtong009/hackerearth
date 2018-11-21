a=0
b=0

def get_sum(string):
    s=string
    lt=[]
    for i in s[::-1]:
        if i in 'aeouiAEOUI':
            lt.append(1)
        else:
            lt.append(0)
    return lt
def sun(list):
    lt=list
    