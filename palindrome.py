#function that says if a word is palindrome
#it takes o(n) time
def isP(palabra):
	original=list(palabra)
	volteada=list(palabra[::-1])
	iguales=0
	for element in range(0,len(palabra)):
		if(original[element]==volteada[element]):
			iguales+=1
	print(iguales)
	return(iguales==len(palabra))

palabra="perroorrep"
#print(isP(palabra))

#parecido, pero si encuentro una letra diferente regresa falso
def isPa(palabra):
	original=list(palabra)
	volteada=list(palabra[::-1])
	for element in range(0,len(palabra)):
		if(original[element]!=volteada[element]):
			return False
	return True

palabra="perroorrep"
print(isPa(palabra))

#LOOOOOOOOOOOOOL, amo python o(n) for the string size and o (1) for the comparison
def is_palindrome(input_string):
    return input_string == input_string[::-1]
