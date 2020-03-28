class archivos:
	def IngrasarDatos(self,nombre,datos):
		infile = open(nombre,"a")
		infile.write(datos + '\n')
		infile.close()
	def LeerDatos(self,nombre):
		infile = open(nombre,"r")
		datos = infile.read()
		infile.close()
		return datos
							
class usuario:
	nombres = ""
	password = ""
	datos = ""
	def registrar(self):
		nombre = input('ingrese su nombre de usuario: ' )
		apellido = input('ingrese su apellido completo: ')
		correo = input('ingrese su correo electronico: ')
		contra = input('ingrese una contraseña para este usuario ')
		datos = (nombre + '\n' + apellido + '\n' + correo + '\n' + contra + '\n')
		return datos
		print("Su registro se ha realizado con exito :D ")
		
	def InicarCesion(self,Usuarios,PassWord):
		Usuario = input("ingrese su Nombre de usaurio: ")
		Pass = input("ingrese su contraseña: ")	
		if(Usuario in Usuarios  and Pass in PassWord ):
			if(usuario=="admin" and Pass == "12345678" ):
				print(Usuarios)
					
			else:
				c = False
				while c ==False:
					print('bienvenido ', Usuario)
					print('|1| para Sumar ')
					print('|2| para Restar')
					print('|3| pqra Multiplicar')
					print('|4| para Dividir')
					op = input('Elija una opcion: ')
					y = False
					while y == False:
						try:
							num1 = input('ingrese el primer numero: ')
							num2 = input('ingrese el segundo numero: ')
							y = True
						except:
							print("solo numero amigo mio : D ")
					if(op == '1'):
						resultado = float(num1) + float(num2)
						print('el resultado es :  ', str(resultado))
						m = input("presione enter para continuar")
						break
					elif(op == '2'):
						resultado =  float(num1) - float(num2)
						print('el resultado es :  ', str(resultado))
						m = input("presione enter para continuar")
						break
					elif(op == '3'):
						resultado =  float(num1) * float(num2)
						print('el resultado es :  ', str(resultado))
						m = input("presione enter para continuar")
						break
					elif(op == '4'):
						resultado =  float(num1) / float(num2)
						print('el resultado es :  ', str(resultado))
						m = input("presione enter para continuar")
						break
					elif op == '5':
						print('graxcias por usar el prgrama')
						m = input("presione enter para continuar")
						exit()
					else:
						print('esta opcion no existe ')
				return True
		
		else: 
			return False
			
user = usuario()
archivo = archivos()
h = False
while h == False:
	print("|1| Regitrase")
	print("|2| Iniciar sesion")
	print("|3| Salir")
	selec = input("Elija una opcion: ")

	if selec == "1" : 
		datos= user.registrar()
		archivo.IngrasarDatos("Datos.txt", datos)
	elif selec == "2":
		Usuarios = archivo.LeerDatos("Datos.txt")
		PassWord = archivo.LeerDatos("Datos.txt")
		user.InicarCesion(Usuarios,PassWord)
	elif selec == "3":
		print("gracias por usar este programas UwU")
		n = input("presine cualquier tecla para continuar")
		exit()
	else:
		print("esta opcion no existe ")
