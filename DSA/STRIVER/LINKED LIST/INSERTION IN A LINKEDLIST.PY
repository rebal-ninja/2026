# # INSERTING A NODE AT THE START 


# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedlist:
#     def __init__(self):
#         self.head = None 
#         # this means the first node that is created will be at the end 
#         # the node at the end is always null 

#     def at_start(self,data):
#         new_node = node(data)
#         # creating a new node 
#         new_node.next= self.head
#         # linking the adress of the new_node and the previous node 
#         self.head = new_node
#         # here we update the value that is passed to the current node 
#         # which also means its the first element at this moment

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="-->")
#             temp = temp.next
#         print(None)
    



# li = linkedlist()
# n = int(input("enter the no of node you want to enter"))
# for i in range (n):
#     value = int(input("enter the value "))
#     li.at_start(value)
# li.display()



# INSERTING A NODE AT THE END

class node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        # considering head of a node is none

    def at_end(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
    
        temp = self.head
        while temp.next :
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print(None)

li = linkedlist()
n = int(input("enter the number of nodes"))
for i in range (n):
    value = int(input("enter a value"))
    li.at_end(value)
li.display()

        

        