import os

'''
Challenge B

Create a program that will read the generated file above and print to the console the object and its type. 
Spaces before and after the alphanumeric object must be stripped.

'''
def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        objects = content.strip(',').split(',')  
        print(objects)

if __name__ == "__main__":
    filename = "random.txt"
    if os.path.exists(filename):
        process_file(filename)
    else:
        print(f"Error: File '{filename}' not found.")