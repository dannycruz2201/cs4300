import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from task5 import (
    get_first_three_books,
    get_all_books,
    ai_books,
    get_book_count,
    get_book_by_index,
    get_books_by_author,
    get_student_id,
    add_student,
    get_all_students,
    remove_student,
    student_database
)


# =============================================================================
# TESTS FOR LIST DATA STRUCTURE (ai_books)
# =============================================================================

class TestAIBooksList:
    """Test cases for the AI books list data structure."""
    
    def test_ai_books_has_ten_books(self):
        """Test that ai_books list contains exactly 10 books."""
        assert len(ai_books) == 10
    
    def test_each_book_has_title_and_author(self):
        """Test that each book dictionary has 'title' and 'author' keys."""
        for book in ai_books:
            assert "title" in book
            assert "author" in book
    
    def test_get_first_three_books_returns_three_books(self):
        """Test that get_first_three_books returns exactly 3 books."""
        result = get_first_three_books()
        assert len(result) == 3
    
    def test_get_first_three_books_returns_correct_books(self):
        """Test that get_first_three_books returns the first 3 books from the list."""
        result = get_first_three_books()
        expected = ai_books[:3]
        assert result == expected
    
    def test_get_first_three_books_uses_list_slicing(self):
        """Test that the first three books match expected content."""
        result = get_first_three_books()
        assert result[0]["title"] == "Artificial Intelligence: A Modern Approach"
        assert result[1]["title"] == "Life 3.0: Being Human in the Age of Artificial Intelligence"
        assert result[2]["title"] == "Superintelligence: Paths, Dangers, Strategies"
    
    def test_get_all_books_returns_complete_list(self):
        """Test that get_all_books returns all 10 books."""
        result = get_all_books()
        assert len(result) == 10
        assert result == ai_books
    
    def test_get_book_count_returns_ten(self):
        """Test that get_book_count returns 10."""
        assert get_book_count() == 10
    
    def test_get_book_by_index_valid(self):
        """Test get_book_by_index with valid indices."""
        first_book = get_book_by_index(0)
        assert first_book["title"] == "Artificial Intelligence: A Modern Approach"
        
        last_book = get_book_by_index(9)
        assert last_book["title"] == "Human Compatible: AI and the Problem of Control"
    
    def test_get_book_by_index_invalid(self):
        """Test get_book_by_index with invalid index returns None."""
        assert get_book_by_index(-1) is None
        assert get_book_by_index(10) is None
        assert get_book_by_index(100) is None
    
    def test_get_books_by_author_partial_match(self):
        """Test finding books by partial author name."""
        stuart_books = get_books_by_author("Stuart")
        assert len(stuart_books) == 2  # Stuart Russell has 2 books
    
    def test_get_books_by_author_specific(self):
        """Test finding books by specific author name."""
        tegmark_books = get_books_by_author("Max Tegmark")
        assert len(tegmark_books) == 1
        assert tegmark_books[0]["title"] == "Life 3.0: Being Human in the Age of Artificial Intelligence"


# =============================================================================
# TESTS FOR DICTIONARY DATA STRUCTURE (student_database)
# =============================================================================

class TestStudentDatabase:
    """Test cases for the student database dictionary."""
    
    def test_student_database_is_dictionary(self):
        """Test that student_database is a dictionary."""
        assert isinstance(student_database, dict)
    
    def test_student_database_has_at_least_five_students(self):
        """Test that the database contains at least 5 students."""
        assert len(student_database) >= 5
    
    def test_get_student_id_returns_correct_id(self):
        """Test that get_student_id returns the correct ID for a known student."""
        assert get_student_id("Alice Smith") == 1001
        assert get_student_id("Bob Jones") == 1002
    
    def test_get_student_id_returns_none_for_unknown_student(self):
        """Test that get_student_id returns None for a student not in database."""
        assert get_student_id("Unknown Student") is None
    
    def test_add_student_adds_new_entry(self):
        """Test that add_student correctly adds a new student."""
        original_count = len(student_database)
        add_student("Test Student", 9999)
        assert len(student_database) == original_count + 1
        assert student_database["Test Student"] == 9999
        # Clean up
        del student_database["Test Student"]
    
    def test_get_all_students_returns_dictionary(self):
        """Test that get_all_students returns the student database."""
        result = get_all_students()
        assert result == student_database
        assert isinstance(result, dict)
    
    def test_remove_student_deletes_existing_student(self):
        """Test that remove_student removes an existing student."""
        # Add a temporary student
        student_database["Temp Student"] = 8888
        assert "Temp Student" in student_database
        
        result = remove_student("Temp Student")
        assert result is True
        assert "Temp Student" not in student_database
    
    def test_remove_student_returns_false_for_nonexistent(self):
        """Test that remove_student returns False when student doesn't exist."""
        result = remove_student("Nonexistent Student")
        assert result is False
    
    def test_remove_student_returns_true_for_existing(self):
        """Test that remove_student returns True when student exists."""
        # Add a temporary student
        student_database["Another Temp"] = 7777
        result = remove_student("Another Temp")
        assert result is True


# =============================================================================
# EDGE CASE TESTS
# =============================================================================

class TestEdgeCases:
    """Edge case tests for both data structures."""
    
    def test_ai_books_title_is_string(self):
        """Test that all book titles are strings."""
        for book in ai_books:
            assert isinstance(book["title"], str)
    
    def test_ai_books_author_is_string(self):
        """Test that all book authors are strings."""
        for book in ai_books:
            assert isinstance(book["author"], str)
    
    def test_student_id_is_int_or_string(self):
        """Test that all student IDs are either int or str."""
        for student_id in student_database.values():
            assert isinstance(student_id, (int, str))