a = -1
#lets chheck whether a is even 
if a % 2 == 0:
    print("{} is even".format(a))
else:
    print("{} is odd".format(a))
    
if a < 10 and a >= 0:
    print("{} is greaterthan or equal to zero and less than 10".format(a))
elif a >= 10 and a < 20:
    print("{} is between 10 and 20".format(a))
elif a >=20:
    print("{} is equal to or greater than 20".format(a))
else:
    print("{} is lessthan 0".format(a))