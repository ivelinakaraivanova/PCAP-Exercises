class Vehicle():
   pass
        
class Rideable():
   pass
      
class PetrolVehicle(Vehicle):
   pass
        
class Car(PetrolVehicle, Rideable):
   pass


# bases for Vehicle and Rideable
print(Vehicle.__bases__)
print(Rideable.__bases__)
print(PetrolVehicle.__bases__)
print(Car.__bases__)