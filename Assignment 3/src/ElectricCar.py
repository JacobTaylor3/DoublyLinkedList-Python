import Car

class ElectricCar(Car.Car):

    def __init__(self,makeAndModel="none assigned", numberOfDoors=4, maximumNumberOfPassengers=5, batterySize = -1):
      super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)

      self.batterySize = batterySize


    def setBatterySize(self,s):
      self.batterySize = s
    
    def getBatterySize(self):
       return (self.batterySize)
    

    def __str__(self):
      stringToReturn = f"Electric Car\n{super().__str__()}\nBattery Size:{self.batterySize}"
      return stringToReturn
    
    def __eq__(self,other):
       return(super().__eq__(other) and self.getBatterySize() == other.getBatterySize())
    

if __name__ =="__main__":
   car1 = ElectricCar("BMW",15,32,2)
   car2 = ElectricCar("BMW",15,32,2)
   print(car1 == car2)

   x= Car.Car()
   print(x.getMakeAndModel())

   
  




