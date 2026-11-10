# '''
# a = "a very long string with emails"

# emails = []
# 3 seconds
# '''

# f = open("file.txt", "r")
# data = f.read()
# print(data)
# f.close()



# st = "Hey Harry you are amazing"

# f = open("myfile.txt", "w")

# f.write(st)

# f.close()



f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()



# st = "Hey Harry you are amazing"

# f = open("myfile.txt", "a")

# f.write(st)

# f.close()



# f = open("file.txt")
# print(f.read())
# f.close()

# # The same can be written using with statement like this:
# with open("file.txt") as f:
#     print(f.read())

# You dont have to explicitly close the file



# Harry is a good boy
# I am a second line
# This is amazing
# Twinkle Twinkle little star



# Hey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazingHey Harry you are amazing