def addition(x,y):
    summation = x + y
    return "The sum of {} and {} is {}".format(x,y,summation)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(addition(number1,number2))

def uppercase(message):
    return str(message).upper()
print(uppercase("Hello David"))