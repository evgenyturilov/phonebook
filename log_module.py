# Модуль предназначенный для записи данных в текстовый файл

def log(a, b, c, d):
  with open('phonebook.txt', 'a') as file:
    file.write('имя. {} {}, тел. {}, кат. {}\n'.format(a, b, c, d))