from cryptography.fernet import Fernet
import os


# Function to generate and save encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved successfully.")


# Function to load encryption key
def load_key():
    if not os.path.exists("key.key"):
        print("Encryption key not found. Generating a new key...")
        generate_key()
    with open("key.key", "rb") as key_file:
        return key_file.read()


# Function to encrypt password
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode()).decode()


# Function to decrypt password
def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password.encode()).decode()


# Function to view passwords
def view_passwords(key):
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()  # removing trailing space
                user, encrypted_pass = data.split("|")  # getting user and password from txt
                decrypted_pass = decrypt_password(encrypted_pass, key)
                print("User:", user, "| Password:", decrypted_pass)
    except FileNotFoundError:
        print("Password file not found, add password first!")


# Function to add a new password
def add_password(key):
    name = input('Account Name: ')
    pwd = input("Password: ")
    encrypted_pwd = encrypt_password(pwd, key)
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Password added successfully.")


# Main function
def main():
    key = load_key()
    while True:
        print("\nPassword Manager Menu:")
        print("1. View Passwords")
        print("2. Add Password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_passwords(key)
        elif choice == "2":
            add_password(key)
        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
