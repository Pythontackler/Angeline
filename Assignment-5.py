
def create_file():
    try:
        # Creating a new text file in write mode
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is  the second line with a number: 123\n")
            file.write("The third line is right here!\n")
        print("File created and initial lines written.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        # Reading the contents of the file and displaying them
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file():
    try:
        # Opening the file in append mode and adding more lines
        with open("my_file.txt", "a") as file:
            file.write("Appending line 4.\n")
            file.write("Appending line 5 with another number: 456\n")
            file.write("Appending line 6!\n")
        print("Additional lines appended.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    try:
        create_file()
        read_file()
        append_to_file()
        read_file()
    finally:
        print("Script execution completed.")

if __name__ == "__main__":
    main()
