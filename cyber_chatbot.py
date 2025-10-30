import sys

# 1. THE CORE KNOWLEDGE BASE: Terms and Definitions
# Keys are the simple terms (keywords) to search for, in lowercase.
# Values are the chatbot's responses (the definitions).
CORE_TERMS = {
    # 1. THE CORE KNOWLEDGE BASE: Terms and Definitions

    "phishing": "Phishing is a cyber attack where criminals trick you into giving them sensitive information, often through fake emails or websites that look legitimate.",
    "malware": "Malware is any software designed to harm or gain unauthorized access to a computer system. This includes viruses, worms, ransomware, and spyware.",
    "firewall": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
    "vpn": "A VPN (Virtual Private Network) encrypts your internet connection and masks your IP address, providing a secure and private connection to a network.",
    "ddos": "A DDoS (Distributed Denial of Service) attack attempts to overwhelm a website or online service with a flood of internet traffic from multiple compromised computer systems, making it inaccessible to legitimate users.",
    "two-factor authentication": "Two-factor authentication (2FA) is a security process where a user provides two different authentication factors to verify themselves, like a password and a code from their phone.",
    # --- NEW TERM ADDED BELOW ---
    "encryption": "Encryption is the process of converting information or data into a code, to prevent unauthorized access. It scrambles data so it can only be read by authorized parties who have the correct decryption key.",

}

# The default response if the term is not found
DEFAULT_RESPONSE = "I'm sorry, I don't have a definition for that specific term yet. Try asking for 'phishing' or 'firewall'."

# --- Response Logic ---
def get_response(user_input: str) -> str:
    """
    Processes the user's input, checks for greetings, keywords, and returns the appropriate response.
    """
    # 1. Normalization: Convert to lowercase and remove extra spaces
    cleaned_input = user_input.lower().strip()
    
    # 2. Check for Greetings
    if "hello" in cleaned_input or "hi" in cleaned_input:
        return "Hello! I am a simple Cyber Terminology Explainer. Ask me about a core term like 'malware' or 'vpn'."
    
    # 3. Check for Farewell
    if cleaned_input in ["quit", "exit", "bye"]:
        return "Goodbye! Stay secure and informed."

    # 4. Check for Core Keyword Matches (The Smart Part)
    # This loop checks if any of the keys in CORE_TERMS exist *anywhere* in the user's input.
    for term, definition in CORE_TERMS.items():
        if term in cleaned_input:
            return definition
    
    # 5. Default Fallback
    return DEFAULT_RESPONSE

# --- Main Program Execution ---
def run_chatbot():
    """
    The main loop that starts and runs the chat session.
    """
    print("\n----------------------------------------------------")
    print("🤖 **Cyber Assistant Initialized**")
    print("Ask me about a term like 'malware' or 'what is a vpn'.")
    print("Type 'quit' or 'exit' to end the session.")
    print("----------------------------------------------------")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Get the bot's response
        response = get_response(user_input)
        
        # Check if the response is a special exit command, and break the loop
        if "Goodbye" in response:
            print(f"🤖: {response}")
            sys.exit() # Exits the script cleanly
        
        # Print the regular response
        print(f"🤖: {response}")

# This line ensures the chatbot only runs when you execute the script directly
if __name__ == "__main__":
    run_chatbot()