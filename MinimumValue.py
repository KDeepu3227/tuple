'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
def get_min_from_user():
    n = int(input("Enter the number of elements: "))
    values = ()
    for _ in range(n):
        value = int(input("Enter a value: "))
        values += (value,) 
    print("The minimum value is:", min(values))
get_min_from_user()
'''
Enter the number of elements: 3
Enter a value: 20
Enter a value: 10
Enter a value: 30
The minimum value is: 10
