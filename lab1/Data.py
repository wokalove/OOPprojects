import urllib.request
import xmltodict

class Connect:
    def __init__(self,url_link):
        self.connect = urllib.request.urlopen(url_link)
        #Parsing(self)


class Parsing:
    def __init__(self,obj):
        read_file = obj.connect.read()
        self.data = xmltodict.parse(read_file)
        #CurrencySet(self)
        
class CurrencySet:
    def __init__(self,obj):
        self.currency_set = obj.data
        #print(self.currency_set)

class Currency:
    @staticmethod
    def get_name(obj):
        name = obj.currency_set
        return name
    def get_currency_code(self,obj):
        code = 1
        return code
    def get_rate(self,obj):
        rate = 1
        return rate


url='https://www.nbp.pl/kursy/xml/lasta.xml'

object1 = Connect(url)
parsed = Parsing(object1)
currency_set = CurrencySet(parsed)
currency = Currency()
#print(currency.get_name(currency_set))