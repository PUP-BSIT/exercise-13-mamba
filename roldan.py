def border():
    print("========================================================="
            "===========================")

def show_roldan():
    while True:
        border()
        print("\t\t\tHello! I'm Gian Rafael Roldan.")
        border()
        print("1. Personal Information")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("\t\t\t\tTEAMMATES COMMENTS")
        border()
        print("Bernas comment: Good, I like your code!")
        print("Buenacifra comment: Have fun coding!")
        print("Tero comment: Nice hobby!")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            border()
            print("\t\t\t\t\tPERSONAL INFORMATION")
            border()
            print(
                "Name: Gian Rafael B. Roldan\n"
                "Age: 20\n"
                "Birthday: 08/08/2004\n"
                "Address: New Lower Bicutan, Taguig\n"
                "School: PUP-Taguig\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '2':
            border()
            print("\t\t\t\t\tGOALS")
            border()
            print("My goal is winning in silence, "
                  "living in peace.\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '3':
            border()
            print("\t\t\t\t\tHOBBIES")
            border()
            print("I enjoy playing basketball, "
                  "nature tripping, "
                  "and exploring different cities.\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '4':
            border()
            print("\t\t\t\t\tMOTTO")
            border()
            print("My motto is: 'real eyes "
                  "realize real lies.'\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '5':
            border()
            print("Exiting...")
            border()
            break
        print("Invalid option. Please try again.") 
        continue