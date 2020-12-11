from Buildings import Building, Mint, Hut

class User:
    def __init__(self,nickname):
        self.__money = 2000
        self.__nickname = nickname
        self.__collection = []

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money
    
    @property
    def nickname(self):
        return self.__nickname
    @nickname.setter
    def nickname(self,money):
        self.__nickname = nickname

    def get_collection(self):
        return self.__collection

    def buy_building(self,building:Building):
        if(self.__money < building.value):
            print("You can't buy building!")
        else:
            self.__money-=building.value
            print("You bought",building.name)
            self.__collection.append(building)
            print("Your savings:",self.__money)

    def check_principle(self)->Building:
        counter = 0

        for c in self.__collection:
            if isinstance(c, Mint) or isinstance(c, Hut):
                counter+=1
                if counter == 2:
                    print("Możesz wybudować kopalnię złota, mennicę i tartak")
                else:
                    print("Nie możesz wybudować kopalnii złota, mennicy oraz tartaku")


user1 = User('Ola')
mint = Mint('Mint',3000)
hut = Hut("Hut",200)
user1.buy_building(mint)
user1.buy_building(hut)
print(user1.get_collection())
user1.check_principle()