
class Tree:
  def __init__(self, value):
    self.value = value
    self.children = []

  def print_all(self):
      print(self.value)
      for c in self.children:
          print("--",c.value)
          if c.children ==[]:
                continue
          else:
              for cc in c.children:
                  print("  --",cc.value)
  def append_node(self,obj):
      self.children.append(obj)
  def remove_node(self,item):
      pass
  def get_children(self):
      return self.children


class Flyweight(Tree):
    def __init__(self):
        self.children = self.get_children()
        print(self.children)
        
    def search_tree(self):
        print(self.value)
        for c in self.children:
            print("--",c.value)
            if c.children ==[]:
                continue
            else:
                for cc in c.children:
                    print("  --",cc.value)
 
root = Tree("Katarzyna")
root.append_node(Tree("Iksińska"))
root.append_node(Tree("Nowak"))
root.children[0].append_node(Tree(97059382))
root.children[1].append_node(Tree(32632721))


root.print_all()

fly = Flyweight()
#fly.search_tree()

