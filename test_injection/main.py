from importlib import import_module


# do: 
# [python3 main.py]
# Input file to execute: [testexe.py]
# This will execute a user inputted class called runner with 
# def printExecuted(self) and def resetCount(self)


def main():
    fname = ""
    fname = input("Input file to execute: ")
    
    try:
        fname = fname.split('.')[0] 
        pkg = import_module(fname)
    except:
        print("error loading file. Exiting...")
        exit() 
    

    rtest = pkg.runner() 
    rtest.printExecuted() # Executed 1 time(s)
    rtest.printExecuted() # Executed 2 time(s)
    rtest.resetCount()    # Counter reset to 0
    rtest.printExecuted() # Executed 1 time(s)
    rtest.printExecuted() # Executed 2 time(s) 

main() 
