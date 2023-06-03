from time import sleep
from colorama import Fore
from files.checkYes import checkYes
from pathlib import Path
import os
def clear(): return os.system('cls')


def exit_program():
    while True:
        clear()
        userInput = input(
            f"{Fore.RED}Are you sure you want to exit the program? y/n :: {Fore.RESET}")
        result = checkYes(userInput)
        if result == True:
            print(
                f"\n\nRemoving Winstall.txt if it exists.")
            sleep(0.5)
            try:
                file_path = Path("Winstall.txt")
                file_path.unlink()

                print(
                    f"{Fore.GREEN}Winstall.txt has been deleted!{Fore.RESET}")
            except:

                print(
                    f"{Fore.GREEN}Winstall.txt was not found!{Fore.RESET}")
            sleep(0.5)

            print(
                f"\n\tExiting the program now. Have a good day!\n")
            exit()
        elif result == False:
            print("\n\nNot exiting the program. Going back to menu")
            sleep(1)
            clear()
            return
        else:
            print("\nNot a proper input.")
            sleep(0.5)
