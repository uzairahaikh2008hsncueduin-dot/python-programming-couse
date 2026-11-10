# # a = int(input("Enter your number: "))
# # b = int(input("Enter your number: "))
# # c = int(input("Enter your number: "))
 
# # average = (a + b + c)/3
# # print(average)

# # a = int(input("Enter your number: "))
# # b = int(input("Enter your number: "))
# # c = int(input("Enter your number: "))
 
# # average = (a + b + c)/3
# # print(average)

# # Function Definition
# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
    
#     average = (a + b + c)/3
#     print(average)


# avg() # Function Call
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# avg()





# def goodDay():
#     print("Good Day")

# goodDay()



# def goodDay(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "ok"

# a = goodDay("Harry", "Thank you") 
# print(a)




# def goodDay(name, ending="Thank you"):
#     print(f"Good Day, {name}")
#     print(ending)

# goodDay("Harry", "Thanks")
# goodDay("Rohan")




'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")