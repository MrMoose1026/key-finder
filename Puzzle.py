import bitcoin
from bitcoin import*
import colorama
from colorama import Fore, Back, Style
import random
col=1
for x in range(col+5000):
  b= random.randint(33, 127) 
  print(Fore.RED + chr(b), end = ' '+Style.RESET_ALL) 
print() 
print(Fore.GREEN) 
print("-------------------------------------------------------------")
print("<=================== BITCOIN PUZZLE ======================>") 
print("-------------------------------------------------------------") 
print(Style.RESET_ALL) 
print(Fore.GREEN ) 
print(Fore.RED+'-----------------------------------------------------------------------------------------------'+Style.RESET_ALL) 
print(Fore.GREEN+"number-64"+Fore.CYAN+Style.BRIGHT+"'16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN'"+Style.RESET_ALL+Fore.GREEN+" total received [0.64002564] balance [0.64002564]") 
print("keyspace for number-64 start->"+Fore.CYAN+Style.BRIGHT+"[9223372036854775808]"+Style.RESET_ALL+Fore.GREEN+" stop->"+Fore.CYAN+Style.BRIGHT+"[18446744073709551615]"+Style.RESET_ALL) 
print(Fore.RED+'-----------------------------------------------------------------------------------------------'+Style.RESET_ALL)
