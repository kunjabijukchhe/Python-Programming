class vehicles:
    def __init__(self,color,kind,prices,name):
        self.color=color
        self.prices=prices
        self.name=name
        self.kind=kind

         
car1=vehicles("red",50000.00,"Fer","Convertible")
car2=vehicles("blue",10000.00,"Fer","Van")

print(car1.name)
print(car1.color)
print(car1.kind)
print(car1.prices)
print(car2.name)
print(car2.color)
print(car2.kind)
print(car2.prices)
    

