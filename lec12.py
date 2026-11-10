# # Using walrus operator 
# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)


# from typing import List, Union, Tuple 

# n : int = 5

# name: str = "Harry"


# def  sum(a: int, b: int) -> int:
#     return a+b



# def http_status(status): 
#     match status:  
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"  


# print(http_status(5007))




# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except ValueError as v:
#     print("Heyyyy")
#     print(v)
    
# except Exception as e:
#     print(e) 

# print("Thank You")




# a = int(input("Enter a number: "))
# b = int(input("Enter second number: "))

# if(b == 0):
#     raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
# else:
#     print(f"The division a/b is {a/b}")






# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

    
# except Exception as e:
#     print(e) 


# else:
#     print("I am inside else")




# def main():
#     try:
#         a = int(input("Hey, Enter a number: "))
#         print(a)
#         return

        
#     except Exception as e:
#         print(e) 
#         return


#     finally:
#         print("Hey I am inside of finally")


# main()




# from module import myFunc



# a = 89

# def fun(): 
#     # global a
#     a = 3
#     print(a)


# fun()
# print(a)




# l = [3, 513, 53, 535]

# # index = 0
# # for item in l:
# #     print(f"The item number at index {index} is {item}")
# #     index += 1

# # This can be simplified using enumerate function

# for index, item in enumerate(l):
#     print(f"The item number at index {index} is {item}")





# myList = [1, 2, 9, 5, 3, 5]

# # squaredList = []
# # for item in myList:
# #     squaredList.append(item*item)

# squaredList = [i*i for i in myList]

# print(squaredList)





def myFunc():
    print("Hello world!")



if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)