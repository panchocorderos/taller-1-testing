class Person:
  def __init__(self, name, bday, age, gender, dateWeight):
        self.name = name #name person
        self.bday = bday #birth day date
        self.age = age
        self.isAthlete = None #bool physical condition
        self.gender = gender #gender (man or woman)
        self.dateWeight = dateWeight #date weigh
        self.weight = None # weight in kg
        self.imc = None
        self.height = None #height in mt
        self.interpretation = " "

  def setIMC(self):
    self.imc = (float(self.weight)/(float(self.height)**2))

  def setHeight(self, height):
    self.height = height

  def setIsAthlete(self, isAthlete):
    self.isAthlete = isAthlete

  def setWeight(self, weight):
    self.weight = weight
    
  def setInterpretation(self):
    if (self.gender == "M"):
      if (self.imc < 20):
        self.interpretation = "BAJO PESO"
      elif (self.imc >= 20 and self.imc <= 24.9):
        self.interpretation = "NORMAL"
      elif  (self.imc >= 25 and self.imc <= 29.9):
        self.interpretation = "OBSESIDAD LEVE"

      elif  (self.imc >= 30 and self.imc <= 40):
        self.interpretation = "OBESIDAD SEVERA"
      elif  (self.imc > 40):
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
      elif (self.imc > 37):
        self.interpretation = "OBESIDAD MUY SEVERA"


  def __str__(self):
    return '\n\n'\
      '-------- Info --------\n'\
      '|\n'\
      '|  Nombre: {0}\n'\
      '|  Edad: {1}\n'\
      '|  ¿Hace ejercicio?: {2}\n'\
      '|  Genero: {3}\n'\
      '|  Peso: {4}\n'\
      '|  Altura: {5}\n'\
      '|  IMC: {6}\n'\
      '|  Interpretacion: {7}\n'\
      '|\n'\
      '|  Fecha Registro: {8}\n'\
      '|\n'\
      '----------------------\n'.format(self.name, self.age, self.isAthlete, self.gender, self.weight, self.height, self.imc, self.interpretation, self.dateWeight)
