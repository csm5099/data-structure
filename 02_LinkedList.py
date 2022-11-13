class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.current = None
    self.no = 0
  
  def __len__(self):
    return self.no
  
  def create_node(self, data):
    return Node(data)
  
  def is_list_empty(self):
    if self.head == None:
      return True
    else:
      return False
  
  def add_node_to_empty(self,data):
    print("empty")
    new_node = self.create_node(data)
    self.head = new_node
    self.tail = new_node
    self.current = new_node
    self.no += 1
  
  def add_node_to_first(self, data):
    print("first")
    new_node = self.create_node(data)
    new_node.next = self.head
    self.head = new_node
    self.no += 1
  
  def add_node_to_middle(self, data):
    print("middle")
    new_node = self.create_node(data)
    new_node.next = self.current.next
    self.current.next = new_node
    self.no += 1
  
  def add_node_to_last(self, data):
    print("last")
    new_node = self.create_node(data)
    self.tail.next = new_node
    self.tail = new_node
    self.no += 1
    
  def sort_asc(self,data):
    cursor = self.head
    while cursor is not None:
      if cursor.data > data:
        return cursor
      else:
        self.current = cursor
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

  def print_list(self):
    tmp = self.head
    while tmp is not None:
      print(f"{tmp.data}")
      tmp = tmp.next

  def search_node(self):
    pass
  
  def delete_node(self):
    pass
  
  def concatenate_list(self):
    pass

lkdlst = LinkedList()
inputs = [2,7,3,5,8,1,4,6]
for item in inputs:
  lkdlst.do_sort_insert(item)
  lkdlst.print_list()
print(f"length of list is {len(lkdlst)}")