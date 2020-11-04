class Tree():
    def __init__(self,root):
        self.root = root
        self.children = []
        self.Nodes=[]
    def addNode(self,obj):
        self.children.append(obj)

    def __iter__(self):
        return self

    def __next__(self):
        x =self.children
        x+=1
        return x

    def print_all(self):
        print(self.root)
        for c in self.children:
            print("--",c.data)
            if c.children ==[]:
                continue
            else:
                print("  --",c.children)

    def print_tree(self,low,high):
        current = low
        while current < high:
            yield current
            current += 1
                
        '''for c in iterator(3, 9):
            print(c)
        '''
class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)
    def get_data(self):
        return self.data
    def getChildNodes(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)


class Flyweight:
    def search(self,item):
        pass


n = Tree("Iza")
p = Tree('Kasia')
q = Tree('Antoni')
n.addNode(Node("Kowalska"))
n.addNode(Node("Nowak"))

n.children[0].addNode(Node(1029))
n.children[1].addNode(Node(1234))
#n.getAllNodes()
print(n.children[0])

n.print_all()

myiter = iter(n)
print(next(myiter))
