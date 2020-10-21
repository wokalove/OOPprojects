import fs
from io import StringIO
from abc import ABCMeta, abstractmethod

class Node:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create_new(self, name):
        pass
    @abstractmethod
    def remove(self, name):
        pass

class File(Node):
    def __init__(self,name):
        self.name = name
    def write_to_file(self,data):
        self.name = StringIO()
        self.name.write(data)
        print('cos ',file=self.name)
        print(self.name.getvalue())
        self.name.close()

class Folder(Node):
    def create_new(self,name):
        self.new = fs.open_fs('mem://')
        self.new.makedirs(name)
    def print_tree(self):
        self.new.tree()




obj2 = Folder()
obj2.create_new('mój/kolejny')
obj2.print_tree()
obj2.create_new('jeden')
obj2.print_tree()

obj = File("moj plik")
obj.write_to_file("ooola")
