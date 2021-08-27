from datetime import datetime
import re

def validarNombre(name):
  # Acepta solo letras, espacios y tildes
  regex = re.compile(r"^[a-zA-Z\u00C0-\u017F\s]+$", re.U)
  return regex.match(name) is not None


def validarIsAthlete(Athlete):
  # Acepta solo si y no
  regex = re.compile(r'^(?:SI|NO)$', re.U)
  return regex.match(Athlete) is not None

def validarGender(gender):

  # Acepta solo M y F
  regex = re.compile(r'^(?:M|F)$', re.U)
  return regex.match(gender) is not None


def validarheight(num):
  # Acepta solo numeros 1 | 1.1 | 1.12 | 1.123
  regex = re.compile(r'^(\d{1})([.]\d{1,3})?$', re.U)
  return regex.match(num) is not None

def validarWeight(weight):
  # Acepta solo numeros 1 | 12 | 135
  regex = re.compile(r'^(\d{1,3})([.]\d{1,2})?$', re.U)
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





