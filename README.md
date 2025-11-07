# 🛡️ Cybersecurity Projects Collection

This repository contains a collection of simple Python scripts designed to practice fundamental cybersecurity concepts, scripting, and development logic.

---

## 📚 Project List

### 1. Simple Port Scanner (Project #2)
* **Purpose:** A Python script utilizing the built-in `socket` module to scan a target IP or hostname for commonly open TCP ports (22, 80, 443, etc.). This demonstrates basic network reconnaissance and socket programming.
* **Location:** [`port-scanner/simple_scanner.py`](./port-scanner/simple_scanner.py)

### 2. Password Checker Assistant (Project #1)
* **Purpose:** A Python script that checks a user-provided password against 5 core security rules (Length, Uppercase, Lowercase, Digit, Special Character) and assigns a strength rating.
* **Location:** [`password-checker/password_checker.py`](./password-checker/password_checker.py)

### 3. Cyber Terminology Explainer Chatbot (Project #3)
* **Purpose:** A rule-based chatbot that uses keyword matching to provide definitions for cybersecurity terms (Malware, Phishing, VPN, etc.).
* **Location:** [`cyber_chatbot.py`](./cyber_chatbot.py)
* *Note: Detailed usage and examples for the chatbot are listed below.*

---

## 🤖 Detailed Usage: Cyber Terminology Explainer

### 💡 How It Works

The chatbot uses a large Python dictionary (`CORE_TERMS`) to store terms (keywords) and their definitions. When a user inputs a sentence, the bot:

1.  Converts the input to lowercase.
2.  Scans the input for any keywords (like "phishing," "malware," or "encryption").
3.  Returns the corresponding definition.

It is designed to be flexible, meaning you don't need to ask an exact question to get an answer!

### 🚀 Getting Started

#### Prerequisites

* **Python 3.x** installed on your system.

#### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR REPO URL HERE]
    ```
2.  **Navigate to the directory:**
    ```bash
    cd Cybersecurity-Projects
    ```
3.  **Run the Chatbot:**
    ```bash
    python cyber_chatbot.py
    ```

#### 💬 Sample Interaction

| User Input | Expected Bot Response |
| :--- | :--- |
| `'What is malware?'` | Malware is any software designed to harm or gain unauthorized access to a computer system... |
| `'Define encryption for me.'` | Encryption is the process of converting information or data into a code, to prevent unauthorized access... |
| `'hello'` | Hello! I am a simple Cyber Terminology Explainer... |

---

## ✨ Future Improvements

- Implement a separate file (e.g., a JSON file) for the term definitions to keep the Python script cleaner.
- Add more advanced matching using libraries like NLTK to better understand user intent.
- Expand the knowledge base to include common security tips.