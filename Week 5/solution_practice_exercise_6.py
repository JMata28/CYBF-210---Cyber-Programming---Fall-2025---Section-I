# Today’s problem is calculating the Fibonacci series using recursion. 
# The problem is described here: https://leetcode.com/problems/fibonacci-number/description/ 
# The solution we will go over is an adaptation of LeetCode user Vaishnav’s solution found here: https://leetcode.com/problems/fibonacci-number/solutions/7205782/with-recursion-python-3 

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(4))