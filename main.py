from attack_simulator import brute_force_attack, dictionary_attack, password_strength

def menu():

    while True:

        print("\nCyber Attack Simulator")
        print("1 Brute Force Attack")
        print("2 Dictionary Attack")
        print("3 Check Password Strength")
        print("4 Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            password = input("Enter a short password (3 characters only): ")
            brute_force_attack(password)

        elif choice == "2":

            password = input("Enter password to test: ")
            dictionary_attack(password)

        elif choice == "3":

            password = input("Enter password: ")
            strength = password_strength(password)
            print("Password strength:", strength)

        elif choice == "4":
            break

        else:
            print("Invalid choice")

menu()