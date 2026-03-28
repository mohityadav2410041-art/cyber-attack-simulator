import time

def brute_force_attack(correct_password):

    print("\nStarting Brute Force Attack...")

    chars = "abcdefghijklmnopqrstuvwxyz1234567890"

    attempts = 0

    for c1 in chars:
        for c2 in chars:
            for c3 in chars:

                guess = c1 + c2 + c3
                attempts += 1

                print("Trying:", guess)

                if guess == correct_password:
                    print("\nPassword cracked:", guess)
                    print("Attempts:", attempts)
                    return

    print("Password not found")


def dictionary_attack(correct_password):

    print("\nStarting Dictionary Attack...")

    attempts = 0

    with open("wordlist.txt", "r") as file:
        for word in file:

            guess = word.strip()
            attempts += 1

            print("Trying:", guess)

            if guess == correct_password:
                print("\nPassword cracked:", guess)
                print("Attempts:", attempts)
                return

    print("Password not found in wordlist")


def password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in "!@#$%" for c in password):
        score += 1

    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"