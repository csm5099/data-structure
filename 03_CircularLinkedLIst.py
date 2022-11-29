class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class CircularLinkedList:
  def __init__(self):
    self.head = None
    self.current = None
    self.before = None
    self.no = 0
    
  def __len__(self):
    return self.no
  
  def create_node(self, data):
    return Node(data)
  
  def is_list_empty(self):
    return True if (self.head == None) else False
  
  def add_node_to_empty(self,data):
    new_node = self.create_node(data)
    self.head = new_node
    self.current = new_node
    new_node.next = self.head
    self.no += 1
    
  def add_node_to_first(self, data):
    new_node = self.create_node(data)
    new_node.next = self.head
    self.head.next = new_node
    self.head = new_node
    self.no += 1
    
  def add_node_to_middle(self, data):
    new_node = self.create_node(data)
    new_node.next = self.before.next
    self.before.next = self.before.next
    self.no += 1
    
  def add_node_to_last(self, data):
    new_node = self.create_node(data)
    new_node.next = self.head
    self.head = new_node
    self.current.next = self.head
    
  def sort_asc(self,data):
    cursor = self.head
    while self.current != self.head:
      if cursor.data > data:
        self.current = cursor
        return cursor
      else:
        self.before = cursor
        cursor = cursor.next
    return None
  
  def do_sort_insert(self,data):
    if self.is_list_empty():
      self.add_node_to_empty(data)
    else:
      cursor = self.sort_asc(data)
      
      if cursor == self.head:
        self.add_node_to_first(data)
        
      elif cursor != None:
        self.add_node_to_middle(data)
        
      else:
        self.add_node_to_last(data)
    
    self.current = self.head

  def print_node_data(self):
    while self.current != self.head:
      print(f"{self.current.data}")
      self.current = self.current.next
  
  def search_node(self, target):
    cursor = self.head
    while self.current != self.head:
      if cursor.data == target:
        self.current = cursor
        return cursor
      else:
        self.before = cursor
        cursor = cursor.next
    return None
  
  def delete_node(self, target):
    print(f"delete data : {target}")
    cursor = self.search_node(target)
    
    if self.is_list_empty():
      return False

    else:
      # the target is in the start of this list
      if self.current.next == self.head.next:
        print("first")
        self.head = self.current.next
        
      # the target is in the end of this list
      elif self.current.next == self.head:
        print("last")
        self.before.next = None
      
      # the target is in the middle of this list
      else:
        print("middle")
        self.before.next = self.current.next

lkdlst = CircularLinkedList()
inputs = [2,7,3,5,8,1,4,6]

for item in inputs:
  lkdlst.do_sort_insert(item)

lkdlst.print_node_data()