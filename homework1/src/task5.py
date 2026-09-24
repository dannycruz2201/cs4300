# Task 5: Data Structures - Book List and Student Database

# =============================================================================
# DATA STRUCTURE 1: List of Favorite AI Books
# =============================================================================

# List of 10 AI books with "title" and "author" keys
ai_books = [
    {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell and Peter Norvig"},
    {"title": "Life 3.0: Being Human in the Age of Artificial Intelligence", "author": "Max Tegmark"},
    {"title": "Superintelligence: Paths, Dangers, Strategies", "author": "Nick Bostrom"},
    {"title": "Artificial Intelligence: A Guide for Thinking Humans", "author": "Melanie Mitchell"},
    {"title": "AI Superpowers: China, Silicon Valley, and the New World Order", "author": "Kai-Fu Lee"},
    {"title": "The Alignment Problem: Machine Learning and Human Values", "author": "Brian Christian"},
    {"title": "Co-Intelligence: Living and Working with AI", "author": "Ethan Mollick"},
    {"title": "The Master Algorithm", "author": "Pedro Domingos"},
    {"title": "The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI", "author": "Fei-Fei Li"},
    {"title": "Human Compatible: AI and the Problem of Control", "author": "Stuart Russell"}
]

def get_first_three_books():
    return ai_books[:3]

def get_all_books():
    return ai_books

def get_book_count():
    return len(ai_books)

def get_book_by_index(index):
    if 0 <= index < len(ai_books):
        return ai_books[index]
    return None

def get_books_by_author(author_name):
    matching_books = []
    for book in ai_books:
        if author_name.lower() in book["author"].lower():
            matching_books.append(book)
    return matching_books

# =============================================================================
# DATA STRUCTURE 2: Student Database
# =============================================================================

student_database = {
    "Alice Smith": 1001,
    "Bob Jones": 1002,
    "Charlie Brown": 1003,
    "Diana Prince": 1004,
    "Eve Davis": 1005
}

def get_student_id(name):
    return student_database.get(name)

def add_student(name, student_id):
    student_database[name] = student_id
    return student_database

def get_all_students():
    return student_database

def remove_student(name):
    if name in student_database:
        del student_database[name]
        return True
    return False

def main():
    """Main function demonstrating both data structures."""
    print("=== First Three AI Books ===")
    first_three = get_first_three_books()
    for i, book in enumerate(first_three, 1):
        print(f"{i}. \"{book['title']}\" by {book['author']}")
    
    print(f"\nTotal books in collection: {get_book_count()}")
    
    print("\n=== Student Database ===")
    for name, student_id in get_all_students().items():
        print(f"{name}: {student_id}")

if __name__ == "__main__":
    main()