huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}#se esta declarando el diccionario llamado huespedes

print (huespedes)#se esta imprimiendo el diccionario
print (huespedes.items())#se esta imprimiendo cada item del diccionario por aparte

print (huespedes.keys())#se esta imprimiendo unicamente las claves del diccionario
for key in huespedes:#se realizo un ciclo para imprimir las claves del diccionario
    print (key)

print (huespedes.values())#se esta imprimiendo unicamente los valores del diccionario
for key in huespedes:#se realizo un ciclo para imprimir los valores del diccionario
    print (huespedes[key])
print()#se imprimio un espacio

for habitacion in huespedes:#se realizo un ciclo para imprimir cada clave con su valor del diccionario
    print (habitacion,':',huespedes[habitacion])
print()#se imprimio un espacio
for habitacion,huesped in huespedes.items():#no seeeeeeee
    print (habitacion,':',huespedes[key])
for indice, key in enumerate(huespedes):#se realizo un ciclo para enumerar cada grupo de clave y valor del diccionario
    print (indice+1,key,huespedes[key])
print()#se imprimio un espacio

print (huespedes[105])#se imprimio el valor de la clave 105
print (huespedes.get(105))#se imprimio el valor de la clave 105

print ('====================================')#se imprimio un separador

huespedes[102]='Fanny Lu'#se esta declarando una clave y valor al diccionario
huespedes[107]='Don Omar'#se esta declarando una clave y valor al diccionario
huespedes.setdefault('109','Luis Miguel')#se esta declarando una clave y valor en la que la clave no se encontraba antes en el diccionario

for huesped in huespedes.items():#se realizo un ciclo para imprimir cada clave con su valor incluyendo los recientemente agregados, pero como no se declaro la variable de habitacion, no se pudo imprimir correctamente cada item
    print (habitacion,':',huesped)
print()#se imprimio un espacio

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}#se creo una variable para agregar dos nuevos items
huespedes.update(registroshoy)#se cargaron los datos de la variable al diccionario
for habitacion, huesped in huespedes.items():#se realizo un ciclo para imprimir cada clave con su valor incluyendo los recientemente agregados
    print (habitacion,':',huesped)
print()#se imprimio un espacio

print ('====================================')#se imprimio un separador

huespedes[107]='Ricky Martin'#se agrego un nuevo item al arreglo
print (huespedes)#se imprimio el diccionario completo

print ('====================================')#se imprimio un separador

del huespedes[102]#se borro el item con clave 102
huespedes.pop(202)#se borro el item con clave 202
print(huespedes)#se imprimio el diccionario completo

print ('====================================')#se imprimio un separador

copia1=huespedes.copy()#se creo una variable que contiene la copia del diccionario
print ('copia1: ',copia1)#se imprime la variable de la copia del diccionario
copia2={}#se creo un diccionario vacio
copia2.update(huespedes)#se le cargaron los datos del diccionario completo al nuevo diccionario
print ("copia2: ",copia2)#se imprime el segundo diccionario

print ('====================================')#se imprimio un separador

lista=[2,5,7,1]#se agrego un arreglo
diccio=dict.fromkeys(lista,"xxx")#se creo una variable que se convirtio en diccionario y contiene como clave los elementos del arreglo y le asigno un mismo valor "xxx"
print(diccio)#se imprimio la variable diccio

print ('====================================')#se imprimio un separador
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}#se creo un diccionario
print (inventario)#se imprimio el diccionario
inventario["cartera"].sort()#se ordenan alfabeticamente los elementos del conjunto "cartera" del diccionario
print(inventario)#se imprime el diccionario con los cambios anteriores
inventario["cartera"].remove("Moneda")#se remueve el elemento "moneda" del conjunto 'cartera' del diccionario
print(inventario)#se imprime el diccionario con los nuevo cambios
print(inventario.get("plata")[0])#se imprime el valor de la posicion 0 del elemento 'plata' del diccionario