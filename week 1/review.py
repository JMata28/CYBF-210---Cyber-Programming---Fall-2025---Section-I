# Printing statements
print("Hello World!")
print("Welcome to CYBF 210 - Cyber Programming!")

# Basic variables
students_present = 12
average_grade = 99.99
# Remember Python is case sensitive!! False and True must have their first letter capitalized
daytime_class = True
class_code = "CYBF 210"  # notice snake case, which is typical for Python code

# Common string functions
# To get the length of a string
len(class_code)  # What value will show in our terminal if we run the program? If any?
# To access specific characters in a string using indexing (Python is zero-indexed)
# What will the following lines print?
class_code[0]
class_code[5]
class_code[-1]
class_code[:3]
class_code[1:2]
# Escape character in strings
# \", \\, \n
print("The title of the Book is \"The Great Gatsby\"")

# Formatted strings
formatted_string = f"This class is {class_code}"
print(formatted_string)

# Common string methods
my_sentence = "Pizza is my favorite food."
# Method does not change the original value of string
print(my_sentence.upper())
print(my_sentence.lower())
print(my_sentence.title())
print(my_sentence.strip())
print(my_sentence.lstrip())
print(my_sentence.rstrip())
print(my_sentence.find("zza"))
#More methods and Python documentation on built-in types here: https://docs.python.org/3/library/stdtypes.html#string-methods
print(my_sentence.replace("i", "j"))
print("Pizzas" in my_sentence)

# user input
fav_food = input("Enter your favorite food: ")
print(fav_food)

