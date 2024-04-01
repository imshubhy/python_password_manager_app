from cryptography.fernet import Fernet
import os


# Function to generate and save encryption key

# encryption key required for any operation e.g. -> encrypting and decrypting
def generate_key():
    key = Fernet.generate_key()                # generating the key here
    with open("key.key", "wb") as key_file:    # creating key file
        key_file.write(key)                    # saving the key into key_file


# Function to load encryption key

def load_key():          # need to have the key for encrypting and decrypting the password.
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
                data = line.rstrip()
                user, encrypted_pass = data.split("|")
                decrypted_pass = decrypt_password(encrypted_pass, key)
                print("User:", user, "| Password:", decrypted_pass)
    except FileNotFoundError:
        print("Password file not found.")


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
        mode = input(
            "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view_passwords(key)
        elif mode == "add":
            add_password(key)
        else:
            print("Invalid mode.")


if __name__ == "__main__":
    main()
