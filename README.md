# 🤖 Simple Cyber Terminology Explainer Chatbot

This is a rule-based chatbot built in Python designed to provide quick definitions for common cybersecurity terms. It is a beginner project intended to practice basic Python logic, dictionaries, and string manipulation for keyword matching.

---

## 💡 How It Works

The chatbot uses a large Python dictionary (`CORE_TERMS`) to store terms (keywords) and their definitions. When a user inputs a sentence, the bot:

1.  Converts the input to lowercase.
2.  Scans the input for any keywords (like "phishing," "malware," or "encryption").
3.  Returns the corresponding definition.

It is designed to be flexible, meaning you don't need to ask an exact question to get an answer!

## 🚀 Getting Started

### Prerequisites

* **Python 3.x** installed on your system.

### Installation and Setup

1.  **Clone the Repository:** ```bash
    git clone [YOUR REPO URL HERE]
    ```
2.  **Navigate to the directory:**
    ```bash
    cd simple-cyber-chatbot
    ```
3.  **Run the Chatbot:**
    ```bash
    python cyber_chatbot.py
    ```

## 💬 Sample Interaction

| User Input | Expected Bot Response |
| :--- | :--- |
| `What is malware?` | Malware is any software designed to harm or gain unauthorized access to a computer system... |
| `Define encryption for me.` | Encryption is the process of converting information or data into a code, to prevent unauthorized access... |
| `hello` | Hello! I am a simple Cyber Terminology Explainer... |

## ✨ Future Improvements

* Implement a separate file (e.g., a JSON file) for the term definitions to keep the Python script cleaner.
* Add more advanced matching using libraries like NLTK to better understand user intent.
* Expand the knowledge base to include common security tips.