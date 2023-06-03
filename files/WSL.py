import subprocess
from colorama import Fore
import os
from time import sleep
from subprocess import Popen
def clear(): return os.system('cls')


def enableWSL():
    sleep(1)
    clear()

    print(f"Tring to enable WSL...\n")
    sleep(0.5)

    process = Popen(
        ["powershell.exe", "files/ps/EnableWSL.ps1"], stdout=subprocess.PIPE)
    result = process.communicate()[0]
    decoded_result = result.decode()

    last_line = decoded_result.splitlines()[-1]

    if "Enabled" in last_line:
        print(
            f"\n{Fore.GREEN}{last_line}{Fore.RESET}")

    elif "Not" in last_line:
        print(
            f"\n{Fore.RED}ERROR:{Fore.RESET}")
        print(
            f"\t{decoded_result}{Fore.RESET}")
    sleep(1)
    print(
        f"\n\n\t{Fore.CYAN}Going back to main menu....{Fore.RESET}")
    sleep(2)
