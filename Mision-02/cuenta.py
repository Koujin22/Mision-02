# Autor: Emiliano Heredia Garcia    A01377072
# Descripcion:Calcula precio de comida agregando 13% propina y 15% impuestos

# Escribe tu programa después de esta línea.


org = int(input("Ingrese total:"))
imp = org*.15
prop = org*.13
total = org+imp+prop
print("La propina es de: %.2f"%prop)
print("El impuesto es de: %.2f"%imp)
print("El precio total es de: %.2f" %total)