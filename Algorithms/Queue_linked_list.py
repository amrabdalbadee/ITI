#queue with linkedlist
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,data):
        retval =False
        nd =Node(data)
        if self.head==None:
                self.head=nd
                self.tail=nd
                retval=True
        else:
            self.tail.next=nd
            self.tail=nd
            retval=True
        return retval   
    def pop(self):
        result=None
        if self.head==None:
            print('queue is empty')
        elif self.head==self.tail:
            result = self.head
            self.head = None
            self.tail = None
        else:
            result=self.head
            self.head=self.head.next
        return result
    def print(self):
        print(f'Head = {self.head.data}\n')
        print(f'Tail = {self.tail.data}\n')
        print(f'Queue Elements are:')
        element = self.head
        while element != None:
            print(element.data)
            element = element.next
        print('----------------------------')
def main():
    q0 = queue()
    q0.add(1)
    q0.add(2)
    q0.add(3)
    q0.print()
    q0.pop()
    q0.print()





if __name__ == "__main__":
    main()