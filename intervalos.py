#Intervalos Python


class Intervalo:
	
	def __init__(this,cierreA,extremoA,extremoB,cierreB):
		this.extremoA = extremoA
		this.cierreA = cierreA
		this.extremoB = extremoB
		this.cierreB = cierreB
	
	def longitud(this):
		return this.extremoB - this.extremoA
	
	def valor(this):
		aux_cierreA = '('
		aux_cierreB = ')'
			
		if(this.cierreA == 1):
			aux_cierreA = '['
		if(this.cierreB == 1):
			aux_cierreB = ']'
		
			
		return aux_cierreA + str(this.extremoA) + ',' + str(this.extremoB) + aux_cierreB
		

	def union(this,intervalo): 
		#función para sumar intervalos (union)
		
		
		if (this.extremoA < intervalo.extremoA and intervalo.extremoA < intervalo.extremoB and intervalo.extremoB < this.extremoB ):  #a<c<d<b --> ((a,b))
			return 'A ' + str(this.valor())
		   #intervalo.extremoA < this.extremoA < this.extremoB < intervalo.extremoB
		elif (intervalo.extremoA < this.extremoA and this.extremoA < this.extremoB and this.extremoB < intervalo.extremoB):  #c<a<b<d --> ((c,d))
			this.extremoA = intervalo.extremoA
			this.extremoB = intervalo.extremoB
			return 'B ' + str(this.valor())
			#this.extremoA < this.extremoB < intervalo.extremoA < intervalo.extremoB
		elif (this.extremoA < this.extremoB and this.extremoB < intervalo.extremoA  and intervalo.extremoA < intervalo.extremoB ):		#a<b<c<d or 
			return 'C ' + str(this.valor()) + ' U ' + str(intervalo.valor())
			#intervalo.extremoA<intervalo.extremoB <this.extremoA<this.extremoB
		elif (intervalo.extremoA<intervalo.extremoB and intervalo.extremoB <this.extremoA and this.extremoA<this.extremoB ): #c<d<a<b que no solapen nada
			return 'D ' + str(intervalo.valor()) + ' U ' + str(this.valor())
		elif (intervalo.extremoA < this.extremoA): #intercalados por la izquierda C-----a----D----b
			this.extremoA = intervalo.extremoA
			return 'E ' + str(this.valor())
		elif (this.extremoA < intervalo.extremoA): #intercalados por la derecha. a-----C----b---D
			this.extremoB = intervalo.extremoB
			return 'F ' + str(this.valor())
		else:
			#quedan todavia casos que tener en cuenta, pero de momento nos vale.
			return 0
		

class ListaIntervalos:

		def __init__(this):
			#se declara un array que contendrá los intervalos
			this.lista=[]
		
		
		def add(this,intervalo):
			this.lista.append(intervalo)
		
		
		def mostrar(this): 
			resultado = ''
			"""
			for (let i=0;i<this.lista.length;i++){
				resultado +=' ' + this.lista[i]
			"""
			
			for i in this.lista:
				print(i.valor())
				
				resultado +=' ' + str(i.valor())
				#return resultado
			print('----:' + resultado)
			
		
		
		def contar(this):
			return len(this.lista)

		def borrar(this,item):
			this.lista.pop(item)
		
		
		
		
		
#Parte de la comprobación de la clase definida anteriormente
int1 = Intervalo(0,1,6,1)
print(int1.valor())

int2 = Intervalo(0,3,5,0)
print(int2.valor())

print('-*-*-*-*-*-* UNION int1 + int 2 -*-*-*-*-*-*-*-*')

print(int2.union(int1))

print('-*-*-*-*-*-* Lista de Intervalos -*-*-*-*-*-*-*-*')

li = ListaIntervalos()
li.add(int1)
li.add(int2)
li.add(int1)
int3 = Intervalo(0,0,0,0)
li.add(int3)
li.add(int2)

print(li.contar())
print(li.mostrar())
print(li.mostrar())
