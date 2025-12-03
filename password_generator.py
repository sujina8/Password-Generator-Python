import random
import string

###Function used to generate password
def generate_password(length, use_digits=True, use_symbols=True):
    ###Characters set
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    ### Start the password with letters only
    characters = letters
    ### Add digits if user wants
    if use_digits:
        characters += digits
    ### Add symbols if users wants
    if use_symbols:
        characters += symbols

    ### Checking minimum length of password
    if length < 6:
        print("Password length should be at least 6.")
        return None
    ### Generate password by randomly picking characters
    password = ''.join(random.choice(characters) for_in range(length))

    return password

###Main program function
def main():
    print("---Password Generator---")
    
    ### Ask user for length of password
    try:
        length = int(input("Enter the password length: "))
    except ValueError:
        print("Invalid number. Please enter a valid integer.")
        return

    ###Ask user whether to include digits and symbols
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    ###Generate the password
    password = generate_password(length, include_digits, include_symbols)

    ###Displaying generated password
    if password:
        print("\nGenerated Password:")
        print(password)
main()
