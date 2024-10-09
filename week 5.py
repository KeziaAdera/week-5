# file_handling_assignment.py

def create_file():
    try:
        # Step 1: Create a new text file and write to it
        with open('my_file.txt', 'w') as file:
            file.write("Today is rainy.\n")
            file.write("Book your bus tickets at section: 42.\n")
            file.write("Lastly, be early.\n")
        print("File created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error creating file: {e}")
    finally:
        print("Create file operation completed.")

def read_file():
    try:
        # Step 2: Read and display the contents of the file
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("Read file operation completed.")

def append_to_file():
    try:
        # Step 3: Append additional lines to the file
        with open('my_file.txt', 'a') as file:
            file.write("Here is to great times.\n")
            file.write("Seasons of merry: 100.\n")
            file.write("Finally, have a nice day.\n")
        print("Additional content appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Append file operation completed.")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Display the updated contents after appending

if __name__ == "__main__":
    main()

