try:
    # open and read the file
    with open("myfile.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    # handle the FileNotFoundError exception
    print("The file could not be found.")
# No need for a finally block with 'with' statement
