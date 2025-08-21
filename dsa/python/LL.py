class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist :
    def __init__(self):
        self.head = None

    def createNode(self, val):
        newNode = Node(val)
        if(self.head == None) :
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None) :
                temp = temp.next
            temp.next = newNode
        
    def printList(self):
        curr = self.head
        while(curr != None):
            print(f"{curr.val} -> ", end = '')
            curr = curr.next
        print("Null")
        


list = Linkedlist()
list.createNode(20) 
list.createNode(50)
list.createNode(70)
list.createNode(12)

list.printList()