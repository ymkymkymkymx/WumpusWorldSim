class runner:
    def __init__ (self):
        self.counter = 0
    def printExecuted(self):
        self.counter += 1 
        print("Executed {0} time(s)".format(self.counter))
    def resetCount(self):
        self.counter = 0
        print("Counter reset to 0")
