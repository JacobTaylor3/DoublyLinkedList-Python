import unittest
from LinkedList import LinkedList
from ElectricCar import ElectricCar

class LinkedListTest(unittest.TestCase):
        
#For all of these tests, I implemented an __eq__ method to compare Linked Lists. Which can be found in my LinkedList class. 


#LinkedList.delete() tests:

        #Delete first element
        def testDeleteFirstElement(self):       
            originalList = LinkedList()
            originalList.add(ElectricCar("BMW"))
            originalList.add(ElectricCar("Mercedes"))
            originalList.add(ElectricCar("Tesla"))

            originalList.delete(0)
            
            listAfterDelete = LinkedList()
            listAfterDelete.add(ElectricCar("Mercedes"))
            listAfterDelete.add(ElectricCar("Tesla"))


            self.assert_(originalList.length()==2 and originalList == listAfterDelete)
            

        #Delete middle element
        def testDeleteMiddleElement(self):
            originalList = LinkedList()
            originalList.add(ElectricCar("BMW"))
            originalList.add(ElectricCar("Mercedes"))
            originalList.add(ElectricCar("Tesla"))
            originalList.add(ElectricCar("Toyota"))
            originalList.add(ElectricCar("Audi"))
            
            originalList.delete(2)
            
            listAfterDelete = LinkedList()
            listAfterDelete.add(ElectricCar("BMW"))
            listAfterDelete.add(ElectricCar("Mercedes"))
            listAfterDelete.add(ElectricCar("Toyota"))
            listAfterDelete.add(ElectricCar("Audi"))

            
            self.assert_(originalList.length() == 4 and originalList == listAfterDelete)


        #Delete last element
        def testDeleteLastElement(self):
            originalList = LinkedList()
            originalList.add(ElectricCar("BMW"))
            originalList.add(ElectricCar("Mercedes"))
            originalList.add(ElectricCar("Tesla"))
            originalList.add(ElectricCar("Toyota"))
            originalList.add(ElectricCar("Audi"))
            
            originalList.delete(4)
            
            listAfterDelete = LinkedList()
            listAfterDelete.add(ElectricCar("BMW"))
            listAfterDelete.add(ElectricCar("Mercedes"))
            listAfterDelete.add(ElectricCar("Tesla"))
            listAfterDelete.add(ElectricCar("Toyota"))


            self.assert_(originalList.length() == 4 and originalList == listAfterDelete )

    
       
#LinkedList.insert() tests:
        
       #Insert at the head
        def testInsertAtTheHead(self):
            originalList = LinkedList()
            originalList.add(ElectricCar("BMW"))
            originalList.add(ElectricCar("Mercedes"))
            originalList.add(ElectricCar("Tesla"))
            
            originalList.insert(0,ElectricCar("Honda"))
            
            listAfterInsert = LinkedList()
            listAfterInsert.add(ElectricCar("Honda"))
            listAfterInsert.add(ElectricCar("BMW"))
            listAfterInsert.add(ElectricCar("Mercedes"))
            listAfterInsert.add(ElectricCar("Tesla"))


            self.assert_(originalList.length()==4 and originalList == listAfterInsert)


        #Insert at the tail
        def testInsertAtTheTail(self):
            originalList = LinkedList()
            originalList.add(ElectricCar("BMW"))
            originalList.add(ElectricCar("Mercedes"))
            originalList.add(ElectricCar("Tesla"))
            
            originalList.insert(3,ElectricCar("Honda"))
            
            listAfterInsert = LinkedList()
            listAfterInsert.add(ElectricCar("BMW"))
            listAfterInsert.add(ElectricCar("Mercedes"))
            listAfterInsert.add(ElectricCar("Tesla"))
            listAfterInsert.add(ElectricCar("Honda"))


            self.assert_(originalList.length() == 4 and originalList == listAfterInsert)
       
       
        #Insert in the middle
        def testInsertMiddle(self):
            originalList = LinkedList()
            originalList.add(ElectricCar("BMW"))
            originalList.add(ElectricCar("Mercedes"))
            originalList.add(ElectricCar("Tesla"))
            originalList.add(ElectricCar("Lamborghini"))
            originalList.add(ElectricCar("Mclaren"))

            originalList.insert(2,ElectricCar("Mazda"))
            
            listAfterInsert = LinkedList()
            listAfterInsert.add(ElectricCar("BMW"))
            listAfterInsert.add(ElectricCar("Mercedes"))
            listAfterInsert.add(ElectricCar("Mazda"))
            listAfterInsert.add(ElectricCar("Tesla"))
            listAfterInsert.add(ElectricCar("Lamborghini"))
            listAfterInsert.add(ElectricCar("Mclaren"))


            self.assert_(originalList.length() == 6 and originalList == listAfterInsert)