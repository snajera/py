"""
print('------------- Generalidades-------------')

pacientes = ['123','4456','2345','56778']
print(len(pacientes))
print(pacientes[2])

print('Añado un nuevo')
pacientes.append('9999')

for y in pacientes:
	print('UNO '  + y)

	
def multi(n):
	return lambda a: a*n

mydoble=multi(2)
mytriple=multi(3)

print(mytriple(21))

print('-------------CLASES 1-------------------')

class Cuadrado:
	def __init__(self,ladoA,ladoB):
		self.ladoA = ladoA
		self.ladoB = ladoB

	def area(self):
		print('El área es: ' + str(self.ladoA*self.ladoB))
		
c1 = Cuadrado(10,20)
print(c1.ladoA)
print(c1.ladoB)
c1.area()

print('-------------CLASES 2-------------------')

class Cuadrado:
	def __init__(this,ladoA,ladoB):
		this.ladoA = ladoA
		this.ladoB = ladoB

	def area(this):
		print('El área es: ' + str(this.ladoA*this.ladoB))
		
c1 = Cuadrado(10,20)
print(c1.ladoA)
print(c1.ladoB)
c1.area()

print('-------------Iteradores-------------------')

pac = iter(pacientes)

print(next(pac))
print(next(pac))
print(next(pac))

cadena = 'Susana'
cad = iter(cadena)
print(next(cad))
print(next(cad))
print(next(cad))
print(next(cad))

for z in cadena:
	print(z)
	
print('-------------Objeto Iterador-------------------')

class MisNumeros:
	def __iter__(self):
		self.a = 0
		return self
	
	def __next__(self):
		
		if self.a <= 20:		
			x = self.a
			self.a +=1
			return x
		else:
			raise StopIteration

miClase = MisNumeros()

miIter = iter(miClase)

print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
for j in miIter:
	print(j)
"""	
def saludos():
	print('HOLA!!!!')
	
if (1 ==1 and 2==1):
	print("hola de nuevo")
