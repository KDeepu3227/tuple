'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
def get_max_from_user():
    n = int(input("Enter the number of elements: "))
    values = ()
    for _ in range(n):
        value = int(input("Enter a value: "))
        values += (value,)  # Add value to the tuple
    print("The maximum value is:", max(values))
get_max_from_user()
'''
Enter the number of elements: 3
Enter a value: 10
Enter a value: 30
Enter a value: 20
The maximum value is: 30

​
