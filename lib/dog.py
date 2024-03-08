#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name , str) or not (1 <= len(name) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = name 

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed 

# Example usage
my_dog = Dog("Buddy", "Pug")
print(my_dog.name)  
print(my_dog.breed)  


