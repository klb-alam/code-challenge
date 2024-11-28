import random
import string
import os
import argparse
from typing import Callable
from datetime import datetime


RandomGenerator = Callable[[], str]


generate_random_string: Callable[[int], str] = lambda length: "".join(
    random.choice(string.ascii_letters) for _ in range(length)
)
generate_random_real: Callable[[], float] = lambda: random.uniform(-10, 10)
generate_random_integer: Callable[[], int] = lambda: random.randint(-100, 100)


def generate_random_alphanumeric() -> str:
    letters: str = string.ascii_letters
    digits: str = string.digits
    length: int = random.randint(5, 15)
    before_spaces: int = random.randint(0, 10)
    after_spaces: int = random.randint(0, 10)

    chars: list[str] = [random.choice(letters), random.choice(digits)]
    chars.extend(random.choice(letters + digits) for _ in range(length - 2))
    random.shuffle(chars)

    return " " * before_spaces + "".join(chars) + " " * after_spaces


def log_message(message: str) -> None:
    """Logs a message with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def main(filename: str, max_size: int, max_lines: int = None) -> None:
    log_message("File generation started.")
    with open(filename, "w") as f:
        current_size = 0
        line_count = 0

        while current_size < max_size and (max_lines is None or line_count < max_lines):
            random_string = generate_random_alphanumeric() + ","
            f.write(random_string)
            current_size = os.path.getsize(filename)
            line_count += 1

            # Display progress every 10%
            if max_size > 0 and (current_size / max_size * 100) % 10 < 1:
                print(f"Progress: {current_size / max_size * 100:.2f}%")

    log_message("File generation completed successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a random text file with alphanumeric strings."
    )
    parser.add_argument("filename", type=str, help="Name of the output file.")
    parser.add_argument(
        "--max_size",
        type=int,
        default=10 * 1024 * 1024,
        help="Maximum size of the file in bytes (default: 10MB).",
    )
    parser.add_argument(
        "--max_lines",
        type=int,
        help="Maximum number of lines to write (default: unlimited).",
    )

    args = parser.parse_args()
    main(args.filename, args.max_size, args.max_lines)
