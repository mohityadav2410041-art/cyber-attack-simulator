\# Cyber Attack Simulator (Educational CLI Tool)



\##  Project Description



The Cyber Attack Simulator is a command-line based Python application designed to demonstrate how common cyber attacks such as brute force attacks and dictionary attacks work.



This tool helps users understand:

\- How weak passwords can be cracked

\- How attackers attempt multiple password combinations

\- Why strong passwords are important



 This project is developed strictly for educational purposes and does NOT perform real cyber attacks.



\---



\##  Objective



The objective of this project is to create awareness about cybersecurity by simulating basic attack techniques in a safe and controlled environment.



\---



\##  Technologies Used



\- Python 3

\- Command Line Interface (CLI)

\- Text File (wordlist.txt for dictionary attack)



\---



\##  Project Structure



oss-audit-24BCY10041/



main.py → User interface and menu system



attack\_simulator.py → Contains attack logic



wordlist.txt → List of common passwords



README.md → Project documentation



requirements.txt → Dependencies (empty)



\---



\##  Installation \& Setup



Follow these steps to run the project on your system.



\---



\### Step 1: Install Python



Download Python from:

https://www.python.org/downloads/



During installation:

✔ Check "Add Python to PATH"



\---



\### Step 2: Clone the Repository



Open Command Prompt and run:



git clone https://github.com/mohityadav2410041-art/oss-audit-24BCY10041.git



\---



\### Step 3: Navigate to Project Folder



cd oss-audit-24BCY10041



\---



\### Step 4: Run the Program



python main.py



\---



\## ▶️ How to Use the Application



After running the program, you will see the following menu:



Cyber Attack Simulator



1 Brute Force Attack  

2 Dictionary Attack  

3 Check Password Strength  

4 Exit  



\---



\### ➤ Option 1: Brute Force Attack



\- Enter a password (only 3 characters recommended)

\- The system will try all combinations

\- It will display each attempt

\- When the correct password is found, it stops



Example:



Enter password: abc  

→ Program tries combinations until it finds "abc"



\---



\### ➤ Option 2: Dictionary Attack



\- Enter a password

\- The program checks it against a predefined wordlist

\- If the password is in the list, it will be cracked



Example:



Enter password: admin  

→ Found in wordlist → Password cracked



\---



\### ➤ Option 3: Password Strength Checker



\- Enter any password

\- The system checks:

&#x20; - Length

&#x20; - Uppercase letters

&#x20; - Numbers

&#x20; - Special characters



Output:



Weak / Medium / Strong



\---



\### ➤ Option 4: Exit



Closes the application



\---



\##  How It Works



\### Brute Force Attack

The system generates all possible combinations of characters and tries each one until the correct password is found.



\### Dictionary Attack

The system uses a predefined list of common passwords (wordlist.txt) and checks if the password exists in that list.



\### Password Strength Checker

The system evaluates password strength based on complexity rules.



\---



\##  Data Files



wordlist.txt:

Contains commonly used passwords for dictionary attack simulation.



You can edit this file to add more passwords.



\---



\##  Example Run



1 Brute Force Attack  

Password: abc  

→ Cracked after multiple attempts  



2 Dictionary Attack  

Password: admin  

→ Found in wordlist  



3 Password Strength  

Password: Pass@123  

→ Strong  



\---





\## Ethical Disclaimer



This project is created for educational purposes only.



It demonstrates how cyber attacks work to help users understand security risks and improve password safety.



It must NOT be used for any illegal or unethical activity.



\---



\##  Features Summary



✔ Brute force attack simulation  

✔ Dictionary attack simulation  

✔ Password strength analysis  

✔ Educational cybersecurity concepts  

✔ Command-line based  

✔ No external libraries required  



\---



\##  Author



Mohit



\---



\##  Conclusion



This project helps users understand the importance of strong passwords and how attackers exploit weak security practices. It serves as a basic introduction to cybersecurity concepts and attack methodologies.

