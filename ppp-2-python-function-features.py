# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for i in args:
        print(i)
arb_args("Hello", "world", "!")

# inner_func - Takes in two integers. Two nested functions should perform separate, 
# distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed.
def inner_func(num1, num2):
    def add_numbs(x, y):
        return x+y
    def sub_numbs(a, b):
        return a-b
    result_1 = add_numbs(num1,num2)
    result_2 = sub_numbs(num1, num2)
    print (f"num1 = {num1}   num2 = {num2}")
    print(f"adding = {result_1}, subtracting = {result_2}")
    print(f"Total is: {result_1+result_2}")

inner_func(3,4)

# lunch_lady - Takes in two strings: a student's name and their lunch preference. 
# The function should print both strings. 
# If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, lunch_pref = "Mystery Meat"):
    print(f"Student Name: {name} and lunch preferance is: {lunch_pref}")

lunch_lady("Prashant", "pizza")
lunch_lady("Chris")

# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(x ,y):
    return x+y, x*y
sum, multiply = sum_n_product(10,5)
print(f"Sum = {sum}     multiply = {multiply}")

# alias_arb_args - Should be arb_args but assigned an alias. 
# Remember, variables can hold functions in Python just like they can in JS. 
# Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args
alias_arb_args("prashant", "kumar")

# arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*nums):
    sum = 0
    for i in nums:
        sum+=i
    return sum/len(nums)

print(arb_mean(6,4,2,18))

# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*str):
    longest_str = str[0]
    for i in str:
        if len(i) > len(longest_str):
            longest_str = i

    return longest_str

print(arb_longest_string("kumar", "prashant", "hello!", "wisconsin"))