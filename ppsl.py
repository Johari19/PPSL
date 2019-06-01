# Hello! My name is Joseph Ambayec
# Please visit my website for more info!
# www.josephambayec.dev
# Also see license for public use!
import sys
import time
# Pause function
def pause():
    programPause = input("Press any key to continue...")
# This will pause your program until user presses a key
def choice():
    programChoice = input("Would you like this process? Y/N: \n")
    if (programChoice == "Y" or programChoice == "y"):
        # Nothing
        print("Continuing process!")
        time.sleep(3)
    else:
        print("Stopping process")
        time.sleep(3)
        sys.exit()
pause()
choice()
