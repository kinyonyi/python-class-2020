import random
print(random.random())#return float btn 0 to 1
#return random values btn 2 and 8
randomised = random.randint(2, 8)
print(randomised)
fruits = ['mangoes','guava','tomatoes','onions']
print(random.choice(fruits))
print(random.randrange(100, 200, 15))