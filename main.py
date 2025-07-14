# Import both functions from stats.py
from stats import get_word_count, get_char_counts


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # Add this line to call the function and create the variable
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")

      # Get and print character counts
    char_counts = get_char_counts(text)
    print(char_counts)

main()