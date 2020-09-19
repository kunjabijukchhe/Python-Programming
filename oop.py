class Dog:
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def output(self):
        return f"{self.name} is {self.age} years old."


a=Dog("Buddy",9)


print(a.name)
print(a.age)
print(a.species)
print(a.output())