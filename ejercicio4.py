def ValorCadena(x, y):
	a=len(x)
	b=len(y)
	if a > b:
		print x
	else:
		if a==b:
			print x + y
		else:
			print y
e=raw_input("insertar una primera palabra o cadena:")
f=raw_input("insertar una segunda palabra o cadena:")
ValorCadena(e, f)
