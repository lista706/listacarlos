class test: 
	def test(self):
		iterador = False
		puntos= 0
		while iterador == False:
			print("¿siente usted tos seca ( tos sin  flemas y con un sonido mas fuerte)? s/n")
			resp = input()
			if resp == 's' :
				puntos = puntos + 1
				break
			if resp == 'n' : 
				puntos = puntos
				break
		while iterador == False:
			print("¿siente usted dolor de garganta( un dolor agudo y  punsante)? s/n")
			resp = input()
			if resp == 's' :
				puntos =puntos + 1
				break
			if resp == 'n' : 
				puntos = puntos
				break
		while iterador == False:
			print("¿tiene usted secrecion nasal( en su mayoria flema de un color verde o blanco)? s/n")
			resp = input()
			if resp == 's' :
				break
				puntos = puntos + 1
			if resp == 'n' : 
				puntos = puntos
				break
		while iterador == False:
			print("¿siente usted dificultad para respirar? s/n")
			resp = input()
			if resp == 's' :
				puntos = puntos + 1
				break
			if resp == 'n' : 
				puntos = puntos
				break
				
		if  puntos == 4:
			return True
		else:
			return False

class persona:
	Datos = list()
	Paise = list()
	def caso(self,nombre,apellido,edad,fecha,pais,genero, test):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.fecha = fecha
		self.pais  = pais
		self.genero = genero
		self.test = test
		self.Datos = (self. nombre +" | "+ self.apellido +" | "+ self.edad+" | "+ self.fecha +" | "+ self.pais +" | "+ self.genero +" | "+ "test realizado: "+self.test)
		self.Paise.append(pais)

class registro(persona):
	def LeerCurados(self):
		curados = open("paises.txt", "r")
		ListaCurados= curados.readlines()
		curados.close()
		return ListaCurados
	def LeerFallecidos(self):
		fallecidos = open("paises.txt", "r")
		listaFallecidos= fallecidos.readlines()
		fallecidos.close()
		return listaFallecidos
	def LeerNEgativos(self):
		descartados = open("paises.txt", "r")
		listaDescartados= descartados.readlines()
		descartados.close()
		return listaDescartados
	def LeerPaises(self):
		paises = open("paises.txt", "r")
		listapaises= paises.readlines()
		paises.close()
		return listapaises
	def LeerCasos(self):
		casos = open("Casos.txt", "r")
		listaCasos = casos.readlines()
		casos.close
		return listaCasos
	def LeerPositivos(self):
		Positivos = open("CasosPositivos.txt","r")
		listaPositivos = Positivos.readlines()
		Positivos.close()
		return listaPositivos
		#archvios
	def archivoCasos(self):
		Casos = open("Casos.txt", "a")
		Casos.write(self.Datos +'\n')
		Casos.close()
	def archivoPositivos(self,confirmados):
		Positivos= open("CasosPositivos.txt", "a")
		Positivos.write(confirmados+'\n')
		Positivos.close()
	def archivoNegativos(descartados):
		negativos = open("CasosNegativos.txt", "a")
		negativos.write(descartados+'\n')
		negativos.close()
	def archivoFallecidos(self,bajas):
		fallecidos = open("Fallecidos.txt", "a")
		fallecidos.write(bajas+'\n')
		fallecidos.close()
	def archivoCurados(self,curado):
		Curados = open("Curados.txt","a"+'\n')
		Curados.write(curado+'\n')
		Curados.close()
	def archivoPaise(self):
		paises = open("paises.txt" , "a")
		for i in self.paise:
			paises.write(i)
		paises.close()	
