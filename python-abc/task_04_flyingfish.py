ass Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Testing the implementation
flying_fish = FlyingFish()

flying_fish.fly()     # Expected: "The flying fish is soaring!"
flying_fish.swim()    # Expected: "The flying fish is swimming!"
flying_fish.habitat() # Expected: "The flying fish lives both in water and the sky!"

# Investigate the method resolution order
print(FlyingFish.mro())  # or print(FlyingFish.__mro__)
