import os
from pathlib import Path
print(os.getcwd())

file_path = Path("lessons") / "lesson_08"/ "sample.txt" #relative path
# without context managers
file = open(file_path, "w")
try:
    file.write("This is a sample text!")
finally:
    file.close()

#with context managers
with open(file_path, "w") as file:
    file.write("This is a sample text from the context manager\n")

#with context managers
with open(file_path, "a") as file:
    file.write("This is a sample text from the context manager\n")


#file handle handling: reading

with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())

# generator function to read a file:
def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line
print("---------------------")
#gen = read_file_line_by_line(file_path=file_path)
#print(next(gen))
#print(next(gen))

for line in read_file_line_by_line(file_path):
    print(type(line))
    print(line)