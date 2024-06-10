print ("calculadora")
num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))
print("elija una operación 's' para suma, 'r' para resta,'m' para multiplicacion y 'd' para division ")
operacion = input("digite la operacion: ").upper()

if operacion=='S':
   suma = num1+num2
   print(f"\nla suma es: {suma}")
elif  operacion=='R':
    resta = num1-num2
    print(f"\nla resta es: {resta}")
elif  operacion=='M':
    mult =  num1*num2
    print(f"\nla multiplicacion es: {mult}")
elif  operacion=='D':
    div=num1/num2
    print(f"\nla division es: {div:.2}")

else:
    print("error al  elegir la operacion")
    