iterado = False
registro = registro()
test = test()
while iterado  == False:
	print("                     *****************|ELIJA UNA POCION|*******************")
	print("")
	print("")
	print("                       ***************************************************")
	print("                       *  |1| registrar un nuevo caso                    *")
	print("                       *  |2| cambiar estatus de un caso                 *")
	print("                       *  |3| ver lista de fallecidos/curados            *")
	print("                       *  |4| ver la cantidad de casos por pais          *")
	print("                       *  |5| salir                                      *")
	print("                       ***************************************************")
	print("")
	op = input("                       ")
	
	if op == '1' :
		nombre = input("ingrese su nombre: " )
		apellido = input("ingrese su apellido: ")
		edad = input("ingrese su edad: ")
		fecha = input("ingrese su fecha de nacimiento( ejemplo: dia-mes-año ): ")
		pais =input("pais de residencia: ")
		genero = input("¿cual es su genero? M/F : ")
		c = test.test()
		registro.caso(nombre,apellido,edad,fecha,pais,genero,test)
		registro.archivoCasos()
		print("")
		print("se a registrado el caso con existo")
		print("")
		input("presione enter para continuar....")
	elif(op =='2'):
		iterador2 = False
		while iterador2 == False:
			print("¿QUE DESEA CAMBIA EN EL ESTATUS?")
			print("|1| para confimar caso")
			print("|2| para descartar caso")
			print("|3| para carfirmar un fallecido")
			print("|4| para confirmar una recuperacion")
			opcion = input("ingrese una opcion: ")
			if(opcion == '1'):
				listaCasos = registro.LeerCasos()
				ite = False
				while ite == False:
					j = 0
					for i in listaCasos:
						j = j +1
						print(str(j) +" " +i)

					print("ingrese el nombre de la persona a confirmar: ")
					nombre = input()
					print("ingrese el apellido de la persona a confirmar: ")
					apellido = input()
					for y in listaCasos:
						if nombre in y and apellido in y:
							confirmados = y
							archivo = open("Casos.txt","w")
							for k in listaCasos:
								if k != confirmados:
									archivo.write(k)
							archivo.close()
							break
					if confirmados == 	"" : 
						print("este pasiente no esta en la lista de casos ")
					else:
						registro.archivoPositivos(confirmados)	
						
			elif(opcion == '2'):
				listaCasos = registro.LeerCasos()
				ite = False
				while ite == False:
					j = 0
					for i in listaCasos:
						j = j +1
						print(str(j) +" " +i)

					print("ingrese el nombre de la persona a descartar: ")
					nombre = input()
					print("ingrese el apellido de la persona a descartar ")
					apellido = input()
					for y in listaCasos:
						if nombre in y and apellido in y:
							descartado  = y
							archivo = open("Casos.txt","w")
							for k in listaCasos:
								if k != descartado:
									archivo.write(k)
							archivo.close()
							break
					if descartado == 	"" : 
						print("este pasiente no esta en la lista de casos ")
					else:
						registro.archivoNegativos(descartado)	
			
			elif(opcion == '3'):
				listaCasos = registro.LeerPositivos()
				ite = False
				while ite == False:
					j = 0
					for i in listaCasos:
						j = j +1
						print(str(j) +" " +i)

					print("ingrese el nombre de la persona a descartar: ")
					nombre = input()
					print("ingrese el apellido de la persona a descartar ")
					apellido = input()
					for y in listaCasos:
						if nombre in y and apellido in y:
							fallecido  = y
							archivo = open("CasosPositivos.txt","w")
							for k in listaCasos:
								if k != fallecido:
									archivo.write(k)
							archivo.close()
							break	
					if fallecido == 	"" : 
						print("este pasiente no esta en la lista de casos ")
					else:
						registro.archivoFallecidos(fallecido)	

			elif(opcion == '4'):
				listaCasos = registro.LeerPositivos()
				ite = False
				while ite == False:
					j = 0
					for i in listaCasos:
						j = j +1
						print(str(j) +" " +i)

					print("ingrese el nombre de la persona que se a curado: ")
					nombre = input()
					print("ingrese el apellido de la persona que se a curado: ")
					apellido = input()
					for y in listaCasos:
						if nombre in y and apellido in y:
							curados  = y
							archivo = open("CasosPositivos.txt","w")
							for k in listaCasos:
								if k != curados:
									archivo.write(k)
							
							archivo.close()
							break
									
					if fallecido == 	"" : 
						print("este pasiente no esta en la lista de casos ")
					else:
						registro.archivoCurados(fallecido)
			else:
				iterador2 =False
	elif(op == '3'):
		listaCurados = registro.LeerCurados
		listaFallecidos = registro.LeerFallecidos
		for i in listaCurados:
			print(i)
		for j in listaFallecidos:
			print(j)
	elif(op == '4'):
		listaPaises = registro.LeerPaises
		listaPositivos = registro.LeerPositivos
		listaCurados = registro.LeerCurados
		listaFallecidos = registro.LeerFallecidos
		listaNegativos = registro.LeerNEgativos
		listaCasos = registro.LeerCasos
		for i in listaPaises:
			print(i)
			for j in listaCasos:
				if i in j :
					niño = 0
					adulto = 0
					AdultoMayor = 0
					if "20" in j: 
						niño = niño + 1
					else:
						if "199" in j or "198" in j or "197" in j or "196" in j:
							adulto =  adulto + 1
						else:
							AdultoMayor = AdultoMayor + 1
				print("Casos Posibles ")
				print ("hay niños: " + niño )
				print(" hay adultos: " + adulto)	
				print("hay  adultos mayores: " + AdultoMayor)	
					
			for j in listaPositivos:
				if i in j :
					niño = 0
					adulto = 0
					AdultoMayor = 0
					if "20" in j: 
						niño = niño + 1
					else:
						if"199" in j or "198" in j or "197" in j or "196" in j:
							adulto =  adulto + 1
						else:
							AdultoMayor = AdultoMayor + 1
				print("Casos positivos ")
				print ("hay niños: " + niño )	
				print(" hay adultos: " + adulto)	
				print("hay  adultos mayores: " + AdultoMayor)	
			for j in listaNegativos:
				if i in j :
					niño = 0
					adulto = 0
					AdultoMayor = 0
					if "20" in j: 
						niño = niño + 1
					else:
						if "199" in j or "198" in j or "197" in j or "196" in j:
							adulto =  adulto + 1
						else:
							AdultoMayor = AdultoMayor + 1
				print("Casos negativos ")
				print ("hay niños: " + niño )	
				print(" hay adultos: " + adulto)	
				print("hay  adultos mayores: " + AdultoMayor)	
			for j in listaFallecidos:
				if i in j :
					niño = 0
					adulto = 0
					AdultoMayor = 0
					if "20" in j: 
						niño = niño + 1
					else:
						if "199" in j or "198" in j or "197" in j or "196" in j:
							adulto =  adulto + 1
						else:
							AdultoMayor = AdultoMayor + 1
				print("Fallecidos ")
				print ("hay niños: " + niño )	
				print(" hay adultos: " + adulto)	
				print("hay  adultos mayores: " + AdultoMayor)	
			for j in listaCurados:
				if i in j :
					niño = 0
					adulto = 0
					AdultoMayor = 0
					if "20" in j: 
						niño = niño + 1
					else:
						if "199" in j or "198" in j or "197" in j or "196" in j:
							adulto =  adulto + 1
						else:
							AdultoMayor = AdultoMayor + 1
				print("curados ")
				print ("hay niños: " + niño )	
				print(" hay adultos: " + adulto)	
				print("hay  adultos mayores: " + AdultoMayor)	
	elif(op == '5'):
		print("gracias por usar este programa")
		input("preciones enter para continuar...")
		exit()
	else:
		iterado = False
