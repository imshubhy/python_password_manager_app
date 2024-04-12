from cryptography.fernet import Fernet
import os
import mysql.connector


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
        cursor.execute("SELECT user, password FROM passwords")
        rows = cursor.fetchall()
        if not rows:
            print("No saved passwords. Please add passwords first.")
            return
        for user, encrypted_pass in rows:
            decrypted_pass = decrypt_password(encrypted_pass, key)
            print("User:", user, "| Password:", decrypted_pass)
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Function to add a new password
def add_password(key):
    name = input('Account Name: ')
    pwd = input("Password: ")
    encrypted_pwd = encrypt_password(pwd, key)
    try:
        cursor.execute("INSERT INTO passwords (user, password) VALUES (%s, %s)", (name, encrypted_pwd))
        db.commit()
        print("Password added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()


# Main function
def main_menu(key):
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
    # Connect to MySQL
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="projectdb"
        )
        cursor = db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS passwords (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), password TEXT)")
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    key = load_key()
    main_menu(key)
