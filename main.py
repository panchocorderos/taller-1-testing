from datetime import datetime
import re

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
class Person:
  def __init__(self, name, bday, age, isAthlete, gender, dateWeight, weight, height):
        self.name = name #name person
        self.bday = bday #birth day date
        self.age = age
        self.isAthlete = isAthlete #bool physical condition
        self.gender = gender #gender (man or woman)
        self.dateWeight = dateWeight #date weigh
        self.weight = weight # weight in kg
        self.height = height #height in mt
        self.imc = 0
        self.interpretation = " "

  def getIMC(self):
    self.imc = (float(self.weight)/(float(self.height)**2))

  def getInterpretation(self):
    if (self.gender == "M"):
      if (self.imc < 20):
        self.interpretation = "BAJO PESO"
      elif (self.imc >= 20 and self.imc <= 24.9):
        self.interpretation = "NORMAL"
      elif  (self.imc >= 25 and self.imc <= 29.9):
        self.interpretation = "OBSESIDAD LEVE"

      elif  (self.imc >= 30 and self.imc <= 40):
        self.interpretation = "OBESIDAD SEVERA"
      elif  (self.imc < 40):
        self.interpretation = "OBESIDAD MUY SEVERA"

    else:
      if (self.imc < 20):
        self.interpretation = "BAJO PESO"
      elif (self.imc >= 20 and self.imc <= 23.9):
        self.interpretation = "NORMAL"
      elif (self.imc >= 24 and self.imc <= 28.9):
        self.interpretation = "OBSESIDAD LEVE"

      elif (self.imc >= 29 and self.imc <= 37):
        self.interpretation = "OBESIDAD SEVERA"
      elif (self.imc < 37):
        self.interpretation = "OBESIDAD MUY SEVERA"


  def showInfo(self):
    print("\n\n")
    print("-------- Info --------")
    print("|")
    print("|  Nombre: "+self.name)
    print("|  edad: "+self.age)
    print("|  Fecha Nacimiento: "+self.bday)
    print("|  ¿Hace ejercicio?: "+self.isAthlete)
    print("|  Genero: "+self.gender)
    print("|  Peso: "+self.weight + " Kg")
    print("|  Altura: "+self.height + " M")
    print("|  IMC: "+str(self.imc))
    print("|  Interpretacion: "+self.interpretation)
    print("|")
    print("|  Fecha Registro: "+self.dateWeight)
    print("|")
    print("----------------------")
    print("\n")






def validarNombre(name):
  # Acepta solo letras, espacios y tildes
  regex = re.compile(r"^[a-zA-Z\u00C0-\u017F\s]+$", re.U)
  # print(name, regex.match(name) is not None)
  return regex.match(name) is not None


def validarIsAthlete(Athlete):
  # Acepta solo si y no
  regex = re.compile(r'^(?:SI|NO)$', re.U)
  # print(Athlete, regex.match(Athlete) is not None)
  return regex.match(Athlete) is not None

def validarGender(gender):

  # Acepta solo M y F
  regex = re.compile(r'^(?:M|F)$', re.U)
  # print(gender, regex.match(gender) is not None)
  return regex.match(gender) is not None


def validarheight(num):
  # Acepta solo numeros 1 | 1.1 | 1.12 | 1.123
  regex = re.compile(r'^(\d{1})([.]\d{1,3})?$', re.U)
  # print(num, regex.match(num) is not None)
  return regex.match(num) is not None

def validarWeight(weight):
  # Acepta solo numeros 1 | 12 | 135
  regex = re.compile(r'^(\d{1,3})([.]\d{1,2})?$', re.U)
  # print(weight, regex.match(weight) is not None)
  return regex.match(weight) is not None

def calcularEdad(fecha):
  dateNow = datetime.now()

  try:
    objetoFecha = datetime.strptime(fecha, '%d/%m/%Y') # Trasforma la fecha ingresada en objeto dateTime
    edad = dateNow.year - objetoFecha.year - ((dateNow.month, dateNow.day) < (objetoFecha.month, objetoFecha.day)) # Tambien se puede relativedelta
  except:
    # raise TypeError("Formato ingresado es invalido")

    return "Error"
  else:
    return [True, edad] if(edad >= 15 and edad <= 70)else(False)





