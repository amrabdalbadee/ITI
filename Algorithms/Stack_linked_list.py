#stack with linkedlist
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self,data):
        self.data=data
        self.tail=None
    def add(self,data):
        retval =False
        nd = Node(data)
        if self.tail==None:
              self.tail=nd
              retval=True
        else:
            nd.next = self.tail
            self.tail=nd
            retval=True
        return retval           
    def pop(self):
        result=None
        if self.tail==None:
            print('stack is empty')
        else:
            result=self.tail
            self.tail=self.tail.next
        return result    

