import interface_module as im
import modules as m



def activation():
  inv = im.invitation()
  if inv == 'y':
    m.module1()
    m.module2()
  elif inv == 'n':
    exit('До новых встреч!')
  else:
    print('Введена неверная команда!\n ')
    activation()
  