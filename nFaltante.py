#encontrar el numero que falta del 1 al 10 en una lista de numeros

#suponiendo que solo falta un elemento
def faltantes(lista):
	sumatotal=0
	for element in range(1,11):
		sumatotal+=element
	suma=0
	for element in lista:
		suma+=element
	if(suma!=sumatotal):
		return(sumatotal-suma)

lista=[1,2,4,5,8,9,10]
todos=[1,2,3,4,5,6,7,8,9,10]
#print(faltantes(lista))


#para n elementos
def faltan(lista,todos):
	missing=[]
	for element in todos:
		if element not in lista:
			missing.append(element)
	return(missing)
#print(faltan(lista,todos))

#con sets

def fal(lista,todos):
	return(list(set(todos)-set(lista)))

print(fal(lista,todos))
