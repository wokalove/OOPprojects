class Iterator:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __iter__(self):
      self.index = 0
      return self
  def __next__(self):
      if self.index<0 or self.index>len(self.children)-1:
          raise StopIteration
      else:
          result = self.children[self.index]
          self.index+=1
          return result

  def print_all(self):
      print(self.value)
      for c in self:
          print("--",c.value)
          if c.children ==[]:
                continue
          else:
              for cc in c.children:
                  print("  --",cc.value)
  def append_node(self,obj):
      self.children.append(obj)
  def print_tree(self):
      print(self.value)

obj = Iterator(3)
obj.append_node(Iterator(2))
obj.append_node(Iterator(4))
obj.append_node(Iterator(5))
obj.children[0].append_node(Iterator(2))

obj.print_all()

'''
for c in obj:
    print("Printuję obiekty",c.value)


for c in obj.children[0]:
    print("Printuję obiekty dziecka",c)
'''