#print all the n numbers of the fibonacci serie
#memoria o(n) e igual tiempo
def fib(n):
	if n<1:
		return(False)
	if n==1 or n==2:
		return(1)
	serie=[1,1]
	for position in range(2,n+1):
		suma=serie[position-2]+serie[position-1]
		serie.append(suma)
	return(serie[n-1])

#memoria o(1) en tiempo o(n)
def fib2(n):
	if n<1:
		return(False)
	if n==1 or n==2:
		return(1)
	serie=[1,1]
	for time in range(2,n):
		suma=serie[0]+serie[1]
		arr=[]
		arr.append(serie[1])
		arr.append(suma)
		serie=arr
	return(serie[1])

num=int(input("Dime un número "))
ans=fib2(num)
#print(ans)

#mejor uso variables
def fib3(n):
	if n<1:
		return(False)
	if n==1 or n==2:
		return(1)
	a,b=1,1
	for time in range(2,n):
		suma=a,b
		a,b=b,suma
	return(b)

