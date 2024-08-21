# Close the PC

import os


new = input("Do you want to close the PC? (yes/no): ")

if new.lower() == "yes":
    os.system("shutdown /s /t 0")
else:
    another = input("Do you want to restart the PC? (yes/no): ")
    if another.lower() == "yes":
        os.system("shutdown /r /t 0")
    else:
        oneMore = input("Do you want to log off the current user? (yes/no): ")
        if oneMore.lower() == "yes":
            os.system("shutdown /l")
        else:
            print("Goodbye!")


 