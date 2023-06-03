from colorama import Fore
import subprocess
import os
from time import sleep
def clear(): return os.system('cls')


def enableVBS():
    commands = {
        # this command is broken for now
        # "Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard\\Scenarios\\HypervisorEnforcedCodeIntegrity' -Name 'Enable' -Type DWord -Value 1",
        "bcdedit.exe /set hypervisorlaunchtype auto"
    }

    def call_command(cmd):
        process = subprocess.Popen(
            ["powershell.exe", cmd], stdout=subprocess.PIPE)
        result = process.communicate()[0]
        return result.decode()

    clear()
    for cmd in commands:
        output = call_command(cmd)
        if any(word in output for word in ["no", "No", "NO"]):
            print(f"{Fore.RED}ERROR:{Fore.RESET}")
            print(f"\n{output}")
            print(
                f"\n\t{Fore.CYAN}Press 'ENTER' to go back to menu...{Fore.RESET}")
            input()
            return
    print("All commands were executed successfully.")
    print(f"\t{Fore.CYAN}Returning back to menu now...{Fore.RESET}")
    sleep(1)
    return
