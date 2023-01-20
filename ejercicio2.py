#Calcular la diferencia entre dos conjuntos


colores_1= ["negro","verde","blanco","verde"]
colores_2= ["verde","amarillo","gris","violeta","negro"]

colores_1=set(colores_1)
colores_2=set(colores_2)

diferencia= colores_1.difference(colores_2)

print(diferencia)
