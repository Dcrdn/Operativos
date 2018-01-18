
string="Alo me llamo diego diego diego"
string2="diego"

lista1=string.split(" ")
lista2=string2.split(" ")
st1=set(lista1)
st2=set(lista2)
st=set()
for element in range(5,15):
	st.add(element)


fechas=[("1-10-2018")]
elementos=fechas.split("-")
dias="1234567"
month="123456789dot"
primerDia="4"

while(True):
	current=4
	
"""
print(st1&st2) #interseccion
print(st1-st2) #a-b
print(st1^st2) #(a-b)u(b-a)
print(st1|st2) #aub
print(st1 >= st2) #if st2 is subset of st1
print(st2 <= st1) #if stt1 is subset of st2
"""

for x in range(0,10):
	if x not in st:
		print(x)
