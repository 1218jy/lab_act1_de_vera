#Write a Python function named print_diamond that takes an odd integer 
# n as an argument and prints a diamond shape with a width of n using the * character.
# Note: If an even number is passed, the function should return "Please provide an odd integer."

n = int(input('Enter an odd integer:'))

def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."

    middle = n // 2
   
    for i in range(middle + 1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (middle - i)
        print(spaces + stars)

    for i in range(middle - 1, -1, -1):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (middle - i)
        print(spaces + stars)

print_diamond(n)