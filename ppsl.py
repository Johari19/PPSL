# Hello! My name is Joseph Ambayec
# Please visit my website for more info!
# www.josephambayec.dev
# Also see license for public use!
# Setup
import sys
import time

if __name__ == '__main__':
    print("Do not run this program! Visit my site: www.josephambayec.dev")
    time.sleep(10)
else:
    # Pause function
    def pause():
        # This will pause your program until user presses a key
        programPause = input("Press any key to continue...")

    # Choice function
    def choice():
        # This will give user choice to continue process or stop it
        programChoice = input("Would you like this process? Y/N: \n")
        if (programChoice == "Y" or programChoice == "y"):
            # Nothing
            print("Continuing process!")
            time.sleep(3)
        else:
            print("Stopping process")
            time.sleep(3)
            sys.exit()

    
