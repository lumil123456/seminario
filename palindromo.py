def palindromo(cad):
	cadena = cad[::-1]
	if cadena== cad:
		return True
	else:
		return False
cad=raw_input("ingrese una palabra:")
if palindromo(cad)==True:
	print ("True")
else:
	print("False")
palindromo(cad)