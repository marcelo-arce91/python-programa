saldo=1000
print("\tMenu del cajero ")
print("1. ingresar dinero a la cuenta")
print("2. retirar dinero de la cuenta")
print("3. mostrar dinero disponible")
print("4. salir")

opcion = int(input("elija una opcion del menu: "))
print()
if opcion == 1:
    extra = float(input(" cuanto dinero desea ingresar a la cuenta: "))
    saldo += extra
    print(f" el dinero que hay en la cuenta es de: {saldo} ")

elif opcion== 2:
     retirar = float(input(" cuanto dinero desea retirar de la cuenta: "))
     if retirar>saldo:
       print(" no tiene esa cantidad de dinero en la cuenta ")
     else:
         saldo-=retirar
         print(f"su dinero en la cuenta es :{saldo}")
elif opcion== 3:
     print(f"su dinero en la cuenta es :{saldo}")
elif opcion== 4:
    print(" gracias por usar el cajero automatico ")
else:
    print("Error se esquivoco de opcion del menu")


        