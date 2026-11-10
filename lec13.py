# def square(n):
#     return n*n 

square = lambda x: x*x

print(square(5))



a = ["Harry", "Rohan", "Shubham"]

final = "::".join(a)
print(final)    




a = "{1} is a good {0}".format("harry", "boy")

print(a)






from functools import reduce
# Map Example 
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example
def even(n):
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))