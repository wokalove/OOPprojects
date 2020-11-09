
class Tree:
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

  def print_tree(self):
      print(self.value)
      for c in self:
          print("--",c.value)
          if c.children ==[]:
                continue
          else:
              for cc in c.children:
                  print("  --",cc.value)
                  if cc.children==[]:
                      continue
                  else:
                      for ccc in cc.children:
                          print("       --",ccc.value)
  def append_node(self,obj):
      self.children.append(obj)
  def remove_node(self,name,surname,id_number):
      for c in self:
          if c.value == name:
              del c.value
   
      
  def get_children(self):
      return self.children


class Flyweight(Tree):
    def __init__(self,root):
        self.children = root.get_children()

    def add_non_exist_name(self, if_exists,name,surname,id_number):
        self.append_node(Tree(name))
        
        last_node = len(self.children)-1
        self.children[last_node].append_node(Tree(surname))

        last_node = len(self.children)-1
        self.children[last_node].children[0].append_node(Tree(id_number))

    def add_exist_name(self,name,surname,id_number,name_index):
        child_index=0
        for i in self.children[name_index]:
            child_index+=1
        
        self.children[name_index].append_node(Tree(surname))

        self.children[name_index].children[child_index].append_node(Tree(id_number))


    def check(self,if_exists,name,surname,id_number,name_index):
        print(if_exists)
        if if_exists[2]==True:
            print("Can't create object with the same id!")
            return 0
        else:
            if if_exists[0] == False:
                self.add_non_exist_name(if_exists,name,surname,id_number)
            else:
                self.add_exist_name(name,surname,id_number,name_index)


            
    def search_tree(self,name, surname, id_number):
        name_index = None
        
        name_bool = False
        surname_bool =False
        id_number_bool =False

        for c in self:
            if c.value == name:
                print("Name",c.value, "exists in tree!")
                name_bool = True
                name_index = self.children.index(c)

            if c.children ==[]:
                continue
            else:
                for cc in c.children:
                    if isinstance(cc.value,list):
                        for c in cc.value:
                            if c == surname:
                                print("Surname",c ,"already exists in tree!")
                                surname_bool = True
                    if cc.value==surname:
                        print("Surname",cc.value ,"already exists in tree!")
                        surname_bool == True
                    else:
                        if surname_bool == False:
                            surname_bool = True
    
                    if cc.children==[]:
                        continue
                    else:
                        for ccc in cc.children:
                            if ccc.value==id_number:
                                print("Id",ccc.value, "already exists in tree! Can't create object.")
                                id_number_bool = True
        if_exists=[name_bool,surname_bool,id_number_bool]
        print("Index imienia",name_index)
        self.check(if_exists,name,surname,id_number,name_index)


 
root = Tree("People")

root.append_node(Tree("Katarzyna"))
root.append_node(Tree("Agnieszka"))

root.children[0].append_node(Tree(["Iksińska","Górniak"]))
root.children[1].append_node(Tree("Nowak"))

root.children[0].children[0].append_node(Tree(32632721))
root.children[1].children[0].append_node(Tree(89435495))

root.print_tree()

fly = Flyweight(root)
fly.search_tree("Ania","Górniak",32632721333)
root.print_tree()
fly.search_tree("Ania","Była",32632753)
root.print_tree()
fly.search_tree("Ania","Kazimierska",326327539999)
root.print_tree()
fly.search_tree("Agnieszka",["Kotulska","Misial"],32663733)
root.print_tree()