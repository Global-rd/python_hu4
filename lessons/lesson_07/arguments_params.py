#default argument
def greet(name="User"):
    print(f"Hello {name}")

greet()


#combining default and positional arguments
print("-------------------")

def show_book_details(title, author="Test Writer", year=2026):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

show_book_details("Test Book")
show_book_details("Test Book", "XY")
show_book_details("Test Book", "XY", 2021)

show_book_details("XY book", author="XY writer", year=2025)


#mutable objects as default arguments
#bad example

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))

#good example

def append_to_list(value, my_list=None):

    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))