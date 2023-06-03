from colorama import Fore
from subprocess import Popen
from time import sleep
import sys

# Creating a clear function
import os
def clear(): return os.system('cls')


def perform_checks():
    sleep(2)
    clear()

    print("Starting the Checking process.\n")

    # calling powershell to open the script, dom't touch
    output = Popen(
        ["powershell.exe", "files/ps/performChecks.ps1"], stdout=sys.stdout)
    output.communicate()

    # don't touch this either
    if output.returncode == 0:
        print(
            f"\n{Fore.GREEN}Checks performed successfully!{Fore.RESET}")
        sleep(0.3)
        print("Opening Menu...")
        sleep(1)
        return
    else:
        print(output.stderr)
        print(
            f"{Fore.RED}\nThe script did not execute successfully.{Fore.RESET}")
        print("\tExiting the Program now. Have a good day!")
        exit()
