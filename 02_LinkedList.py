#node class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
#Linked list class  
class LinkedList:
  def __init__(self):
    self.no = 0
    self.head = None
    self.tail = None
    self.current = None
    
  def __len__(self):
    return self.no
    
  def create_node(self, data):
    return Node(data)
  
  '''
  def search_node(self,data):
    count = 0
    cursor = self.head
    while cursor is not None:
      if cursor.data == data:
        self.current = cursor
        return count
      count +=1
      cursor = cursor.next
    return -1
  
  def before_cursor(self, index):
    cursor = self.head
    for i in range(index):
      self.current = cursor
      
    def is_empty(self):
    if self.head is None:
      print("this list is empty!!!")
      return True
    else:
      print("this list is not empty!!!")
      return False
      
    def add_node_last(self, data):
    new = self.create_node(data)
    if self.tail.next == None:
      self.tail.next = new
      self.tail = new
  '''

  #insert_node
  def insert_node(self, data):
    new = self.create_node(data)
    #빈 리스트인지 확인하기
    if self.head == None:
      #그냥 삽입
      self.head = new
      self.tail = new
      pass
    else:
      #맨앞 삽입
      if self.current.next == None:
        new.next = self.current  
        self.current = new
      #중간 삽입
      else:
        new.next = self.current.next
        self.current.next = new

    self.no += 1
    
  def sort_asc(self, data):
    tmp = self.head
    while tmp is not None:
      if tmp.data > data:
        self.current = tmp
        self.insert_node(data)
      else:
        tmp = tmp.next
    self.insert_node(data)
    
  def print_list(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.data)
      tmp = tmp.next
    
lkdlst = LinkedList()
lkdlst.sort_asc(5)
lkdlst.sort_asc(1)
lkdlst.sort_asc(2)
lkdlst.sort_asc(6)
lkdlst.print_list()