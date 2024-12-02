import random
import string
import os


'''
Challenge A
Write a program that will generate four (4) types of printable random objects and store them in a single file, 
each object will be separated by a ",". These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics. 

The alphanumerics should contain a random number of spaces before and after it (not exceeding 10 spaces). The output should be 10MB in size.
'''

generate_random_string = lambda length: ''.join(random.choice(string.ascii_letters) for _ in range(length))
generate_random_real = lambda: random.uniform(-10, 10)
generate_random_integer = lambda: random.randint(-100, 100)


