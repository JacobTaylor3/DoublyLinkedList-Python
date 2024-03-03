from Car import Car

class GasolineCar(Car):


    def __init__(self,makeAndModel="none assigned", numberOfDoors=4,maximumNumberOfPassengers=5, gasTankSize = -1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)

        self.gasTankSize = gasTankSize


    def setGasTankSize(self,s):
        self.gasTankSize = s


    def getGasTankSize(self):
        return(self.gasTankSize)       


    def __str__(self): 
        stringToReturn = f"Gasoline Car\n{super().__str__()}\nGas tank size:{self.gasTankSize}"
        return stringToReturn
    

    def __eq__(self,other):
       return(super().__eq__(other) and self.getGasTankSize() == other.getGasTankSize())



if __name__ =="__main__":
    car1 = GasolineCar("Mercedes", 50,600,4)
    car2 = GasolineCar("Mercedes",50,600,4)