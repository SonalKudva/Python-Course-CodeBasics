'''
Other than math module, there are many other modules that come with the
Python installation.There is another category of modules called external modules.

Thus, the two types of modules are:
1. Built-in modules
2. External modules
'''

# 1.
import math
print("List of functions which are available in math module")
print(dir(math))
print()

import calendar
print("List of functions which are available in calendar module")
print(dir(calendar))
print()

august = calendar.month(2024, 8)
print(august)

# to find out if a year is leap or not
print("Is 2024 a leap year? ", calendar.isleap(2024))
print()

# 2. External modules

# Python PyPI - contains all the different libraries/modules which are available.
# To install a module, we used the 'pip' utility. Whenever we install Python, pip will
# come built in with it.

# 3. User-defined modules - you have some requirement and you want to create your own Python functions
# then we can create a user defined module.

def find_cylinder_volume(radius, height=7):
    print("radius:", radius)
    print("height", height)
    volume = 3.14 * (radius**2) * height
    print(volume)
    return volume

r = 10

v = find_cylinder_volume(radius=r, height=67)
print(v)

'''
Takeaways:
1. Modules in Python allow you to organize and reuse code across multiple programs
2. You can import built-in modules like math and external modules which are available on https://pypi.org/
3. Use import module_name to bring a module into your current script.
4. The pip tool is used to install and manage external Python packages.
5. Use pip install package_name to add new packages to your Python environment.
'''
