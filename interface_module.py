# Модуль предоставления и считывания информации от пользователя

def title():
  print('ТЕЛЕФОННЫЙ СПРАВОЧНИК v.1.0')

def invitation():
  return input('\nВыберете действие:\n\n  Сделать новую запись   - 1\n  Отобразить контакты    - 2\n  Выйти из приложения    - 3\n\n')

def user_data():
  data = [
    input('\n  Введите имя абонента: '),
    input('  Введите фамилию абонента: '),
    input('  Введите номер абонента: '),
    input('  Добавьте информацию: ')
          ]
  return data

  