# hasher.py
import hashlib

# Define a fixed salt for demonstration purposes
# In a real application, this would be a unique, randomly generated string stored per user.
FIXED_SALT = "aB3c9XyZ7q"

def generate_sha256_hash(text, salt):
    """
    Generates a SHA-256 hash for the given text, combined with a salt.
    """
    try:
        # 1. Combine the salt and the text
        # The salt is prepended (added before) the text
        salted_text = salt + text
        
        # 2. Encode the salted string to bytes (required for hashing)
        encoded_text = salted_text.encode('utf-8')
        
        # 3. Create and run the hasher
        hasher = hashlib.sha256()
        hasher.update(encoded_text)
        
        return hasher.hexdigest()
        
    except Exception as e:
        return f"An error occurred during hashing: {e}"

# --- MAIN PROGRAM ---

if __name__ == "__main__":
    print("\n--- SHA-256 Hashing Utility (with Salt) ---")
    
    # Get user input
    user_input = input("Enter the string or password to hash: ")
    
    if not user_input.strip():
        print("[-] Input cannot be empty.")
    else:
        # Generate the hash using the input and the global salt
        hash_output = generate_sha256_hash(user_input, FIXED_SALT)
        
        print("\n--- RESULTS ---")
        print(f"Original Text: {user_input}")
        print(f"Salt Used: {FIXED_SALT}")
        print(f"Algorithm: SHA-256")
        print(f"Hash Output: {hash_output}")