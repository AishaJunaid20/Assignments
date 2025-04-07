# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello! This is a file handling example.\n")
    file.write("Python is fun!")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