def ingresarDatos():
  print("------------- Ingreso -------------")
  name = input("|  Ingrese nombre: ")
  nameValidar = validarNombre(name)
  while not nameValidar:
    print("Error nombre invalido, solo se aceptan letras")
    name = input("|  Ingrese nombre: ")
    nameValidar = validarNombre(name)

  bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
  edad = calcularEdad(bday) # entre 1950 a 2005
  while (edad == "Error") or (not edad[0]):
    if not edad[0]:
      print("      -------- Error --------")
      print("      Debe tener entre 15 a 70 años")
      bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
      edad = calcularEdad(bday)  # entre 1950 a 2005
    else:
      print("Error Formato ingresado es invalido")
      bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
      edad = calcularEdad(bday)

  isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().upper()
  isAthleteValidar = validarIsAthlete(isAthlete)
  while not isAthleteValidar:
    print("\nError: Solo es valido [Si / No]\n")
    isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().upper()
    isAthleteValidar = validarIsAthlete(isAthlete)

  gender = input("|  Genero [M/F]: ").strip().upper()
  genderValidar = validarGender(gender)
  while not genderValidar:
    print("Error: Solo es valido [M / F]")
    gender = input("|  Genero [M/F]: ").strip().upper()
    genderValidar = validarGender(gender)
  if gender == "M":
    gender = "Masculino"
  else:
    gender = "Femenino"

  weight = input("|  Peso[Kg]: ").strip().replace(",", ".")
  weightValidar = validarWeight(weight)
  while (not weightValidar) or (float(weight) == 0):

    if float(weight) == 0:
      print("\nError: no se puede ingresar 0\n")
      weight = input("|  Peso[K]: ").strip().replace(",", ".")
      weightValidar = validarWeight(weight)
    else:
      print("Error: solo es valido hasta tres digitos o hasta tres digitos y dos decimales")
      weight = input("|  Peso[K]: ").strip().replace(",", ".")
      weightValidar = validarWeight(weight)

  height = input("|  Altura[M]: ").strip().replace(",", ".")
  heightValidar = validarheight(height)
  while (not heightValidar) or (float(height) == 0):
    print(height)
    if float(height) == 0:
      print("\nError: no se puede ingresar 0\n")
      height = input("|  Altura[M]: ").strip().replace(",", ".")
      heightValidar = validarheight(height)
    else:
      print("Error: Solo es valido un digito o un digito y hasta 3 decimales")
      height = input("|  Altura[M]: ").strip().replace(",", ".")
      heightValidar = validarheight(height)


  print("|")
  print("----------------------")
  dateNow = datetime.now().strftime("%d/%m/%Y")
  print(edad)
  return Person(name, bday, str(edad[1]), isAthlete, gender, str(dateNow), weight, height)

def buscarDatos():
  pass


if __name__ == "__main__":

  storagePerson = []

  ciclo = True
  while ciclo:

    print("------------- APP IMC -------------")
    print("|")
    print("|  | 1 | Ingresar")
    print("|  | 2 | Buscar")
    print("|  | 3 | Salir")
    print("|")
    opcion = input("|  Ingrese la opcion: ")
    print("|")
    print("----------------------")
    print("\n")

    if opcion == "1":
      # dateNow = datetime.now().strftime("%d/%m/%Y")
      # nuevoIngreso = Person("Daniel", "24/12/1999", "N", "Masculino", dateNow, "50", "2")
      # nuevoIngreso.getIMC()
      # nuevoIngreso.getInterpretation()
      # nuevoIngreso.showInfo()
      # storagePerson.append(nuevoIngreso)

      nuevoIngreso = ingresarDatos()
      nuevoIngreso.getIMC()
      nuevoIngreso.getInterpretation()
      nuevoIngreso.showInfo()
      storagePerson.append(nuevoIngreso)
    elif opcion == "2":

      nameSearch = input("|  Ingrese nombre a buscar: ")
      nameValidar = validarNombre(nameSearch)
      if not nameValidar:
        print("\nError nombre invalido, solo se aceptan letras\n")
      else:
        objetoUsuario = list(filter(lambda objeto: objeto.name == nameSearch,storagePerson))

        if len(objetoUsuario) != 0:
          for i in objetoUsuario:
            i.showInfo()
        else:
          print("\n   Usuario no encontrado\n")

    elif opcion == "3":
      ciclo = False
    else:
      print("  Opcion Invalida")