# d = {} # Empty dictionary
# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23
# }


# # print(marks, type(marks))
# print(marks["Harry"])



# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23,
#     0: "Harry"
# }

# # print(marks.items())
# # print(marks.keys())
# # print(marks.values())
# # marks.update({"Harry": 99, "Renuka": 100})
# # print(marks)

# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error



# e = set() # Dont use s = {} as it will create an empty dictionary
# s = {1, 5, 32, 54,5, 5, 5} 


# print(s)



# s = {1, 5, 32, 54,5, 5, 5, "Harry"}

# print(s, type(s))

# s.add(566)
# print(s, type(s))
# s.remove(1)
# print(s, type(s))



s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))