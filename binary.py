#binario a decimal
def toD(n):
	print(int(n,2))

#decimal a binario
def toB(n):
	dec_num = int(n)
	cnv_bin = ''

	while dec_num> 0:   
		print(dec_num)
		print(dec_num%2)     
		if dec_num%2 == 0:
			cnv_bin += '0'

		else:
			cnv_bin += '1'
		dec_num = dec_num//2
	
	return(cnv_bin[::-1])

print(toB("10"))
