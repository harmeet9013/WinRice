from colorama import Fore, Style
# from Automation import automation
from time import sleep
import os
clear = lambda: os.system('cls')

def display_menu(menu) :
    def printItems():
        for key, item in menu.items():
            print(f'{key}. {item["label"]}')
            sleep(0.1)
        print(Fore.GREEN + "69. Run the entire script and perform all of the tasks.")
        print(Fore.RED +   "    ^ RECOMMENDED BUT WE ARE NOT RESPONSIBLE.")
        print(Style.RESET_ALL)
        print("------------------------------------")
    
    clear()
    while True:
        printItems()
        choice = int(input("Enter your choice :: "))
        break
    
    return
