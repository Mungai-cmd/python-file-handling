# file_handling_assignment.py

def create_and_write_file():
    """Creates a file and writes initial content to it."""
    try:
        # Create and open the file in write mode
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 123\n")
            file.write("Finally, the third line is here.\n")
        print("File created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")
    finally:
        print("Finished writing to the file.")

def read_file():
    """Reads and displays the content of the file."""
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("Content of the file:")
        print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    finally:
        print("Finished reading the file.")

def append_to_file():
    """Appends additional content to the file."""
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending a new line of text.\n")
            file.write("Another line added to the file.\n")
            file.write("And a third additional line.\n")
        print("Content appended successfully.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to append to the file.")
    finally:
        print("Finished appending to the file.")

if __name__ == "__main__":
    create_and_write_file()  # Create the file and write initial content
    read_file()              # Read and display the file content
    append_to_file()         # Append more content to the file
    read_file()              # Read and display the updated file content
