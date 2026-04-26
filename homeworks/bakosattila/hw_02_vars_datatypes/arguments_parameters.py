
def show_book_details(title, author="Test Writer", year=2026):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

show_book_details("The Great Gatsby")
show_book_details("Test Book", "XY")
show_book_details("Another Book", year=2020)
