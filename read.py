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

        for obj in objects:
            try:
                value = int(obj)
                print(f"Object: {value}, Type: Integer")
            except ValueError:
                try:
                    value = float(obj)
                    print(f"Object: {value}, Type: Real Number")
                except ValueError:
                    if obj.isalnum():
                        print(f"Object: {obj}, Type: Alphanumeric")
                    else:
                        stripped_obj = obj.strip()
                        if stripped_obj.isalnum():
                            print(f"Object: {stripped_obj}, Type: Alphanumeric")
                        else:
                            print(f"Object: {obj}, Type: Alphabetical String")

if __name__ == "__main__":
    filename = "random.txt"
    if os.path.exists(filename):
        process_file(filename)
    else:
        print(f"Error: File '{filename}' not found.")