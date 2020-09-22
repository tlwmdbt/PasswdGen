# Password Generator
#================================
from random import *
#================================

while True:
  Eingabe = input ('Wieviele Zeichen soll das Passwort habe: ')  
  
  try:
    Eingabe = int(Eingabe)
  except ValueError:
    # Eingabe ist nicht vom Typ Integer
    print('Bitte nur Zahlen eingeben!')
    break
  else:
    # Eingabe ist vom Typ Integer
    
    if Eingabe <= 24:
      tmp_passwd = []
      i = 0
      
      for i in range(0, Eingabe):
        element = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_.:,;#+*!\§$%&/()=?~ßöäüÖÄÜ')
        
        if element not in tmp_passwd:
          tmp_passwd.append(element)
          i = i + 1
      
      password = "".join(tmp_passwd)
      print(password)
    
    else:
      print("Es sind bis zu 24 Zeichen möglich.")
    break
