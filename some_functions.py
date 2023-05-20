# id generate
def idgenerate():
    import random as r
    id = '88'
    for i in range(6):
        id += str(r.randint(1,10))
    return id
from colorama import Fore, Style
import time
def Purchase_complete():
    dots = 0
    while dots < 4:
        print(Fore.GREEN + "\rPlease Wait" + "." * dots, end="")
        time.sleep(0.3)
        print("\r" + " " * (dots + 1), end="")
        dots += 1
    print("\r" + Fore.LIGHTGREEN_EX + "Purchase Complete!" + Style.RESET_ALL)
def loading_dots():
    dots = 0
    while dots < 4:
        print(Fore.GREEN + "\rLoading" + "." * dots, end="")
        time.sleep(0.3)
        print("\r" + " " * (dots + 1), end="")
        dots += 1

    print("\r" + Fore.LIGHTGREEN_EX + "Loading complete!" + Style.RESET_ALL)
