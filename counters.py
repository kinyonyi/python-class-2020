#we have a for loop and we have a while loop
ending_number = int(input("Enter a number: "))
x = 0
while(x <= ending_number):
    print(x)
    x += 1
even_numbers = []
odd_numbers = []
for y in range(0, ending_number):
    if y % 2 == 0:
        print("{} is even".format(y))
        even_numbers.append(y)
    else:
        print("{} is odd".format(y))
        odd_numbers.append(y)
    #print(y)
print(even_numbers)
print(odd_numbers)