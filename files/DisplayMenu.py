from colorama import Fore
# from Automation import automation
from time import sleep
import os
def clear(): return os.system('cls')


def display_menu(menu):
    def printItems():

        print(
            f"\t                  ( )       __        __       ( )      ___        ___    ")
        print(
            f"\t  //  / /  / /   / /     //   ) )   //  ) )   / /     //   ) )   //___) ) ")
        print(
            f"\t //  / /  / /   / /     //   / /   //        / /     //         //        ")
        print(
            f"\t((__( (__/ /   / /     //   / /   //        / /     ((____     ((____     ")
        print(
            f"\n----------------------------------------------------------------------------------")
        for key, item in menu.items():
            print(f'{item["color"]}{key}. {item["label"]}' + Fore.RESET)
            sleep(0.03)
        print("----------------------------------------------------------------------------------")

    def choiceAction(key):
        if key in menu:
            action = menu[key].get('action')
            sleep(0.1)
            action()
        else:
            print(
                f"{Fore.RED}\nIncorrect choice.{Fore.RESET}")
            sleep(0.5)
            clear()

    while True:
        clear()
        printItems()
        choice = input("Enter your choice :: ")
        choiceAction(choice)

    return
