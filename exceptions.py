try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("you can not divide a number by 0, error {}".format(e))
print("hello david")

try:
    print(name)
except NameError as e:
    print("Err {}".format(e))
else:
    #if nothing wrong happened with the programe
    print("name is now valid")
finally:
    #finally, this will always execute
    print("I will always run irrespective of the above")
    
