def border():
    print("========================================================="
            "===========================")

def show_bernas():
    while True:
        border()
        print("\t\t\tHello! I am Ernesto P. Bernas!")
        border()
        print("1. Personal Information")
        print("2. Goals")
        print("3. Hobbies")
        print("4. Motto")
        print("5. Exit")
        border()
        print("\t\t\t\tTEAMMATES COMMENTS")
        border()
        print("Buenacifra's comment: Good job! Keep it up!")
        print("Roldan's comment: Keep dreaming, keep doing.")
        print("Tero's comment: Good luck and stay consistent! ")
        
        choice = input("\nPlease select an option(1-5): ")
        
        if choice == '1':
            border()
            print("\t\t\t\tPERSONAL INFORMATION")
            border()
            print("Name: Ernesto P. Bernas")
            print("Age: 20")
            print("Birthday: 1/11/2005")
            print("Address: Bagumbayan, Taguig City")
            print("School: PUP - Taguig")
            print("Course: BSIT\n")
            continue
        if choice == '2':
            border()
            print("\t\t\t\t\tGOALS")
            border()
            print("Priority as of now: To pass this course,"
                    " To have Latin Honors, Be Happy in Life.\n")
            continue
        elif choice == '3':
            border()
            print("\t\t\t\t\tHOBBIES")
            border()
            print("Doing Artworks, Playing Sports, Badminton" 
                    ", Swimming, Taekwondo, and Cooking.\n")
            continue
        elif choice == '4':
            border()
            print("\t\t\t\t\tMOTTO")
            border()
            print("Keep on Moving Forward!\n")
            continue
        elif choice == '5': 
            border()
            print("Exiting...")
            border()
            break
        print("Invalid option. Please try again.") 
        continue

bernas = show_bernas()   