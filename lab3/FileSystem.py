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
    def get_name(self):
        pass
    @abstractmethod
    def check_name(self,name,type_of, data = None):
        pass


class File(Node):
    def __init__(self,name,data):
        self.__name = name
        self.__data = data
        
    def more(self):
        print(self.__data)

    def get_name(self):
        return self.__name

class Folder(Node):
    def __init__(self,name):
        self.__name = name
        self.__children = []

    def create_tree(self):
        print("", self.__name)
        children = self.get_children()
        for child in children:
            print(" |__",child.get_name())
            next_node_children =  child.get_children()
            if next_node_children !=[]:
                for child in next_node_children:
                    print("     |_",child.get_name())
    def get_name(self):
        return self.__name

    def ls(self):
        children = self.get_children()
        for child in children:
            print(child.get_name())
        
    def add_node(self,node):
        self.__children.append(node)
            
    def remove_node(self,node):
        node_children = node.get_children()
        if node_children == []:
            self.__children.remove(node)
        else:
            node_children.clear()
            self.__children.remove(node)

    def get_children(self):
        return self.__children

class CheckName(Node):
    def check_name(self,name,type_of, data = None):
        count = name.count(".")
        invalidcharacters= set(string.punctuation)
        invalidcharacters.remove(".")
        
        if any(char  in invalidcharacters  for char in name ) or count>=2:
            print ("Name of " ,name, " is invalid! Can't create object.")
            return 0
        else:
            print ("Name of " ,name, " is valid!")
            if type_of == 'file':
                return File(name,data)
            else:
                return Folder(name)
            



folderA = CheckName().check_name('A', 'folder')
folderB = CheckName().check_name('B', 'folder')
folderC = CheckName().check_name('C', 'folder')
folderD = CheckName().check_name('D', 'folder')
folderE = CheckName().check_name('D...', 'folder')
fileA = CheckName().check_name('fileA', 'file','some data in fileA')


folderA.add_node(folderB)
folderA.add_node(folderC)
folderB.add_node(folderD)
folderB.add_node(fileA)

print("All added folders and files:")
folderA.create_tree()

print("Ls command on folder",folderA.get_name(),":")
folderA.ls()

folderA.remove_node(folderB)

print("After removing folder B:")
folderA.create_tree()

print("Ls command on folder",folderA.get_name(),":")

folderA.ls()



