'''
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''
n = int(input("Enter the number of elements: ")
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
numbers_tuple = tuple(elements)
total_sum = sum(numbers_tuple)
print(total_sum)
'''
Enter the number of elements: 3
10
20
30
60
