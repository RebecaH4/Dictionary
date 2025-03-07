#Rebe HC
#Diccionario
d1 = {"Nombre": "Samanta", "Edad": 27, "Direccion": "Tepeji", "e_mail": "sama@gmail.com"}
d2 = {"Nombre": "Maria", "Edad": 30, "Direccion": "Tula Hgo", "e_mail": "mari35@gmail.com"}
d3 = {"Nombre": "Jose", "Edad": 25, "Direccion": "Jilotepec", "e_mail": "pepe@gmail.com"}

#Imprimir diccionarios
#print(d1)
#print(d2)
#print(d2)

#Consulta/extrae una key
#print(d1['Nombre'])
#print(d1.get('Direccion'))

#Para modificar un elemento usar [] usando el key y asignar uno nuevo
#d2['Nombre'] = "Laura"
#print(d2)

#Si el key no exixte se añade
#d1['cp'] = 54240
#print(d1)

#values()--> devuelve los valoes del diccionario sin los keys
#print(list(d1.values()))

#popitem----> elimina el ultimo elemento del diccionario
#d1.popitem()
#print(d1)

#pop-----> puede eliminar un elemento en particular
#salida = d1.pop('Edad')
#print(d1)

#update---> llama un diccionario y tiene como entrada otro diccionario
#t1 = {'a': 100, 'b': 200}
#t2 = {'e': 50, 'd': 400}
#t1.update(t2)
#print(t1)
