# countE=0
# countP=0
# letterE="E"
# letterP="P"
# fname = input("Enter file name: ")

# with open(fname, 'r') as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             for letter in i:
#                 if(letter==letterE):
#                     countE=countE+1
#                 elif(letter==letterP):
#                     countP=countP+1

# print(countE)
# print(countP)

class textCount:
    def __init__(self,E,P):
        self.E=E
        self.P=P
    def count_E(self):
        letterE="E"
        letterP="P"
        fname = input("Enter file name: ")
        with open(fname, 'r') as f:
            for line in f:
                words = line.split()
                for i in words:
                    for letter in i:
                        if(letter==letterE):
                            countE=countE+1
                        elif(letter==letterP):
                            countP=countP+1

obj=textCount()

print(obj.count_E())