# Autor: Emiliano Heredia, A01377072
# Descripcion: Calcula la distancia o tiempo en base a la velocidad.
# Escribe tu programa después de esta línea.


vel = int(input("Velocidad del auto en km/h: "))
print("Distancia recorrida en 7 horas %.1f" % (vel*7))
print("Distancia recorrida en 4.5 horas %.1f" % (vel*4.5))
print("Tiempo para recorrer 791 km: %.1f" % (791/vel))