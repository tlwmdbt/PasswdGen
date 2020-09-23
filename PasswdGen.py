# Password Generator
#================================
from random import choice, seed, randint
#================================

# User Input aquired via while loop and exception handling
while True:
  # Question
  Eingabe = input("Wieviele Stellen soll das Passwort haben: ")
  try:
      # check first if input is an integer and within the range between 12 and 32
      int_Eingabe = int(Eingabe)
      if int_Eingabe < 12 or int_Eingabe > 32:
          # error message when int but not within range
          print('Alter! Nur Zahlen zwischen 12 und 32! OK?!')
          continue
      break
  except ValueError:
      # error when not an integer
      print("Haha, witzig, das ist keine Zahl!")
  else:
    # catch all for all other cases ¯\_(ツ)_/¯ 
    print("Höma, red ich chinesisch? 你这笨蛋！Eine Zahl zwischen 12 und 32. Los, nochma!")

# Initialize the random generator from OS specific random device
while True:
  try:
    # check if urandom is working
    # 
    from os import urandom
    seed(int.from_bytes(urandom(100), byteorder='big', signed=False))
    print("Benutze /dev/urandom.")
    break
  except ImportError:
    # module not available, so use standard randint
    print("Benutze standard randint().")
    seed(randint(1, 1000))
    break
  else:
    # all other cases, bye ¯\_(ツ)_/¯ 
    print("Kein random möglich.")
    raise SystemExit

# nescessary temporary list and a counter
tmp_passwd = []
i = 0

# while loop to create and choose from a alpha numeric and special character set
for i in range(0, int_Eingabe):
  # setup the set of characters to choose from randomly
  element = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_.:,;#+*!§$%&/()=?~ßöäüÖÄÜ')
  # append it to the temporary list tmp_passwd
  tmp_passwd.append(element)
  # count +1
  i = i + 1 

# construct the password from the list entries and print it to the screen
password = "".join(tmp_passwd)  
print("\n", password, "\n")
raise SystemExit
