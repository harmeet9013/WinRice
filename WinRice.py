# import statements here
# DEPENDENCIES CURRENTLY BEING USED!!!
# COLORAMA

# Script requires >Python3.

from files.ExitProgram import exit_program
from files.Automation import automation
from files.checkYes import checkYes
from files.DisplayMenu import display_menu
from files.PerformChecks import perform_checks
from files.DisplayName import display_name
from files.Winstall import winstall_main
from colorama import Fore
from time import sleep
import os
def clear(): return os.system('cls')


# from time import sleep


def main():

    broken = "Haha this is broken right now pffttttt"
    print(Fore.RESET)
    tasks = {
        '1': {
            'label': 'Winget Install',
            'action': lambda: winstall_main(),
            'color': Fore.WHITE
        },
        '2': {
            'label': 'Disable VBS (NOT WORKING)',
            'action': lambda: print(broken),
            'color': Fore.WHITE
        },
        '3': {
            'label': 'Uninstall Edge (NOT WORKING)',
            'action': lambda: print(broken),
            'color': Fore.WHITE
        },
        '4': {
            'label': 'Remove Brain perhaps? (NOT WORKING)',
            'action': lambda: print(broken),
            'color': Fore.WHITE
        },
        '5': {
            'label': 'Exit Program',
            'action': lambda: exit_program(),
            'color': Fore.RED
        },
        '69': {
            'label': 'Run the entire script and perform all of the tasks.',
            'action': lambda: print(broken),
            'color': Fore.GREEN
        },
    }

    # Print the GIGANTIC Winrice Logo
    display_name()

    # Perform Checks before moving ahead
    # perform_checks()

    # Asking user how to proce
    display_menu(tasks)


main()
