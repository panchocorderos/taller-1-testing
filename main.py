from datetime import datetime
import re

# Requirements
# age >= 15 and age <= 70
# imc = weight/height**2
class Person:
  def __init__(self, name, bday, isAthlete, gender, dateWeight, weight, height):
        self.name = name #name person
        self.bday = bday #birth day date
        self.isAthlete = isAthlete #bool physical condition
        self.gender = gender #gender (man or woman)
        self.dateWeight = dateWeight #date weigh
        self.weight = weight # weight in kg
        self.height = height #height in mt


  def showInfo(self):
    print("-------- Info --------")
    print("|")
    print("|  "+self.name)
    print("|  "+self.bday)
    print("|  "+self.isAthlete)
    print("|  "+self.gender)
    print("|  "+self.dateWeight)
    print("|  "+self.weight)
    print("|  "+self.height)
    print("|")
    print("----------------------")





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
    print("Error Formato ingresado es invalido")
    return "Error"
  else:
    return True if(edad >= 15 and edad <= 70)else(False)


if __name__ == "__main__":

  print("------------- APP IMC -------------")
  name = input("|  Ingrese nombre: ")
  nameValidar = validarNombre(name)
  while not nameValidar:
    print("Error nombre invalido")
    name = input("|  Ingrese nombre: ")
    nameValidar = validarNombre(name)


  bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
  edad = calcularEdad(bday) # entre 1950 a 2005
  while (not edad) or (edad == "Error"):
    if not edad:
      print("      -------- Error --------")
      print("      Debe tener entre 15 a 70 años")
      bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
      edad = calcularEdad(bday)  # entre 1950 a 2005
    else:
      bday = input("|  Ingrese Fecha de nacimiento[24/12/1999]: ")
      edad = calcularEdad(bday)

  isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().upper()
  isAthleteValidar = validarIsAthlete(isAthlete)
  while not isAthleteValidar:
    print("Error: Solo es valido [Si / No]")
    isAthlete = input("|  ¿Hace ejercicio?[Si/No]: ").strip().upper()
    isAthleteValidar = validarIsAthlete(isAthlete)


  gender = input("|  Genero [M/F]: ").strip().upper()
  genderValidar = validarGender(gender)
  while not genderValidar:
    print("Error: Solo es valido [M / F]")
    gender = input("|  Genero [M/F]: ").strip().upper()
    genderValidar = validarGender(gender)


  weight = input("|  Peso[K]: ").strip().replace(",", ".")
  weightValidar = validarWeight(weight)
  while not weightValidar:
    print("Error: solo es valido hasta tres digitos o hasta tres digitos y dos decimales")
    weight = input("|  Peso[K]: ").strip().replace(",", ".")
    weightValidar = validarWeight(weight)


  height = input("|  Altura[M]: ").strip().replace(",", ".")
  heightValidar = validarheight(height)
  while not heightValidar:
    print("Error: Solo es valido un digito o un digito y hasta 3 decimales")
    height = input("|  Altura[M]: ").strip().replace(",", ".")
    heightValidar = validarheight(height)

  dateNow = datetime.now()

  PruebaUno = Person(name, bday, isAthlete, gender, str(dateNow.date()), weight, height)
  PruebaUno.showInfo()

  # PruebaDos = Person("Daniel", "24/12/1999", "N", "M", "22/08/2021", "50", "2")
  # PruebaDos.showInfo()
