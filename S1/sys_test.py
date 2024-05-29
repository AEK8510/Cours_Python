import sys

def addition(x, y):
    return x + y

my_choice = int(sys.argv[1])
lines_count = 0

if my_choice == 1:
    a = sys.argv[2]
    b = sys.argv[3]
    c = addition(a, b)
    print(c)

if my_choice == 2:
    file_name = sys.argv[2]
    with open(file_name, "r") as file:
        Lines = file.readlines()
        lines_count = len(Lines)
    print("file_name contains:", lines_count)