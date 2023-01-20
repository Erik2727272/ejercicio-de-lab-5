#Calcular la diferencia simétrica entre 3 conjuntos

conjunto_A = {1, 2, 3, 4, 8, 10, 20, 45, 100, 234}
conjunto_B = {4, 6, 8, 12, 45, 87, 89, 45, 90}
conjunto_C = {12, 45, 87, 89, 45, 8, 5 , 999, -1}

conjunto_A = set(conjunto_A)
conjunto_B = set(conjunto_B)
conjunto_C = set(conjunto_C)

union_de_todo= conjunto_A| conjunto_B| conjunto_C
interseccion_de_todo= conjunto_A & conjunto_B &  conjunto_C


diferencia_simetrica= print(union_de_todo - interseccion_de_todo)

