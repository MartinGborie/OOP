import library

def run_demo():
    print("--- Demo: Mini Library Management System ---")
    
    # Add books
    library.add_book("123", "Python Basics", "escanor", "Non-Fiction", 5)
    library.add_book("124", "Sci-Fi Adventures", "nico robin", "Sci-Fi", 3)
    
    # Add members
    library.add_member("M001", "jin sakai", "sakaijin@email.com")
    library.add_member("M002", "itachi uchiha", "itachi@email.com")
    
    # Search for a book
    print("\nSearching for 'Python'...")
    library.search_book("Python")
    
    # Borrow a book
    print("\nBorrowing book 123 by M001...")
    library.borrow_book("M001", "123")
    
    # Return a book
    print("\nReturning book 123 by M001...")
    library.return_book("M001", "123")
    
    # Delete a book
    print("\nDeleting book 124...")
    library.delete_book("124")
    
    # Update a book
    print("\nUpdating book 123...")
    library.update_book("123", "Advanced Python", "escanor", "Non-Fiction", 4)

if __name__ == "__main__":
    run_demo()