def border():
    print("========================================================="
            "===========================")

def show_tero():
    while True:
        border()
        print("\t\t\tHello! I'm Altheno Mari L. Tero.")
        border()
        print("1. Personal Information")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("\t\t\t\tTEAMMATES COMMENTS")
        border()
        print("Bernas comments: Clean Coding Structure!")
        print("Buenacifra comments: Great use of functions!")
        print("Roldan comments: Cool hobbies, Keep it up!\n")
        
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            border()
            print("\t\t\t\t\tPERSONAL INFORMATION")
            border()
            print("Name: Altheno Mari L. Tero")
            print("Age: 20")
            print("Birthday: 11/23/2004")
            print("Address: Ususan, Taguig City")
            print("School: PUP - Taguig")
            print("Course: BSIT\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '2':
            border()
            print("\t\t\t\t\tGOALS")
            border()
            print("My goal is to graduate from school,"
                    " achieve financial stability,"
                    " improve my physical fitness and be happy.\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '3':
            border()
            print("\t\t\t\t\tHOBBIES")
            border()
            print("I love playing basketball and"
                    " going to the gym to workout.")
            input("Press 'Enter' to proceed.\n")
            continue
        elif choice == '4':
            border()
            print("\t\t\t\t\tMOTTO")
            border()
            print("My motto is: 'You miss 100% of the"
                    "chances you don't take.\n")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '5':
            border()
            print("Nice to meet you, Bye!")
            border()
            input("Press 'Enter' to proceed.")
            break
        print("\nInvalid option. Please try again.")
        continue