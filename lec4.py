# friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# print(friends[0])
# friends[0] = "Grapes" # Unlike Strings lists are mutable

# print(friends[0])
# print(friends[1:4])


# friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
# print(friends)
# friends.append("Harry")
# print(friends)

# l1 = [1, 34,62, 2, 6, 11]
# # l1.sort()
# # l1.reverse()
# # l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
# value = l1.pop(3)
# print(value)
# print(l1)


# a = (1,45,342,3424,False, "Rohan", "Shivam")
# print(a)
# print(type(a))


a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))