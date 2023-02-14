#students_list=[]
class student:
 def __init__(self,name,id,grade):
    self.name=name
    self.id=id
    self.grade=grade
    self.next=None
    self.prev=None
class students:
    def __init__(self):
        self.head=None
        self.tail=None

    def student_add(self,data):
        s=student(*data)

        if self.head==None :
            self.head=s
            self.tail=s
        else :
            #if self.tail!=None:
            self.tail.next=s
            s.prev=self.tail
            self.tail=s
    def student_insert(self,loc,data):
        s=student(*data)
        if self.tail==None :
            self.head=s
            self.tail=s 
        else:
            i=0
            cur=self.head
            if loc ==0:
                s.next=cur
                cur.prev=s
                self.head=s
            while i < loc-1 and cur.next!= None:
                cur=cur.next
                i=i+1
            if cur == self.tail :
                cur.next=s
                s.prev=cur
                self.tail=s
            else:
                cur.next.prev=s
                s.next=cur.next
                s.prev=cur
                cur.next=s

    def student_search_name(self,name):
        if self.head!=None:
           cur=self.head
           while cur.name != name :
            cur=cur.next      
        return cur 
    def student_search_id(self,id):
        if self.head!=None:
           cur=self.head
           while cur.id != id:
            cur=cur.next
        return cur 
    def print_students(self):
        curr = self.head
        if curr == None:
            print("Empty list of students")
        else:
            while curr.next != None:
                print(f"{curr.name},{curr.id},{curr.grade}")
                curr = curr.next

def main():
    s0= students()
    s0.student_add(('amr',10,'A'))
    s0.student_add(('ziad',11,'B'))
    s0.student_add(('ahmed',12,'C'))
    s0.student_insert(0,('zizoo',20,'D-'))
    s0.student_insert(2,('mostafa',13,'D')) #mid
    s0.student_insert(10,('boda',15,'D-')) #out
    s0.student_insert(5,('mohamed',14,'D+')) #end
    s0.print_students()
        
    #node = s0.student_search_name('boda')
    #print(node.name)
    #node = s0.student_search_id(11)
    #print(node.id)
if __name__  =="__main__" :
    main() 


