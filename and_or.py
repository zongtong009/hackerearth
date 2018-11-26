def fact(integer):
    return integer > 1 and integer * fact(integer - 1) or 1


print(fact(50))
