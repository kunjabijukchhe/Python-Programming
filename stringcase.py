class stringCase:
    def __init__(self):
        self.enter=""
    def getString(self):
        self.enter=input("Enter a string:")
    def setString(self):
        # return self.enter.upper()
        print(self.enter.upper())


a=stringCase()
a.getString()
# print(a.setString())
a.setString()