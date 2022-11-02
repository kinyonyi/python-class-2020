#set methods
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#Adds an element to the set
print(fruits)


fruits = {"apple", "banana", "cherry"}
#Removes all the elements from the set
fruits.clear()
print(fruits)


fruits = {"apple", "banana", "cherry"}
#Returns a copy of the set
x = fruits.copy()
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
#Return a set that contains the items that only exist in set x, and not in set y
z = x.difference(y)

x = {"apple", "juice", "banana", "cherry"}
y = {"google","juice", "microsoft", "apple"}
x.difference_update(y)
#Remove the items that exist in both sets
print("this is the difference")
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#discard a banana from the set
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
#Returns a set, that is the intersection of two or more sets
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
#Remove the items that is not present in both x and y, returns set on only similar items
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
#Returns whether two sets have a intersection or not
z = x.isdisjoint(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
#Returns whether another set contains this set or not
z = x.issubset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
#Returns whether this set contains another set or not
z = x.issuperset(y)
print(z)

fruits = {"apple", "banana", "cherry"}
fruits.pop()
#Removes a random element from the set
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#removes an item from a set
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
#returns the union of two sets
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
#Return a set that contains all items from both sets, except items that are present in both sets:
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
#Remove the items that are present in both sets, AND insert the items that is not present in both sets:
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
#updates a set with another set
print(x)