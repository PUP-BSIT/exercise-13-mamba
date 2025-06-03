def border():
    print("========================================================="
          "===========")

def show_tero():
    while True:
        border()
        print("Hello! I'm Altheno Mari L. Tero.")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("Team Comments:")
        print("Bernas comments: Clean Coding Structure!")
        print("Buenacifra comments: Great use of functions!")
        print("Roldan comments: ")
        border()
        choice = input("Please select an option (1-5): ")
        border()

        if choice == '1':
            border()
            print("Name: Altheno Mari L. Tero\n"
                    "Age: 20\n"
                    "Birthday: 11/23/2004\n"
                    "Address: Ususan, Taguig\n"
                    "School: PUP-Taguig\n"
                    "Course: BSIT"
                    )
            border()
            input = ("Press 'Enter' to proceed.")
            continue
        elif choice == '2':
            border()
            print("My goal is to graduate from school,"
                    " achieve financial stability,"
                    " improve my physical fitness and be happy.")
            border()
            input = ("Press 'Enter' to proceed.")
            continue
        elif choice == '3':
            border()
            print("I love playing basketball and"
                    " going to the gym to workout.")
            border()
            input = ("Press 'Enter' to proceed.")
            continue
        elif choice == '4':
            border()
            print("My motto is: 'You miss 100% of the chances you don't take.'")
            border()
            input = ("Press 'Enter' to proceed.")
            continue
        elif choice == '5':
            border()
            print("Nice to meet you, Bye!")
            border()
            input = ("Press 'Enter' to proceed.")
            break
        print("\nInvalid option. Please try again.")
        continue