# password_checker.py

import string # <--- ADD THIS LINE HERE

# password_checker.py
# ... rest of your original code ...
def check_password_strength(password):
    # 1. Initialize the score and a list to hold feedback messages
    score = 0
    feedback = []

    # --- RULE CHECKS ---

    # 2. Check for Length (8 characters or more)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("[-] Must be at least 8 characters long.")

    # 3. Check for Uppercase Letters
    # The 'any()' function checks if at least one character satisfies the condition
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("[-] Must contain at least one uppercase letter.")

    # 4. Check for Lowercase Letters
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("[-] Must contain at least one lowercase letter.")

    # 5. Check for Digits (Numbers)
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("[-] Must contain at least one number (0-9).")

    # --- UPDATED SCORE EVALUATION ---

    if score == 5:
        strength = "Excellent" # NEW Top Tier!
        message = "👑 Excellent! Your password meets all advanced requirements."
    elif score == 4:
        strength = "Strong"
        message = "✅ Strong. Your password meets all core requirements."
    elif score == 3:
        strength = "Moderate"
        message = "⚠️ Good, but could be stronger. Review the feedback below."
    else:
        strength = "Weak"
        message = "❌ Weak. Your password is too easy to guess. Review the feedback below."
        
    return strength, message, feedback

# --- MAIN PROGRAM ---

if __name__ == "__main__":
    print("--- Simple Password Strength Checker ---")
    
    # Get user input
    user_password = input("Enter a password to check: ")
    
    # Run the checker function
    strength, message, feedback_list = check_password_strength(user_password)
    
    print("\n--- RESULTS ---")
    print(f"Overall Strength: {strength}")
    print(f"Message: {message}")
    
    # Print specific feedback if the password is not strong
    if strength != "Strong":
        print("\nFeedback:")
        for item in feedback_list:
            print(item)