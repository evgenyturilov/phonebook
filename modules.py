# Модуль обработки полученных от пользователя данных

import interface_module as im
import log_module as lm

def module1():    # Функция, инициируемая при первичном вводе данных от пользователя
  fn = im.first_name()
  sn = im.second_name()
  tn = im.tel_number()
  com = im.comments()
  lm.log(fn, sn, tn, com)
  return(fn, sn, tn, com)

def module2():    # Функция, инициируемая при повторных вводах данных от пользователя
  req = im.request()
  if req == 'y':
    fn = im.first_name()
    sn = im.second_name()
    tn = im.tel_number()
    com = im.comments()
    lm.log(fn, sn, tn, com)
    return module2()
  elif req == 'n':
    exit('Пока!')
  else:
    print('Введена неверная команда!\n ')
    return module2()