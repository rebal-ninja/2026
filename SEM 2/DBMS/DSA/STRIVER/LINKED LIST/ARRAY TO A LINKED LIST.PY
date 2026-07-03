class node:
    def __init__(self,data):
        self.data = data      # value stored in node
        self.next = None      # pointer to next node


arr = [2,4,5,7]

# STEP 1 — create first node (HEAD)
head = node(arr[0])          # node(2)
current = head               # current points to head


# STEP 2 — build the rest of the list
for i in range(1,len(arr)):

    new_node = node(arr[i])  # create new node

    current.next = new_node  # connect previous node → new node

    current = new_node       # move current forward


# STEP 3 — traverse and print
temp = head

while temp is not None:
    print(temp.data,end="-->")
    temp = temp.next

print("None")
