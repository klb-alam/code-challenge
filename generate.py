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


def generate_random_alphanumeric():
  letters = string.ascii_letters
  digits = string.digits
  length = random.randint(5, 15)
  before_spaces = random.randint(0, 10)
  after_spaces = random.randint(0, 10)

  # Ensure at least one letter and one digit
  chars = [random.choice(letters), random.choice(digits)]
  chars.extend(random.choice(letters + digits) for i in range(length - 2))
  random.shuffle(chars)

  return " " * before_spaces + ''.join(chars) + " " * after_spaces

def main(filename):
  max_size = 1024 * 1024 * 10
  with open(filename, 'w') as f:
    while os.path.getsize(filename) < max_size:
      f.write(generate_random_string(10) + ",")


if __name__ == "__main__":
  main("random.txt")
  print("File generated successfully!")