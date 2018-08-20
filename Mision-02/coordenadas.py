# Autor: Emiliano Heredia Garcia, A01377072
# Descripcion: Calcula la distancia entre dos cordenadas

# Escribe tu programa después de esta línea.


x1 = int(input("Ingrese x1: "))
x2 = int(input("Ingrese x2: "))
y1 = int(input("Ingrese y1: "))
y2 = int(input("Ingrese y2: "))
x = x2-x1
y = y2-y1
d = ((x**2)+(y**2))**.5
print("Distancia: %.4f"%d)
