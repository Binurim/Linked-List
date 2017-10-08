class node:
  def __init__(self, d, n=None):
    self.data = d
    self.next = n
    
  def setData(self,d):
    self.data = d
    
  def getData(self):
    return self.data
    
  def getNext(self):
    return self.next
    
  def setNext(self,n):
    self.next = n
  
class linkedList:
  def __init__(self):
    self.head = None
    self.size = 0
    
  def getSize(self):
    return self.size
    
  def addF(self,d):
    self.head = node(d)
    self.size += 1
    print(d,"Added as head")
    
  def addL(self,d):
    if self.head == None:
      print("Linked List is empty. Adding as Head..")
      self.head = node(d)
      self.size += 1
    else:
      cur = self.head
      while cur.next != None:
        cur = cur.next
      cur.next = node(d)
      self.size += 1
      print(d,"Added as End..")
      
  def addC(self, d, p):
    if self.size == 0:
      self.head = node(d)
      self.size += 1
    elif self.size == p-1:
      cur = self.head
      while cur.next != None:
        cur = cur.next
      cur.next = node(d)
      self.size += 1
      print(d,"Added as End..")
    else:
      pos = 1
      cur = self.head
      while pos < p-1:
        cur = cur.next
        pos += 1
      new = node(d)
      new.next = cur.next
      cur.next = new
      self.size += 1
      print(d,"Added to given position..")
      
  def printll(self):
    cur = self.head
    print("\n\n\n-----------------------------")
    print("Your Linked List is")
    while cur.next != None:
      print(cur.data)
      cur = cur.next

l = linkedList()
l.addF(10)
l.addL(50)
l.addL(60)
l.addL(70)
l.addL(80)
l.addL(90)
l.addL(100)
l.addC(20,2)
l.addC(30,3)
l.addC(40,4)
l.printll()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    