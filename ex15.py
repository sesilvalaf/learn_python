# use argv to get a filename
from sys import argv

script, filename = argv
# open the file
txt = open(filename)
# read the file and print
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())

