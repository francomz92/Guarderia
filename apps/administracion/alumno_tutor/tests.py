from django.test import TestCase
from .models import Tutor, Alumno
from datetime import datetime


class TutorTest(TestCase):

	# def test_longitud_nombre(self):
	# 	se_puede = True
	# 	try:
	# 		nombre = 'abcdefghijklmnopqrstuvwxyz12345' # 31 Caracteres
	# 		Tutor.objects.create(nombre=nombre,
	# 							 apellido='Sebastian',
	# 							 dni=1234567,
	# 							 telefono=12345678,
	# 							 direccion='La Pampa 319')
	# 	except Exception as err:
	# 		se_puede = False
	# 	finally:
	# 		self.assertEqual(se_puede, False)

	# def test_longitud_apellido(self):
	# 		se_puede = True
	# 		try:
	# 			apellido = 'abcdefghijklmnopqrstuvwxyz12345' # 31 Caracteres
	# 			Tutor.objects.create(nombre='Sebastian',
	# 								apellido=apellido,
	# 								dni=1234567,
	# 								telefono=12345678,
	# 								direccion='La Pampa 319')
	# 		except Exception as err:
	# 			se_puede = False
	# 		finally:
	# 			self.assertEqual(se_puede, False)

	def test_dni_unico(self):
		se_puede = True
		try:
			Tutor.objects.create(nombre='Fraasdasdnco',
								 apellido='asdasd',
								 dni=1234567,
								 telefono=1234148,
								 direccion='La Pampa 319')

			Tutor.objects.create(nombre='sdnco',
								 apellido='FRdasd',
								 dni=1234567,
								 telefono=12341,
								 direccion='La Pampa')
		except Exception as err:
			se_puede = False
		finally:
			self.assertEqual(se_puede, False)

	def test_to_JSON(self):
		try:
			Tutor.objects.create(nombre='Fraasdasdnco',
								 apellido='asdasd',
								 dni=12345678,
								 telefono=1234148,
								 direccion='La Pampa 319')
			registro_toJSON = Tutor.objects.get(dni=12345678).toJSON()
		except Exception as err:
			registro_toJSON = {'err': str(err)}
		finally:
			diccionario = {
				'id': 1,
				'nombre': 'Fraasdasdnco',
				'apellido': 'asdasd',
				'dni': 12345678,
				'telefono': 1234148,
				'direccion': 'La Pampa 319'
			}
			self.assertDictEqual(registro_toJSON, diccionario)


class AlumnoTest(TestCase):
	def setUp(self) -> None:
		Tutor.objects.create(nombre='Franco',
							 apellido='Sebastian',
							 dni=12,
							 telefono=12345678,
							 direccion='La Pampa 319')
		self.tutor = Tutor.objects.get(dni=12)
		return super().setUp()

	# def test_longitud_nombre(self):
	# se_puede = True
	# try:
	# 	nombre = 'abcdefghijklmnopqrstuvwxyz12345'  # 31 Caracteres
	# 	Alumno.objects.create(nombre=nombre,
	# 						  apellido='FRdasd',
	# 						  dni=1,
	# 						  fecha_nacimiento=datetime.strptime('16/04/1992', '%d/%m/%Y'),
	# 						  tutor=self.tutor)
	# except Exception as err:
	# 	print('ERROR ->', err)
	# 	se_puede = False
	# finally:
	# 	self.assertEqual(se_puede, False)

	# def test_longitud_apellido(self):
	#     se_puede = True
	#     try:
	#         apellido = 'abcdefghijklmnopqrstuvwxyz12345'  # 31 Caracteres
	#         Alumno.objects.create(nombre='FRdasd',
	#                               apellido=apellido,
	#                               dni=1,
	#                               fecha_nacimiento=datetime.strptime('16/04/1992', '%d/%m/%Y'),
	#                               tutor=self.tutor)
	#     except Exception as err:
	#         se_puede = False
	#     finally:
	#         self.assertEqual(se_puede, False)

	def test_dni_unico(self):
		se_puede = True
		try:
			Alumno.objects.create(nombre='Fraasdasdnco',
								  apellido='asdasd',
								  dni=2,
								  fecha_nacimiento=datetime.strptime(
									  '16/04/1992', '%d/%m/%Y'),
								  tutor=self.tutor)

			Alumno.objects.create(nombre='sdnco',
								  apellido='FRdasd',
								  dni=2,
								  fecha_nacimiento=datetime.strptime(
									  '16/04/1992', '%d/%m/%Y'),
								  tutor=self.tutor)
		except Exception as err:
			se_puede = False
		finally:
			self.assertEqual(se_puede, False)


	def test_fecha_nacimietno_futura(self):
		pass



class AsistenciaTest(TestCase):
	def setUp(self) -> None:
		Tutor.objects.create(nombre='Franco',
							 apellido='Sebastian',
							 dni=12,
							 telefono=12345678,
							 direccion='La Pampa 319')
		tutor = Tutor.objects.get(dni=12)
		Alumno.objects.create(nombre='Fraasdasdnco',
							  apellido='asdasd',
							  dni=2,
							  fecha_nacimiento=datetime.strptime(
								  '16/04/1992', '%d/%m/%Y'),
							  tutor=tutor)
		self.alumno = Alumno.objects.get(dni=2)
		return super().setUp()

