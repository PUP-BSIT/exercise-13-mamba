from bernas import show_bernas
from buenacifra import show_buenacifra
from roldan import show_roldan
from tero import show_tero

def main_menu():
    while True:
        print("\nWelcome to the Main Menu!")
        print("1. Ernesto Bernas III")
        print("2. Abrianne Buenacifra")
        print("3. Gian Rafael Roldan")
        print("4. Altheno Mari Tero")
        print("5. Exit")

        choice = input("\nPlease select an option (1-5): ")

        if choice == '1':
            show_bernas()
            continue
        elif choice == '2':
            show_buenacifra()
            continue
        elif choice == '3':
            show_roldan()
            continue
        elif choice == '4':
            show_tero()
            continue
        elif choice == '5':
            print("Exiting...")
            break
        print("Invalid choice. Please try again.")
        continue

main_menu()