from calculator import *

def main():
    while True:
        print("\nSzámológép")
        print("Mûveletek:")
        print("1. Összeadás")
        print("2. Kivonás")
        print("3. Szorzás")
        print("4. Osztás")
        print("5. Hatványozás")
        print("6. Négyzetgyök")
        print("7. Százalék számítás")
        print("8. Memória tárolás")
        print("9. Memória hozzáadás")
        print("10. Memória kivonás")
        print("11. Memória törlés")
        print("12. Memória elõhívás")
        print("0. Kilépés")

        choice = input("Válassz mûveletet: ")

        if choice == '0':
            break

        try:
            if choice in ('1', '2', '3', '4', '5', '7'):
                num1 = float(input("Elsõ szám: "))
                num2 = float(input("Második szám: "))

                if choice == '1':
                    print(add(num1, num2))
                elif choice == '2':
                    print(subtract(num1, num2))
                elif choice == '3':
                    print(multiply(num1, num2))
                elif choice == '4':
                    print(divide(num1, num2))
                elif choice == '5':
                    print(power(num1, num2))
                elif choice == '7':
                    print(percentage(num1, num2))
            elif choice == '6':
                num = float(input("Szám: "))
                print(square_root(num))
            elif choice in ('8','9','10'):
                mem_val = float(input("Memória érték: "))
                if choice == '8':
                    memory_store(mem_val)
                    print("Érték tárolva a memóriában")
                elif choice == '9':
                    memory_add(mem_val)
                    print("Érték hozzáadva a memóriához")
                elif choice == '10':
                     memory_subtract(mem_val)
                     print("Érték kivonva a memóriából")
            elif choice == '11':
                memory_clear()
                print("Memória törölve")
            elif choice == '12':
                print(f"Memória értéke: {memory_recall()}")
            else:
                print("Érvénytelen bemenet")
        except ValueError:
            print("Érvénytelen bemenet. Számot adj meg!")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()