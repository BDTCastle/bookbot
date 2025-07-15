# Import functions from stats.py
# main.py
import sys
from stats import get_word_count, get_char_counts, get_sorted_char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
        # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with an error code

    # Use the argument as the book path
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_counts = get_char_counts(text)
    sorted_chars = get_sorted_char_list(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()