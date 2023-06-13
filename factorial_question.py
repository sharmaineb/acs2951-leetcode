"""
restate the question:
the question asks for a function that returns the factorial of any positive input number.

pseudocode:
- define a function called factorial that takes a positive num as input.
- check if num is negative. If it is, raise a ValueError since factorial is undefined for negative numbers.
- check if num is 0 or 1. If it is, return 1 since the factorial of 0 and 1 is defined as 1.
- for any other positive input, calculate the factorial recursively.
   * call the function recursively with num - 1.
   * multiply the result by num.
   * return the result.
"""

# define a function called factorial that takes an input parameter n
def factorial(num):

# check if the input num is less than 0. 
# if it is, raise a ValueError stating that the input has to be a non-negative number
    if num < 0:
        raise ValueError("sorry, input should be a non-negative number.")

# check if the input num is equal to 0 or 1
# if it is, return 1
    elif num == 0 or num == 1:
        return 1
    
# if the input num is not 0 or 1
# take the number and multiply it by the factorial of the number that is one less
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result


print(factorial(4))  

