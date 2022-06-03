# Модуль предоставления и считывания информации от пользователя

def invitation():    # Функция для приглашения пользователя к началу работы
  global inv
  inv = input('Для продолжения работы нажмите Y/N (Д/Н): ')
  inv.lower()
  return inv

def first_name():
  return input('Введите имя абонента: ')
  
def second_name():
  return input('Введите фамилию абонента: ')
  
def tel_number():
  return input('Введите номер абонента: ')

def comments():
  return input('Добавьте информацию: ')

def request():    # Функция для передачу пользователю запроса на продолжение работы
  req = input('\nХотите внести следующую запись? Y/N (Д/Н) ')
  req.lower()
  return req
  