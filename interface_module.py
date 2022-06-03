# Модуль предоставления и считывания информации от пользователя

def title():
  print('ТЕЛЕФОННЫЙ СПРАВОЧНИК v.1.0')

def invitation():
  return input('\nВыберете действие:\n\n  Сделать новую запись   - 1\n  Отобразить контакты    - 2\n  Выйти из приложения    - 3\n\n')

def first_name():
  return input('\n  Введите имя абонента: ')
  
def second_name():
  return input('  Введите фамилию абонента: ')
  
def tel_number():
  return input('  Введите номер абонента: ')

def comments():
  return input('  Добавьте информацию: ')

  