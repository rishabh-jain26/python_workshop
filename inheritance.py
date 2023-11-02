class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        return "woof!"
class cat(animal):
    def speak(self):
        return "meow!"
dog1=dog("nikhil")
cat1=cat("prashant")
print(dog1.name, dog1.speak())
print(cat1.name, cat1.speak())
