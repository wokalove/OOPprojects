import fs
from io import StringIO
from abc import ABCMeta, abstractmethod

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
    def name(self):
        pass

class File(Node):
    def __init__(self,name,data):
        self.name = name
        self.data = data
    def create_tree(self,data):
        pass

class Folder(Node):
    def __init__(self,name):
        self.name = name
    def create_tree(self,nodes):
        nodes.tree()

class Proxy:
    pass
class ManageNode(Node):
    def __init__(self):
        self.new = fs.open_fs('mem://')
    def remove_node(self):
        pass
    def add_new_node(self,name):
        return self.new.makedirs(name)
    def create_tree(self):
        self.new.tree()


obj2 = Folder("folder1")
new = ManageNode().add_new_node('folder')
new = ManageNode().add_new_node('olla')
ManageNode().create_tree()
#obj2.create_new('mój/kolejny')
#obj2.print_tree()
#obj2.create_new('jeden')
#obj2.print_tree()

obj = File("moj plik",'blalala')
#obj.write_to_file("ooola")
