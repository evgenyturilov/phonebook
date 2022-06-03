import log_module as lm
import interface_module as im

def main_logic():
  inv = im.invitation()
  if inv == '1':
    data = im.user_data()
    lm.logger(data)
    return main_logic()
  elif inv == '2':
    lm.rd_txt()
    return main_logic()
  elif inv == '3':
    exit('Конец работы')
  else:
    print('Введена неверная команда!\n ')
    return main_logic()
    
def activation():
  im.title()
  main_logic()
  