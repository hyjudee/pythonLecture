class Animal:
    
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")    

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")


dog = Dog("scoopy")
cat = Cat("garfield")

print(dog.name)
print(cat.name)
dog.eat()
cat.sleep()
dog.speak()
cat.speak()
