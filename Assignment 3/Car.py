


class Car:

    def __init__(self,makeAndModel="none assigned",numberOfDoors = 4, maximumNumberOfPassengers = 5):
        self.makeAndModel = makeAndModel
        self.numberOfDoors = numberOfDoors
        self.maximumNumberOfPassengers = maximumNumberOfPassengers


    def setMakeAndModel(self,s):
        self.makeAndModel = s


    def getMakeAndModel(self): 
        return (self.makeAndModel)
    
    def getMaximumNumberOfPasengers(self):
        return (self.maximumNumberOfPassengers)
    
    def getNumberOfDoors(self):
        return (self.numberOfDoors)
    
    def __str__(self):
        stringToReturn = f"Make and Model:{self.makeAndModel}\nNumber of doors:{self.numberOfDoors}\nMaximum amount of passengers:{self.maximumNumberOfPassengers}"
        return stringToReturn
    
    def __eq__ (self,other):
        return(self.getMakeAndModel() == other.getMakeAndModel()and (self.getMaximumNumberOfPasengers() == other.getMaximumNumberOfPasengers() and self.getNumberOfDoors() == other.getNumberOfDoors()))
    
    



  