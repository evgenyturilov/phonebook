def log(data):
  with open('phonebook.txt', 'a') as file:
    file.write(data)