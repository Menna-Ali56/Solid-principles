# This code does not violate the Liskov Substitution Principle (LSP).
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")
        

class Cat(Animal):
    def make_sound(self):
        print("Meow")
        
def play_with_animal(animal):
    animal.make_sound()
 

dog=Dog()
cat=Cat()
play_with_animal(dog)
play_with_animal(cat)        




    
        