from calculator import *

def main():
    while True:
        print("\nSz�mol�g�p")
        print("M�veletek:")
        print("1. �sszead�s")
        print("2. Kivon�s")
        print("3. Szorz�s")
        print("4. Oszt�s")
        print("5. Hatv�nyoz�s")
        print("6. N�gyzetgy�k")
        print("7. Sz�zal�k sz�m�t�s")
        print("8. Mem�ria t�rol�s")
        print("9. Mem�ria hozz�ad�s")
        print("10. Mem�ria kivon�s")
        print("11. Mem�ria t�rl�s")
        print("12. Mem�ria el�h�v�s")
        print("0. Kil�p�s")

        choice = input("V�lassz m�veletet: ")

        if choice == '0':
            break

        try:
            if choice in ('1', '2', '3', '4', '5', '7'):
                num1 = float(input("Els� sz�m: "))
                num2 = float(input("M�sodik sz�m: "))

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
                num = float(input("Sz�m: "))
                print(square_root(num))
            elif choice in ('8','9','10'):
                mem_val = float(input("Mem�ria �rt�k: "))
                if choice == '8':
                    memory_store(mem_val)
                    print("�rt�k t�rolva a mem�ri�ban")
                elif choice == '9':
                    memory_add(mem_val)
                    print("�rt�k hozz�adva a mem�ri�hoz")
                elif choice == '10':
                     memory_subtract(mem_val)
                     print("�rt�k kivonva a mem�ri�b�l")
            elif choice == '11':
                memory_clear()
                print("Mem�ria t�r�lve")
            elif choice == '12':
                print(f"Mem�ria �rt�ke: {memory_recall()}")
            else:
                print("�rv�nytelen bemenet")
        except ValueError:
            print("�rv�nytelen bemenet. Sz�mot adj meg!")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()