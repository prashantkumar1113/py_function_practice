# Write a Python function called max_num()to find the maximum of three numbers.
import math


def max_num(a, b, c):
    max = a
    num_list = [a, b, c]
    for x in num_list:
        if x > max:
            max = x
    return max
print(max_num(7, 3, 1))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
    result = 1
    for num in list:
        result *= num
    return result
print(mult_list([2,4,6]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]
print(rev_string("Prashant"))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, beginning, end):
    return num >= beginning and num <= end 

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together.
# n!/k!(n−k)!

def pascal(num_of_rows):
    print_str = ""
    for n in range(0, num_of_rows):
        for k in range(0,n+1):
            # print(f"i:{i}, j:{j}")
            print(f"{math.comb(n,k)} ", end="")
        print("")
pascal(5)