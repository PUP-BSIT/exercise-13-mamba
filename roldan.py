def border():
    print("-" * 60)

def show_roldan():
    while True:
        border()
        print("Hello! I'm Gian Rafael B. Roldan.")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("Team Comments:")
        print("Bernas comment: Good, I like your code!")
        print("Buenacifra comment: Have fun coding!")
        print("Tero comment: ")
        border()
        choice = input("Please select an option (1-5): ")
        border()

        if choice == '1':
            border()
            print(
                "Name: Gian Rafael B. Roldan\n"
                "Age: 20\n"
                "Birthday: 08/08/2004\n"
                "Address: New Lower Bicutan, Taguig\n"
                "School: PUP-Taguig\n"
                "Course: BSIT"
            )
            border()
            continue
        elif choice == '2':
            border()
            print("My goal is Winning in silence, "
                  "living in peace.")
            border()
            continue
        elif choice == '3':
            border()
            print("I enjoy playing basketball, "
                  "nature tripping, "
                  "and exploring different cities.")
            border()
            continue
        elif choice == '4':
            border()
            print("My motto is: 'real eyes "
                  "realize real lies.'")
            border()
            continue
        elif choice == '5':
            border()
            print("Good bye!")
            border()
            break
        print("\nInvalid option. Please try again.")
        continue

roldan = show_roldan()