import fs
from io import StringIO
from abc import ABCMeta, abstractmethod
import string


class Node:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create_tree(self):
        pass
    @abstractmethod
    def ls(self):
        pass
    @abstractmethod
    def more(self):
        pass
    @abstractmethod
    def get_name(self,name):
        pass

class File(Node):
    def __init__(self,name,data):
        self.name = name
        self.data = data
    def more(self):
        print(self.data)
    def get_name(self):
        return self.name

class Folder(Node):
    def __init__(self,name):
        self.name = name
        self.children = []
    def create_tree(self):
        print("", self.name)
        children = self.get_children()
        for child in children:
            print(" |__",child.name)
            next_node_children =  child.get_children()
            if next_node_children !=[]:
                for child in next_node_children:
                    print("     |_",child.name)
        
    def get_name(self):
        return self.name


    def ls(self):
        pass
    def add_node(self,node):
        self.children.append(node)
    def remove_node(self,node):
        self.children.remove(node)
    def get_children(self):
        return self.children



class CheckName(Node):
    def __init__(self,node):
        self.node = node
        self.check_name(node)
    def check_name(self,name):
        count = name.count(".")
        invalidcharacters= set(string.punctuation)
        invalidcharacters.remove(".")
        
        if any(char  in invalidcharacters  for char in name ) or count>=2:
            print ("Name of " ,name, " is invalid!")
        else:
            print ("Name of " ,name, " is valid!")




folderA = Folder('A...')
folderB = Folder('B')
folderC = Folder('C')
folderD = Folder ('D')
fileA = File("fileA","data1")


folderA.add_node(folderB)
folderA.add_node(folderC)
folderB.add_node(folderD)
folderB.add_node(fileA)


folderA.create_tree()

folderA_name = folderA.get_name()
CheckName(folderA_name)

'''    
print("from folder1 ")
for i in folder1.children:
    print(i.name)
print("from folder2")
for i in folder2.children: 
    print(i.name)
'''

