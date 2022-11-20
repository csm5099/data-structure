class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.before = None
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
    self.before = new_node
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
    new_node.next = self.before.next
    self.before.next = new_node
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

  def print_node_data(self):
    tmp = self.head
    while tmp is not None:
      print(f"{tmp.data}")
      tmp = tmp.next

  def search_node(self,target):
    tmp = self.head
    while tmp is not None:
      if tmp.data == target:
        return tmp
      else:
        self.before = tmp
        tmp = tmp.next
    return None

  def delete_node(self, target):
    print(f"delete data")
    current = self.search_node(target)
    
    if self.is_list_empty():
      return False
    else:
      if current.next != None:
        # the target is in the start of this list
        if current.next == self.head.next:
          print("first")
          self.head = current.next
        # the target is in the end of this list
        elif current.next == self.tail.next:
          self.before.next = None
        
        # the target is in the middle of this list
        else:
          self.before = current.next
      
      else:
        return False







lkdlst = LinkedList()
inputs = [2,7,3,5,8,1,4,6]

# insert node and sort
for item in inputs:
  lkdlst.do_sort_insert(item)
  lkdlst.print_node_data()

print(f"-------------")
# print length of the list
print(f"length of list is {len(lkdlst)}")

print(f"-------------")
# print each nodes address
node = lkdlst.head
while node is not None:
  print(f"{id(node)}")
  node = node.next
print(f"-------------")

#search a data
print(lkdlst.search_node(4))
print(lkdlst.search_node(1))
print(lkdlst.search_node(3))
lkdlst.search_node(10)

#delete data
lkdlst.delete_node(1)
lkdlst.print_node_data()
lkdlst.delete_node(4)
lkdlst.print_node_data()
