import random
import string
import sys  # for cleaner exit on error

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    """
    Generates a random password of the specified length with the given character types.

    Args:
        length (int): The desired length of the password.
        include_lowercase (bool): Whether to include lowercase letters (a-z).
        include_uppercase (bool): Whether to include uppercase letters (A-Z).
        include_digits (bool): Whether to include digits (0-9).
        include_symbols (bool): Whether to include special symbols (e.g., !@#$%^&*()).

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the password length is non-positive or no character type is selected.
    """
    # Check for valid length
    if length <= 0:
        raise ValueError("Password length must be a positive number.")

    # Collect all available characters based on selected options
    all_characters = ""
    if include_lowercase:
        all_characters += string.ascii_lowercase
    if include_uppercase:
        all_characters += string.ascii_uppercase
    if include_digits:
        all_characters += string.digits
    if include_symbols:
        all_characters += string.punctuation

    # Check that at least one character type is selected
    if not all_characters:
        raise ValueError("No character type selected for password generation.")

    # Generate the password by randomly choosing characters from the available set
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password


# --- main part of the program for user interaction ---

if __name__ == "__main__":
    print("--- Secure Password Generator ---")

    # Get password length from the user
    while True:
        try:
            password_length_str = input("Enter the desired password length (e.g., 12): ")
            password_length = int(password_length_str)
            if password_length <= 0:
                print("Error: Password length must be a positive number.")
                continue  # ask for input again
            break  # exit loop if input is valid
        except ValueError:
            print("Error: Please enter a valid integer for the length.")

    # Get character inclusion/exclusion options
    print("\nSelect character types to include (yes/no or y/n):")

    # Helper function to parse yes/no response
    def ask_yes_no(prompt):
        while True:
            response = input(prompt).lower().strip()
            if response in ['yes', 'y', 'да', 'д', 'lf']:  # Russian options kept for flexibility
                return True
            elif response in ['no', 'n', 'нет', 'н', 'net']:  # Russian options
                return False
            else:
                print("Please answer 'yes' or 'no' ('y' or 'n').")  # translate prompt

    include_lower = ask_yes_no("Include lowercase letters (a-z)? ")
    include_upper = ask_yes_no("Include uppercase letters (A-Z)? ")
    include_digits = ask_yes_no("Include digits (0-9)? ")
    include_symbols = ask_yes_no("Include special symbols (!@#$%^&*()...)? ")

    # Generate and print the password
    try:
        generated_password = generate_password(
            password_length,
            include_lowercase=include_lower,
            include_uppercase=include_upper,
            include_digits=include_digits,
            include_symbols=include_symbols
        )
        print("\n--- Your Generated Password ---")
        print(generated_password)
        print("-----------------------------------")

    except ValueError as e:
        print(f"\nError generating password: {e}")
        sys.exit(1)  # exit with an error code