'''
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
input_data = input("Enter numbers separated by spaces: ")
numbers_tuple = tuple(map(int, input_data.split()))
print(len(numbers_tuple))
'''
Enter numbers separated by spaces: 10 20 30
3
