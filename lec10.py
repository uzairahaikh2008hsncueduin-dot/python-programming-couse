# class Employee: 
#     language = "Py" # This is a class attribute
#     salary = 1200000


# harry = Employee()
# harry.name = "Harry" # This is an instance attribute
# print(harry.name, harry.language, harry.salary)

# rohan = Employee()
# rohan.name = "Rohan Roro Robinson"
# print(rohan.name, rohan.salary, rohan.language)

# # Here name is instance attribute and salary and language are class attributes as they directly belong to the class




# class Employee: 
#     language = "Python" # This is a class attribute
#     salary = 1200000


# harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
# print(harry.language, harry.salary)
 



# class Employee: 
#     language = "Python" # This is a class attribute
#     salary = 1200000

#     def getInfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")

#     @staticmethod
#     def greet():
#         print("Good morning")


# harry = Employee()
# # harry.language = "JavaScript" # This is an instance attribute
# harry.greet()
# harry.getInfo() 
# # Employee.getInfo(harry)
 




class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

rohan = Employee()