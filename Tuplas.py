t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')#se creo una tupla
print (t)#se imprimio la tupla
print (len(t))#se imprimio el numero de conjuntos contenidos en la tupla


print ('=====================================')#se imprime un separador
print (t[0])#se imprimio el valor del conjunto de la posicion 0 de la tupla
print (t[3])#se imprimio el valor del conjunto de la posicion 3 de la tupla
print (t[1:3])#se imprimio el valor de los conjuntos de las posiciones de la 1 a la 3 sin contar la 3 de la tupla
print (t[3][1])#se imprimio el valor de la posicion numero 1 del conjunto de la posicion 3 de la tupla


print ('====================================')#se imprime un separador
print (t[3])#se imprimio el valor del conjunto de la posicion 3 de la tupla
t[3].append('lorito')#se le agrego 'lorito' al elemento de la posicion 3 de la tupla
print (t)#se imprimio la tupla

print ('====================================')#se imprime un separador
for elemento in t:#se creo un ciclo para imprimir separadamente cada conjunto de la tupla
    print (elemento)

print ('====================================')#se imprime un separador
for index in range(0,len(t)):#se creo un ciclo en donde se almaceno en una variable los conjuntos de las posiciones de la 0 a la 5 de la tupla
    print (t[index])#se imprimio la variable

print ('====================================')#se imprime un separador
if 'a' in t:#se creo un condicional que se realizara si encuentra 'a' en la tupla
    print ("El elemento 'a' esta en la tupla")#se imprime una frase resultante del condicional

print ('====================================')#se imprime un separador
lista=list(t)#se guardaron los datos de la tupla en una variable 'lista'
lista[1]='A'#se agrego 'A' en la posicion numero 1 de la variable con los datos de la tupla
print (lista)#se imprime la variable 'lista'

tupla=tuple(lista)#se crea una variable que contiene los datos de la variable 'lista' y la cambia por una tupla
print (tupla)#se imprime la nueva tupla

print ('====================================')#se imprime un separador
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]#se crea una variable de lista con distintos valores
for x, y in l:#se crea un ciclo con las variables 'x' y 'y'
    print (x, ':', y)#se imprime los primeros valores de cada conjunto de la lista(x) y luego sus valores correspondientes(y)