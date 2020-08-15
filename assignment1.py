""" 1. Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line. """

number = [num for num in range(2000,3201) if num % 7 == 0 and num % 5 != 0]
print(number)


""" 2. Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.  """
def rev_name():
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    return (f'{first_name[::-1]} {last_name[::-1]}')
print(f'Reversed Name: {rev_name()}')


"""3. Write a Python program to find the volume of a sphere with diameter 12 cm. 
Formula: V=4/3 * π * r ^ 3"""
from math import pi
def vol():
    diameter = 12
    volume = (4/3) * pi * (diameter/2)**3
    return volume
print(f'Volume of Sphere: {vol()}')