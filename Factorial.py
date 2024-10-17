'''
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
def main():
    input_tuple = (1, 2, 3, 4, 1, 5, 1) 
    x = 1
    count = input_tuple.count(x)
    factorial_value = calculate_factorial(count)
    print(f"Count of {x}: {count}")
    print(f"Factorial of {count}: {factorial_value}")
if __name__ == "__main__":
    main()
'''
Count of 1: 3
Factorial of 3: 6
