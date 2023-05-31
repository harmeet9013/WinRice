from colorama import Fore
import subprocess
from time import sleep
import os
def clear(): return os.system('cls')


def winstall_main():

    def winget_install(app_name):
        process = subprocess.Popen(
            ["powershell.exe", f"winget install {app_name} -s winget -h --accept-package-agreements --disable-interactivity"], stdout=subprocess.PIPE)
        result = process.communicate()[0]
        decoded_result = result.decode()

        last_line = decoded_result.splitlines()[-1]

        if "upgrade" in last_line:
            return True
        elif any(word in last_line for word in ["No", "not"]):
            print(
                f"\n{Fore.RED}ERROR:{Fore.RESET}")
            print(
                f"\t{decoded_result.splitlines()[-1]}")
            return False
        return True

    def textFileMethod():
        try:
            file = open("Winstall.txt", "x")
        except:
            print(
                f"Found {Fore.GREEN}Winstall.txt!{Fore.RESET}")
            sleep(1)
        else:
            print(
                f"{Fore.RED}Winstall.txt was not found.{Fore.RESET}")
            print(
                f"Creating the file and opening Notepad in a second.")
            sleep(1)
            clear()
            # Here starts the real fun

            print(
                f"Notepad has been launched.")
            print(
                f"{Fore.RED}(If it did not, then create Winstall.txt yourself at root directory){Fore.RESET}")
            print(
                f"Inside the text file make sure to input all of the programs in the next line")
            print(
                f"\n{Fore.GREEN}For example:")
            print(
                f"{Fore.YELLOW}Steam\nDiscord\nSpotify\nAnd so on...")
            print(
                f"\n{Fore.RED}Once you are dome creating/editing the file, Save it (overwrite if necessary).")
            print(
                f"{Fore.GREEN}Close Notepad (MAKE SURE YOUR FILE IS SAVED!){Fore.RESET}")
            subprocess.call("notepad.exe Winstall.txt")

            print(
                f"\t\n{Fore.CYAN}Press any key to start installing apps.{Fore.RESET}")
            input()

        clear()
        file = open("Winstall.txt", "r")
        for name in file:
            print(
                f"{Fore.RESET}Trying to install '{Fore.CYAN}{name.strip()}{Fore.RESET}'")
            catchOutput = winget_install(name.strip())
            # if there is any error break the loop
            if catchOutput == False:
                return False
            print(
                f"{Fore.GREEN}Installed '{name}'!{Fore.RESET}\n")
        return True

    def consoleMethod():
        clear()

        print(
            f"In order to make Console method work you need to carefully follow the steps.")
        print(
            f"\n{Fore.GREEN}Please enter the softwares name line by line.{Fore.RESET}")
        print("That means you need to hit enter every time you write a software name.")
        print(f"\n{Fore.CYAN}Press 'ENTER' to start.{Fore.RESET}")
        input()

        # actual input starts here
        clear()
        app_names = []
        while True:
            item = input(
                f"{Fore.RESET}Enter the {len(app_names) + 1} software name :: {Fore.GREEN}")
            if item == '':
                print(f"{Fore.RED}Please enter a name!\n{Fore.RESET}")
            elif item == 'done' or item == 'Done' or item == 'DONE':
                break
            else:
                app_names.append(item)

        clear()
        for name in app_names:
            print(
                f"{Fore.RESET}Trying to install '{Fore.CYAN}{name}{Fore.RESET}'")
            catchOutput = winget_install(name)
            # if there is any error break the loop
            if catchOutput == False:
                return False
            print(
                f"{Fore.GREEN}Installed '{name}'!{Fore.RESET}\n")
        return True

    def choiceSwitch(choice):
        match choice:
            case 1:
                clear()
                if textFileMethod() == True:
                    return True
                return False
            case 2:
                clear()
                if consoleMethod() == True:
                    return True
                return False
            case 3:
                return 'exit'
            case default:
                print(
                    f"\n{Fore.RED}Incorrect choice. Please provide a proper input.{Fore.RESET}")
                input()
                clear()

    while True:
        clear()

        print(
            f"1. Install from Winstall.txt {Fore.GREEN}<<== RECOMMENDED!{Fore.RESET}")
        print(
            f"   ^If the file does not exist, the program will launch a text editor.")
        print(
            f"2. Write program names in console/terminal")
        print(
            f"{Fore.RED}3. Go back to previous menu{Fore.RESET}")
        print(
            f"-------------------------------------------------------------------------")

        output = choiceSwitch(int(input("Enter your choice :: ")))
        if output == True:
            print(
                f"\n\n{Fore.GREEN}Winget successfully installed applications.")
            print(
                f"\t{Fore.CYAN}Press 'ENTER' to continue...{Fore.RESET}")
            input()
            return True
        elif output == False:
            print(
                f"\n\n>> {Fore.RED}The Script has failed installing some/all programs.")
            print(
                f"\t{Fore.CYAN}Press 'ENTER' to continue...{Fore.RESET}")
            input()
        elif output == 'exit':
            print(
                f"\nGoing back to previous menu...")
            sleep(1)
            return False
