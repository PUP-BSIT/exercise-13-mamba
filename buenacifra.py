def border():
    print("========================================================="
          "===========")

def show_buenacifra():
    while True:
        border()
        print("\t\t\tHello! I'm Abrianne Buenacifra.")
        border()
        print("1. Personal Information")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("\t\t\t\tTEAMMATES COMMENTS")
        border()
        print("Bernas' comment: Goodluck on your Goals!")
        print("Roldan's comment: ")
        print("Tero comments: ")

        choice = input("Please select an option (1-5): ")

        if choice == '1':
            border()
            print("\t\t\t\t\tPERSONAL INFORMATION")
            border()
            print("Name: Abrianne Buenacifra\n"
                    "Age: 20\n"
                    "Birthday: 04/27/2005\n"
                    "Address: New Lower Bicutan, Taguig\n"
                    "School: PUP-Taguig\n"
                    "Course: BSIT")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '2':
            border()
            print("\t\t\t\t\tGOALS")
            border()
            print("My goal is to graduate with honors and"
                    " to have a successful career.")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '3':
            border()
            print("\t\t\t\t\tHOBBIES")
            border()
            print("I enjoy reading manhwas and"
                    " watching documentaries.")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '4':
            border()
            print("\t\t\t\t\tMOTTO")
            border()
            print("My motto is: 'Do it scared.'")
            input("Press 'Enter' to proceed.")
            continue
        elif choice == '5':
            border()
            print("Good bye!")
            border()
            break
        print("\nInvalid option. Please try again.")
        continue