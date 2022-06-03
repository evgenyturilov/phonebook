# Модуль предназначенный для работы с файлами

def rd_txt():
  with open('phonebook.txt', 'r') as file:
    print(f'\n{file.read()}')
    
def logger(data):
  count = sum(1 for line in open('phonebook.txt', 'r')) + 1
  with open('phonebook.txt', 'a') as file:
    file.write(f'{count}. Имя: {data[0]} {data[1]}, тел. {data[2]}, прим. {data[3]}\n')
  with open('phonebook.csv', 'a') as file:
    for i in data:
      file.write(i)
    file.write('\n')
      