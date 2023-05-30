# import statements here
#DEPENDENCIES CURRENTLY BEING USED!!!
#COLORAMA


from files.Winstall import winstall_main
from files.DisplayName import display_name
from files.PerformChecks import perform_checks
from files.DisplayMenu import display_menu
from files.Automation import automation

# from time import sleep

def main() :
    
    broken = "Haha this is broken right now pffttttt"
    
    tasks = {
        '1' : {
            'label' : 'Winget Install',
            'callFun' : lambda: winstall_main()
        },
        '2' : {
            'label' : 'Disable VBS',
            'callFun' : lambda: print(broken)
        },
        '3' : {
            'label' : 'Uninstall Edge',
            'callFun' : lambda: print(broken)
        },
        '4' : {
            'label' : 'Remove Brain perhaps?',
            'callFun' : lambda: print(broken)
        },
    }
    
    #Print the GIGANTIC Winrice Logo
    display_name()
        
    #Perform Checks before moving ahead
    perform_checks()
    
    #Asking user how to proce
    display_menu(tasks)
    

main()

