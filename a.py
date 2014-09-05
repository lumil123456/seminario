lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  
w=0  
print(lista)  
C=int(input("ingrese la cantidad de numeros que desea ingresar\n"))  
for i in range (C):  
	n=int(input("ingresa un numero\n"))  
	lista.append(n)  
T = len(lista)  
while(w!=(T-1)):  
	w=0  
	for k in range(T-1):  
		if(lista[k]<=lista[k+1]):  
			w=w+1  
		else:  
			tem=lista[k]  
			lista[k]=lista[k+1]  
			lista[k+1]=tem  
print(lista) 
