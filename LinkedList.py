#LinkedList

#Element class represent a single node in the LinkedList
class Elements(object):
    
    #Here the value is used to store the node's value and next is the reference to next node.
    def __init__(self,value):
        self.value=value
        self.next=None

#LinkedList class represent the LinkedList itself.
class LinkedList(object):
    
    #Here the constructor initializes the LinkedList with head node, if not provided then NONE.
    def __init__(self,head=None):
        self.head=head

    #Here the append method adds the element to end of list.
    #Keeps going until the last node is found and then assign the next attribute of the last node to the new element.
    def append(self,new_element):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_element
        else:
            self.head=new_element

    #The get_position method takes a position, returns the element of that position.
    #Starts from head node, till the LinkedList until the desired position is reached. Returns NONE if position is not founded.
    def get_position(self,position):
        current=self.head
        pos=1
        if self.head:
            while pos!=position:
                if current.next==None:
                    return None
                pos+=1
                current=current.next
            return current
        else:
            return "Empty List"
        
    #The insert method takes a new element and position. Inserts a new element at specific position by updating the next attribute.
    #Keeps going in the LinkedList until the position is founded and element is adjusted.
    def insert(self,new_element,position):
        counter=1
        current=self.head
        if position>1:
            while counter<position-1:
                current=current.next
                counter+=1
                if current==None:
                    return "Position is not in the list."
                new_element.next=current.next
                current.next=new_element
        elif position==1:
            new_element.next=self.head
            self.head=new_element
            
    #The delete method takes the value and delete the first occurrence of the node with the value.
    #When founded, it updates the next attribute of previous node to skip the current node.
    def delete(self,value):
        current=self.head
        previous=None
        while current and current.value!=value:
            previous=current
            current=current.next
        if current:
            if previous:
                previous.next=current.next
            else:
                self.head=current.next
        
#Object for Elements Class                
E1=Elements(11)
E2=Elements(22)
E3=Elements(33)
E4=Elements(44)
E5=Elements(55)

#Object for LinkedList Class
E=LinkedList(E1)

#Appending the Elements class object in LinkedList
E.append(E2)
E.append(E4)
E.append(E5)

#Calling the get_position method
print(E.head.next.next.value)
print(E.get_position(2).value)

#Calling the insert method
E.insert(E3,3)
print(E.get_position(3).value)

#Calling the delete method
E.delete(2)
print(E.get_position(2).value)
print(E.get_position(3).value)
