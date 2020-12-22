def conversor(pais_pesos, valorDolar):
    pesos = input("Por favor ingrese la cantidad de pesos " + pais_pesos + " que tienes: ")
    pesos = float(pesos)
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")



menu = """
⚡⚡ PASE Y CAMBIE SU DINERO ⚡⚡

1 👉 Conversion de dolares a pesos Colombianos
2 👉 Conversion de dolares a pesos Mexicanos
2 👉 Conversion de dolares a pesos Argentinos


Elija la opcion que quiere convertir """
opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)  
elif opcion == 2:
    conversor("Mexicanos", 24)  
elif opcion == 3:
    conversor("Argentinos", 65)  

else:
    print("Elija unicamente los valores que ahi se encuentran")

# if opcion == 1:
#     pesos = input("Por favor ingrese la cantidad de pesos Colombianos que tienes: ")
#     pesos = float(pesos)
#     valorDolar = 3875 
#     dolares = pesos / valorDolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# elif opcion == 2:
#     pesos = input("Por favor ingrese la cantidad de pesos Mexicanos que tienes: ")
#     pesos = float(pesos)
#     valorDolar = 24 
#     dolares = pesos / valorDolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# elif opcion == 3:
#     pesos = input("Por favor ingrese la cantidad de pesos Argentinos que tienes: ")
#     pesos = float(pesos)
#     valorDolar = 65 
#     dolares = pesos / valorDolar
#     dolares = round(dolares, 2)
#     dolares = str(dolares)
#     print("Tienes $" + dolares + " dolares")
# else:
#     print("Elija unicamente los valores que ahi se encuentran")










# pesos = input("Por favor ingrese la cantidad de epsos colombianos que tienes: ")
# pesos = float(pesos)
# valorDolar = 3875 
# dolares = pesos / valorDolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dolares")

#crear este mismo programa pero usando condicionales, para usarlo en pesos argentinos y mexicanos, recuerda que un dolar equivale a 65 en arg y 24 en mex

