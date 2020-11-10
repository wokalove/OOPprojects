
class Tree:
  def __init__(self, value):
    self._value = value
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
      print(self._value)
      for c in self:
          print("--",c._value)
          if c.children ==[]:
                continue
          else:
              for cc in c.children:
                  print("  --",cc._value)
                  if cc.children==[]:
                      continue
                  else:
                      for ccc in cc.children:
                          print("       --",ccc._value)
  def append_node(self,obj):
      self.children.append(obj)

  def remove_node(self,name_id,surname_id):
      print(name_id,surname_id)
      del self.children[name_id].children[surname_id]
    
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


    def add_new_person(self,if_exists,name,surname,id_number,name_index):
        print(if_exists)
        if if_exists[2]==True:
            print("Can't create object with the same id!")
            return 0
        else:
            if if_exists[0] == False:
                self.add_non_exist_name(if_exists,name,surname,id_number)
            else:
                self.add_exist_name(name,surname,id_number,name_index)


            
    def search_tree(self,name, surname, id_number,action):
        name_index = None
        surname_index = None
        
        name_bool = False
        surname_bool =False
        id_number_bool =False

        for c in self:
            if c._value == name:
                print("Name",c._value, "exists in tree!")
                name_bool = True
                name_index = self.children.index(c)

            if c.children ==[]:
                continue
            else:
                for cc in c.children:
                    if isinstance(cc._value,list):
                        for c in cc._value:
                            if c == surname:
                                print("Surname",c ,"already exists in tree!")
                                surname_bool = True
                    if cc._value == surname:
                        print("Surname",cc._value ,"already exists in tree!")
                        surname_bool == True
                        surname_index = self.children[name_index].children.index(cc)
                    else:
                        if surname_bool == False:
                            surname_bool = True
    
                    if cc.children==[]:
                        continue
                    else:
                        for ccc in cc.children:
                            if ccc._value==id_number:
                                print("Id",ccc._value, "already exists in tree!")
                                id_number_bool = True
        if_exists=[name_bool,surname_bool,id_number_bool]
        print("Index imienia",name_index)

        if(action =="add"):
            self.add_new_person(if_exists,name,surname,id_number,name_index)
        elif(action =="remove"):
            self.remove_node(name_index,surname_index)



 
root = Tree("People")

root.append_node(Tree("Katarzyna"))
root.append_node(Tree("Agnieszka"))

root.children[0].append_node(Tree(["Iksińska","Lotos"]))
root.children[1].append_node(Tree("Nowak"))

root.children[0].children[0].append_node(Tree(89022511203))
root.children[1].children[0].append_node(Tree(79031104637))

root.print_tree()

fly = Flyweight(root)
fly.search_tree("Ania","Górniak",990221983640,"add")
root.print_tree()
fly.search_tree("Ania","Była",60040163746,"add")
root.print_tree()
fly.search_tree("Ania","Kazimierska",77011242915,"add")
root.print_tree()
fly.search_tree("Agnieszka",["Kotulska","Misial"],68113025183,"add")
root.print_tree()

fly.search_tree("Agnieszka","Nowak",79031104637,"remove")

root.print_tree()