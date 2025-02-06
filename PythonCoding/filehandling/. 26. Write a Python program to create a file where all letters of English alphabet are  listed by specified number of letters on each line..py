import string  # Import string module to get the alphabet


# Function to create file with alphabet letters
def create_alphabet_file(filename, letters_per_line):
    alphabet = string.ascii_uppercase  # This is a string containing 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open(filename, "w") as file:  # Open a file in write mode
        for i in range(0, len(alphabet), letters_per_line):  # Loop through the alphabet
            line = alphabet[i:i + letters_per_line]  # Get a slice of letters
            file.write(line + "\n")  # Write the letters and move to the next line


# Example usage of the function
create_alphabet_file("alphabet.txt", 5)  # Create the file with 5 letters per line

print("File created successfully!")
