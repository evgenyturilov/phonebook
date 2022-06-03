# Модуль предназначенный для импорта и экспорта данных в/из файла

def log_txt(a, b, c, d):
  with open('phonebook.txt', 'a') as file:
    file.write('имя. {} {}, тел. {}, кат. {}\n'.format(a, b, c, d))

def log_csv(a, b, c, d):
  with open('phonebook.csv', 'a') as file:
    file.write(f'{a} {b} {c} {d}\n')

def rd_txt():
  with open('phonebook.txt', 'r') as file:
    print(f'\n{file.read()}')