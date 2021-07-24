class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
    def insert(self, d):
        k=Node(d)
        if(self.root==None):
            self.root=k
        else:
            t=self.root
            while(t!=None):
                t1=t
                if(t.data>k.data):
                    t=t.left
                else:
                    t=t.right
            t=t1
            if(t.data>k.data):
                t.left=k
            else:
                t.right=k

k=BST()
k.insert(10)
k.insert(20)
k.insert(40)
k.insert(5)
k.insert(2)
print(k)

