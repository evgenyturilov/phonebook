# Модуль обработки полученных от пользователя данных

import interface_module as im
import log_module as lm

def data_collector():
  fn = im.first_name()
  sn = im.second_name()
  tn = im.tel_number()
  com = im.comments()
  lm.log_txt(fn, sn, tn, com)
  lm.log_csv(fn, sn, tn, com)
  
def main_logic():
  inv = im.invitation()
  if inv == '1':
    data_collector()
    return main_logic()
  elif inv == '2':
    lm.rd_txt()
    return main_logic()
  elif inv == '3':
    exit('Конец работы')
  else:
    print('Введена неверная команда!\n ')
    return main_logic()