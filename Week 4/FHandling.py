try:
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: make all text uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("modified_" + filename, "w") as file:
        file.write(modified_content)

    print("File has been read and modified successfully!")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: The file cannot be read (permission denied).")
