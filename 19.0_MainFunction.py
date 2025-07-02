'''
Let's look at the main function in Python which is called an entry point.
In other programming languages, we have a main function act as an entry point. The execution starts from this
function. We can have other functions written, but main acts like an entry point.

In Python, we have a way to provide that entry point.
'''
def calculate_triangle_area(base, height):
    print("value of __name__ :", __name__)
    return (base*height)/2

# The above approach works, but the way to write a proper entry point is by:
if __name__ == "__main__":
    print("Area of triangle: ", calculate_triangle_area(10, 5))

# __name__ is a spatial parameter or variable in Python and by default it is set to __main__

'''
Takeaways:
1. 'if __name__ == "__main__" is a way to define entry point in Python code (similar to main function in C++ or Java)
2. When you import any module (eg. import numpy as np), the module._name_ is set to the name of that module
(eg. np._name_ is set as 'Numpy')
'''