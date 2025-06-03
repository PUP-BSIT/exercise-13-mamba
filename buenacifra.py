def border():
    print("========================================================="
          "===========")

def show_buenacifra():
    while True:
        border()
        print("Hello! I'm Abrianne Buenacifra.")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("Team Comments:")
        print("Bernas comments: Goodluck on your Goals!")
        print("Roldan comments: ")
        print("Tero comments: ")
        border()
        choice = input("Please select an option (1-5): ")
        border()

        if choice == '1':
            border()
            print("Name: Abrianne Buenacifra\n"
                    "Age: 20\n"
                    "Birthday: 04/27/2005\n"
                    "Address: New Lower Bicutan, Taguig\n"
                    "School: PUP-Taguig\n"
                    "Course: BSIT"
                    )
            border()
            continue
        elif choice == '2':
            border()
            print("My goal is to graduate with honors and"
                    " to have a successful career.")
            border()
            continue
        elif choice == '3':
            border()
            print("I enjoy reading manhwas and"
                    " watching documentaries.")
            border()
            continue
        elif choice == '4':
            border()
            print("My motto is: 'Do it scared.'")
            border()
            continue
        elif choice == '5':
            border()
            print("Good bye!")
            border()
            break
        print("\nInvalid option. Please try again.")
        continue

buenacifra = show_buenacifra()