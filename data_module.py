# Модуль обработки полученных от пользователя данных

import interface_module as im
import log_module as lm

def module1():    # Функция, инициируемая при первичном вводе данных от пользователя
  inv = im.invitation()
  if inv == 'y' or inv == 'д':
    fn = im.first_name()
    sn = im.second_name()
    tn = im.tel_number()
    com = im.comments()
    lm.log_txt(fn, sn, tn, com)
    lm.log_csv(fn, sn, tn, com)
  elif inv == 'n' or inv == 'н':
    exit('Гудбай!')
  else:
    print('Введена неверная команда!\n ')
    return module1()

def module2():    # Функция, инициируемая при повторных вводах данных от пользователя
  req = im.request()
  if req == 'y' or req == 'д':
    fn = im.first_name()
    sn = im.second_name()
    tn = im.tel_number()
    com = im.comments()
    lm.log_txt(fn, sn, tn, com)
    lm.log_csv(fn, sn, tn, com)
    return module2()
  elif req == 'n' or req == 'н':
    exit('Пока!')
  else:
    print('Введена неверная команда!\n ')
    return module2()