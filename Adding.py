'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
input_tuple = tuple(map(int, input().split()))
total = 0
for number in input_tuple:
    total += number
print(total)
'''
30 40 20
90
