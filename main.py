# Function to generate and save encryption key

def generate_key():
    # This function is not needed since we are not using encryption
    pass


# Function to load encryption key

def load_key():
    # This function is not needed since we are not using encryption
    pass


# Function to encrypt password (not needed in this case)
def encrypt_password(password, key):
    return password


# Function to decrypt password (not needed in this case)
def decrypt_password(encrypted_password, key):
    return encrypted_password


# Function to view passwords
def view_passwords():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                print(line.rstrip())
    except FileNotFoundError:
        print("Password file not found.")


# Function to add a new password
def add_password():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
    print("Password added successfully.")


# Main function
def main():
    while True:
        mode = input(
            "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view_passwords()
        elif mode == "add":
            add_password()
        else:
            print("Invalid mode.")


if __name__ == "__main__":
    main()


# Function to generate and save encryption key

def generate_key():
    # This function is not needed since we are not using encryption
    pass


# Function to load encryption key

def load_key():
    # This function is not needed since we are not using encryption
    pass


# Function to encrypt password (not needed in this case)
def encrypt_password(password, key):
    return password


# Function to decrypt password (not needed in this case)
def decrypt_password(encrypted_password, key):
    return encrypted_password


# Function to view passwords
def view_passwords():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                print(line.rstrip())
    except FileNotFoundError:
        print("Password file not found.")


# Function to add a new password
def add_password():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
    print("Password added successfully.")


# Main function
def main():
    while True:
        mode = input(
            "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view_passwords()
        elif mode == "add":
            add_password()
        else:
            print("Invalid mode.")


