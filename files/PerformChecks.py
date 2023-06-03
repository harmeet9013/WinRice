from colorama import Fore
import subprocess
from time import sleep
import sys

# Creating a clear function
import os
def clear(): return os.system('cls')


def perform_checks():
    clear()
    functions = {
        1: {
            "function": "oscheck",
            "label": "Checking windows version",
            "success": "Windows version is supported!",
            "failed": "Windows version is NOT supported!"
        },
        2: {
            "function": "isadmin",
            "label": "Checking session elevation",
            "success": "Session is elevated!",
            "failed": "Session is NOT elevated!"
        },
        3: {
            "function": "isonline",
            "label": "Checking internet access",
            "success": "Device is connected to the Internet!",
            "failed": "Device is NOT connected to the Internet!"
        },
        4: {
            "function": "isrestartpending",
            "label": "Checking device session",
            "success": "Device session is fresh!",
            "failed": "Device session is NOT fresh!"
        }
    }

    # run powershell
    def run(cmd):
        completed = subprocess.Popen(
            ["powershell.exe", cmd], stdout=subprocess.PIPE)

        # prints the ... while ps is executing
        while completed.poll() is None:
            sleep(0.5)
            print('.', end='', flush=True)
        result = completed.communicate()[0]
        return result.decode()

    print("Launching requirements checks...\n")

    for key, item in functions.items():
        print(
            f"\n\t{item['label']}", end='')
        process = run(
            'powershell -command "& {. ./files/ps/performChecks.ps1; ' + item["function"] + ' }"')

        if "False" in process:
            print(
                f"{Fore.RED}\n\t[{key}/4] {item['failed']}{Fore.RESET}")
            print(
                f"{Fore.CYAN}\nExiting the Program now. Have a good day!{Fore.RESET}")
            exit()
        print(
            f"{Fore.GREEN}\n\t[{key}/4] {item['success']}{Fore.RESET}")
        sleep(0.7)

    print(
        f"\nAll checks performed successfully!")
    sleep(0.3)
    print(
        f"{Fore.CYAN}\tOpening Menu...{Fore.RESET}")
    sleep(1)
    return
