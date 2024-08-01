import string
import random

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 1:
        print("Password length must be at least 1.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

        if length < 1:
            print("Password length must be at least 1.")
            continue

        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        
        if password:
            print(f"Generated Password: {password}")

        next_password = input("Do you want to generate another password? (yes/no): ")
        if next_password.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
