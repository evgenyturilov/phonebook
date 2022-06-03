# Модуль предназначенный для работы с файлами

def rd_txt():
  with open('phonebook.txt', 'r') as file:
    print(f'\n{file.read()}')
    
def logger(data):
  count = sum(1 for line in open('phonebook.txt', 'r'))
  with open('phonebook.txt', 'a', encoding='utf8') as file:
    file.write(f'{count + 1}. Имя: {data[0]} {data[1]}, тел. {data[2]}, прим. {data[3]}\n')
  with open('phonebook.csv', 'a', encoding='utf8') as file:
    file.write(f'{count + 1};')
    for i in data:
      file.write('{};'.format(i))
    file.write('\n')
      