from typing import Callable
import random
import string
import os

# Type aliases
RandomGenerator = Callable[[], str]

# Type-annotated lambda functions
generate_random_string: Callable[[int], str] = lambda length: ''.join(random.choice(string.ascii_letters) for _ in range(length))
generate_random_real: Callable[[], float] = lambda: random.uniform(-10, 10)
generate_random_integer: Callable[[], int] = lambda: random.randint(-100, 100)

def generate_random_alphanumeric() -> str:
    letters: str = string.ascii_letters
    digits: str = string.digits
    length: int = random.randint(5, 15)
    before_spaces: int = random.randint(0, 10)
    after_spaces: int = random.randint(0, 10)

    # Ensure at least one letter and one digit
    chars: list[str] = [random.choice(letters), random.choice(digits)]
    chars.extend(random.choice(letters + digits) for i in range(length - 2))
    random.shuffle(chars)

    return " " * before_spaces + ''.join(chars) + " " * after_spaces

def main(filename: str) -> None:
    max_size: int = 1024 * 1024 * 10  # 10MB in bytes
    with open(filename, 'w') as f:
        while os.path.getsize(filename) < max_size:
            f.write(generate_random_alphanumeric() + ",")

if __name__ == "__main__":
    main("random.txt")
    print("File generated successfully!")