'''
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
def count_value_in_tuple():
    values_input = input("Enter tuple values separated by space: ")
    values = tuple(map(int, values_input.split()))  
    x = int(input("Enter the value to count: "))
    count = values.count(x)
    print(count)
count_value_in_tuple()
'''
Enter tuple values separated by space: 1 2 3 1 2 3 4 1 2 1
Enter the value to count: 2
3
