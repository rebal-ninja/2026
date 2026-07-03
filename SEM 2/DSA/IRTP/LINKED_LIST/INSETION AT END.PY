class node:
    def __init__(self,data):
        self.data= data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def at_end(self,data):
        new_node  = node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next :
            temp = temp.next
            temp.next = new_node
        
    def diplay(self):
        temp = self.head 
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
        
     
li = linkedlist()
n= int(input("enter the no of nodes"))
for i in range(n):
    value = int(input("enter value"))
    li.at_end(value)
li.diplay()