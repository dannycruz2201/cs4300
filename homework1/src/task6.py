import os

def count_words():
    """
    Reads the file 'src/task6_read_me.txt' and returns the total word count.

    Returns:
        int: The number of words in the file
    """
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Build the full path to the file
    file_path = os.path.join(script_dir, 'task6_read_me.txt')
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        content = file.read()
    
    # Split the content into words and count them
    words = content.split()
    word_count = len(words)
    
    # Return the word count
    return word_count

# Run file directly to test
if __name__ == "__main__":
    # This block runs when you execute: python src/task6.py
    # It's useful for quick testing before running the full test
    
    result = count_words()
    print(f"Total word count: {result}")