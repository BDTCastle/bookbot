def get_word_count(text):
    words = text.split()
    return len(words)
# New function for counting characters
def get_char_counts(text):
    # Convert the text to lowercase
    lowered_text = text.lower()
    
    # Create the empty dictionary
    char_counts = {}
    
    # Loop through each character
    for char in lowered_text:
        if char in char_counts:
            # If character exists, increment its count
            char_counts[char] += 1
        else:
            # If character is new, add it with a count of 1
            char_counts[char] = 1
            
    return char_counts
# New helper function for sorting
def sort_on(d):
    return d["num"]

# New function to convert dict to sorted list
def get_sorted_char_list(char_counts_dict):
    char_list = []
    # Convert the dictionary to a list of dictionaries
    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list in descending order using the helper function
    char_list.sort(reverse=True, key=sort_on)
    return char_list