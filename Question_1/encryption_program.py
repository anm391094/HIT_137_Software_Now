import os

# Function to encrypt text using n and m
def encrypt(text, n, m):
    encrypted_text = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                encrypted_char = chr(((ord(char) - ord('a') + (n * m)) % 26) + ord('a'))
            elif 'n' <= char <= 'z':
                encrypted_char = chr(((ord(char) - ord('n') - (n + m)) % 26) + ord('n'))
            encrypted_text += encrypted_char
        elif char.isupper():
            if 'A' <= char <= 'M':
                encrypted_char = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            elif 'N' <= char <= 'Z':
                encrypted_char = chr(((ord(char) - ord('N') + m**2) % 26) + ord('N'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using n and m
def decrypt(text, n, m):
    decrypted_text = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                decrypted_char = chr(((ord(char) - ord('a') - (n * m)) % 26) + ord('a'))
            elif 'n' <= char <= 'z':
                decrypted_char = chr(((ord(char) - ord('n') + (n + m)) % 26) + ord('n'))
            decrypted_text += decrypted_char
        elif char.isupper():
            if 'A' <= char <= 'M':
                decrypted_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            elif 'N' <= char <= 'Z':
                decrypted_char = chr(((ord(char) - ord('N') - m**2) % 26) + ord('N'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Function to check if decryption is successful
def check_correctness(original, decrypted):
    return original == decrypted

# Function to read the original text from the raw_text.txt file in the same folder as the script
def load_original_text(folder_path):
    try:
        with open(os.path.join(folder_path, 'raw_text.txt'), 'r') as file:
            original_text = file.read()
        print(f"Original text: {original_text}")
        return original_text
    except FileNotFoundError:
        print("Error: 'raw_text.txt' file not found.")
        return None

# Main function to execute the encryption, decryption, and comparison
def main():
    folder_path = '/Users/anmshahariyar/Desktop/python/Assignment_2_S1_2025'  # Path to the folder containing raw_text.txt
    
    # Load the original text from the raw_text.txt file
    original_text = load_original_text(folder_path)
    
    if not original_text:
        return  # Exit if the file is not found
    
    # Get n and m values from user
    n = int(input("Enter the value of n: "))
    m = int(input("Enter the value of m: "))
    
    # Encrypt the text
    encrypted_text = encrypt(original_text, n, m)
    print(f"Encrypted text: {encrypted_text}")
    
    # Save the encrypted text to encrypted_text.txt
    with open(os.path.join(folder_path, 'encrypted_text.txt'), 'w') as file:
        file.write(encrypted_text)
    
    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, n, m)
    print(f"Decrypted text: {decrypted_text}")
    
    # Check if decryption is successful
    if check_correctness(original_text, decrypted_text):
        print("Decryption successful! The text matches the original.")
    else:
        print("Decryption failed! The text does not match the original.")

if __name__ == "__main__":
    main()
