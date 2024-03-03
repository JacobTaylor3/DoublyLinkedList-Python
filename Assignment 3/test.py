
from LinkedList import LinkedList 

l = LinkedList()

l2 = LinkedList()

l.add(3)

l.add(5)

l2.add(10)

l2.add(50)

def merge(list:LinkedList, list2:LinkedList):
    newLinkedList = LinkedList()
    current = list.head

    while(current is not None):
        newLinkedList.add(current)

        current = current.getNext()

    current2 = list2.head

    while(current2 is not None):
        newLinkedList.add(current2)

        current2 = current2.getNext()

    return (newLinkedList)



merge(l,l2)

newList = merge(l,l2)

print(newList)
# print(l2)



