#lol, sí funciona con duplicados, pero no con n numeros parecidos
def duplicate_items(list_numbers):
    list_numbers.sort()
    seen=[]
    for element in range(1,len(list_numbers)):
    	if(list_numbers[element]==list_numbers[element-1]):
    		seen.append(list_numbers[element])
    return(seen)

a=[4,4,5,6,5]
#a.sort()
#print(duplicate_items(a))

#lo hago con diccionarios ;) tiene tiempo o(n) y o(1) de mis consultas
def duplicado(lista):
	dic={}
	for element in range(len(lista)):
		if(lista[element] in dic):
			vistas=dic[lista[element]]
			dic[lista[element]]=vistas+1
		else:
			dic[lista[element]]=1
	return(dic)

answer=duplicado(a)
seen=[]
for key,value in answer.items():
	if(value>1):
		seen.append(key)

print(answer)
print(seen)