class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

x = Node(10)                    #it will print data element of x node but will not print the adress field 
y = Node(20)
print(x)
print(y)

x.next = y
print(x.next)
print(y.data)
print(y.next)
print(x.data)
print(x.next.data)          #it is pointing to the data of next node
#print(y.next.data)          #it is pointing to the data of next node y.next is none here..so it will give error
x.data = 50
print(x.data)
