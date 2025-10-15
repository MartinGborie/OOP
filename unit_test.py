import library

def run_tests():
    # Test 1: Add a book
    library.books.clear()
    library.members.clear()
    library.add_book("123", "Python Basics", "escanor", "Non-Fiction", 5)
    assert "123" in library.books, "Test 1 Failed: Book not added"
    print("Test 1 Passed: Book added successfully")

    # Test 2: Add duplicate ISBN
    library.add_book("123", "Duplicate Book", "senku", "Fiction", 3)
    assert len(library.books) == 1, "Test 2 Failed: Duplicate ISBN not handled"
    print("Test 2 Passed: Duplicate ISBN handled")

    # Test 3: Borrow a book
    library.add_member("M001", "jin sakai", "sakaijin@email.com")
    library.borrow_book("M001", "123")
    title, author, genre, copies = library.books["123"]
    assert copies == 4, "Test 3 Failed: Borrowing not reducing copies"
    print("Test 3 Passed: Book borrowed successfully")

    # Test 4: Borrow when no copies left
    for _ in range(4):
        library.borrow_book("M001", "123")
    library.borrow_book("M001", "123")
    assert library.books["123"][3] == 0, "Test 4 Failed: Borrowing with no copies"
    print("Test 4 Passed: Borrowing with no copies handled")

    # Test 5: Return a book
    library.return_book("M001", "123")
    title, author, genre, copies = library.books["123"]
    assert copies == 1, "Test 5 Failed: Return not increasing copies"
    print("Test 5 Passed: Book returned successfully")

if __name__ == "__main__":
    run_tests()