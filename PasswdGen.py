# Password Generator
#================================
from random import *
#================================
while True:
  Eingabe = input("Wieviele Stellen soll das Passwort haben: ")
  try:
      int_Eingabe = int(Eingabe)
      if int_Eingabe <= 0 or int_Eingabe > 32:
          print('Bitte nur positive Zahlen kleiner 32 eingeben!')
          continue
      break
  except ValueError:
      print("Haha, witzig, das ist keine Zahl!")
  else:
    print("Was auch immer du jetzt wieder eingegeben hast das war keine gülltige Eingabe!")

tmp_passwd = []
i = 0

for i in range(0, int_Eingabe):
  element = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_.:,;#+*!\§$%&/()=?~ßöäüÖÄÜ')
  tmp_passwd.append(element)
  password = "".join(tmp_passwd)  
  i = i + 1  
print(password)
