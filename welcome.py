#!/usr/bin/env python3
#Menu


plate1 = "Hamburguesa"
plate2 = "Hotdog"
plate3 = "Sandwich"

print("¡Bienvenido! Este es nuestro menu: \n ")
print(plate1, plate2, plate3, sep='\n')


pick = input("Elige platillo: ")
if pick == "Hamburguesa":
    from hamburguesa.py import hamburguesa
    print(hamburguesa)
elif pick == "Sandwich":
    from sandwich.py import sandwich
    print(sandwich)
elif pick == "Hotdog":
    from hotdog.py import hotdog
    print(hotdog)
else:
    print("No hay eso")