from Node import Node
from Car import Car
from ElectricCar import ElectricCar
from GasolineCar import GasolineCar

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        


    def add(self,obj): 
        newNode = Node(obj)
        if self.size ==0:
            self.tail = newNode
            self.head = newNode
        else:
           self.tail.setNext(newNode)
           newNode.setPrevious(self.tail)
           self.tail = newNode

        self.size = self.size +1


    def insert(self,idx,obj):           
        newNode = Node(obj)
        if idx <0:
            return
        elif idx >= self.size: #add at the tail of the list
            self.tail.setNext(newNode)
            newNode.setPrevious(self.tail)
            self.tail = newNode

    
        elif self.size == 0: #empty list
            self.head = newNode
            self.tail = newNode

        elif idx ==0:   #at head
            self.head.setPrevious(newNode)
            newNode.setNext(self.head)
            self.head = newNode 
  
        else: # in middle
            atIndex = self.head 
            count =0

            while(count < idx):  
                atIndex = atIndex.getNext()
                count = count +1

            beforeIndex = atIndex.getPrevious()
            atIndex.setPrevious(newNode)
            newNode.setNext(atIndex)
            newNode.setPrevious(beforeIndex)
            beforeIndex.setNext(newNode)
           
        self.size = self.size +1

    
    def length(self):
        return(self.size)
    

    def __getitem__(self,idx):
        if self.head is None or idx>=self.size or idx<0:
            return
        
        elif idx == 0:
            return (self.head.getData())
        
        elif idx == self.size -1:
            return (self.tail.getData())
        
        else:

            current = self.head 
            count =0
            while(count<idx):
                current = current.getNext()
                count = count +1

            return(current.getData())
        

    def delete(self,idx): 
        if idx >= self.size  or idx <0 or self.head is None:
            return
        
        elif self.size == 1 and idx ==0: #At head when length is 1 
            self.head = None
            self.tail = None

        elif idx ==0: #Head
         newHead = self.head.getNext()
         newHead.setPrevious(None)
         self.head = newHead

        elif idx == self.size -1: #Tail
            newTail = self.tail.getPrevious()
            newTail.setNext(None)
            self.tail = newTail

        else: #Middle
            current = self.head
            count =0

            while(count<idx-1):
                current = current.getNext()
                count = count +1

            oneBeforeIndex = current
            oneAfterIndex = oneBeforeIndex.getNext().getNext()

            oneBeforeIndex.setNext(oneAfterIndex)
            oneAfterIndex.setPrevious(oneBeforeIndex)

        self.size = self.size-1


    def __str__(self):
        stringToReturn = f"Length of list:{str(self.size)}"
        current = self.head
        while(current is not None):
            stringToReturn = stringToReturn + "\n \n" + str(current)
            current = current.getNext()

        return stringToReturn
    

    def maximumValue(self):
        maximum = self.head.getData()

        current = self.head

        while(current is not None):
            if current.getData() >maximum:
                maximum = current.getData()

            current = current.getNext()
        
        return maximum
    
    def __eq__(self,o):         # Used for Unittest
        
        if self.length() != o.length():
            return False
        elif self.head is None and o.head is None:
            return True

        else:
            current = self.head
            count =0
            while(current is not None):
                if self.__getitem__(count) != o.__getitem__(count):
                    return False
                
                count = count +1
                current = current.getNext()
        return True





if __name__ == "__main__":
    list = LinkedList()
    list.add(5)
    temp =list.head
    
    print(temp ==list.head)

    
  
    

   


    

   



    
    
