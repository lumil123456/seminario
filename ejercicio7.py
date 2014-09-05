def secuencia(x):
	a=x
	cant=1
	con=1
	while cant<=a:
		while con<=cant:
			print cant,
			con=con+1
		print" "
		cant=cant+1
		con=1
	cant=a-1
	while a >=1:
		while con<=cant:
			print cant,
			con=con+1
		print" "
		cant=cant-1
		con=1
		a=a-1
e=input ("insertar un numero:")
secuencia(x)