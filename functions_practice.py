# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.
# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.
def say_hello():
    print("Hello")
say_hello()
# 2. a 'sum' function that accepts two integers and returns the sum.
def sum(a, b):
    return a+b
print("sum: ", sum(5,4))
# 3. an 'average' function that accepts two numbers and returns the average.
def average(a,b):
    return (a+b)/2

print("average: ", average(5,4))

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).
def fullname(first_name, last_name):
    return f"{last_name}, {first_name}"

print("fullname: ", fullname("Prashant", "Kumar"))

# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def student(first_name, last_name, graduation_year, student_number):
    return [first_name, last_name, graduation_year, student_number]
print(student("Prashant", "Kumar", 2022, 123456))
# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def is_adult(age):
    if age > 18: return True
    else: return False

print(is_adult(25))
#7. A function that accepts a string and prints the string in reverse (no return value).
def string_reverse(str):
    new_str = str[::-1]
    return new_str
print(string_reverse("Hello, World! backwards"))


def hello():
    print("Hello World! How are you?")

hello()

def pack(one, two, three):
    return [one, two, three]

packed_items = pack("backpack", "hat", "sunscreen")
print(packed_items)