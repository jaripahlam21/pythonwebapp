# word_count.py
import sys

def count_words(filepath):
    """Counts the number of words in a given file."""
    with open(filepath, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

if __name__ == "__main__":
    # Check if a file path was provided as a command line argument
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            print("Word count:", count_words(path))
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
    else:
        print("Please provide a file path as a command line argument.")

