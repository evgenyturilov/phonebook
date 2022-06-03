# Управляющий модуль

import log_module as lm
import interface_module as im

def activation():
  inv = im.invitation()
  if inv == '1':
    data = im.user_data()
    lm.logger(data)
    return activation()
  elif inv == '2':
    lm.rd_txt()
    return activation()
  elif inv == '3':
    exit('Конец работы')
  else:
    print('Введена неверная команда!\n ')
    return activation()
  