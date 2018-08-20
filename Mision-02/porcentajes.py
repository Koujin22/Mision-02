# Autor: Emiliano Heredia Garcia, A01377072
# Descripcion: A base de numero de mujeres y hombres se consigue total y porcentajes.

# Escribe tu programa después de esta línea.


hom = int(input("Ingrese numero de hombres: "))
muj = int(input("Ingrese numero de mujeres: "))

total = hom+muj
print("El total de alumnos es de: %i" % total)
print("El porcentaje de mujeres es de: %.1f "%(100*muj/total))
print("El porcentaje de hombres es de: %.1f "%(100*hom/total))
