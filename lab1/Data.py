import urllib.request
import xmltodict

class Connect:
    def __init__(self,url_link):
        self.connect = urllib.request.urlopen(url_link)
        #Parsing(selff)

class Parsing:
    def __init__(self,obj):
        read_file = obj.connect.read()
        self.data = xmltodict.parse(read_file)
        #CurrencySet(self)
        
class CurrencySet:
    def __init__(self,obj):
        self.currency_set = obj.data['tabela_kursow']['pozycja']
        #print(self.currency_set)

class Currency:
    def get_position(self,obj):
        self.len_currency_set = len(obj.currency_set)
        for i in range(self.len_currency_set):
            self.result_list = [v for k,v in obj.currency_set[i].items()]
            print(self.result_list)
            return self.result_list
    
    def get_currency_name(self,obj):
        values = self.get_position(obj)
        name = values[0]
        return name
    def get_converter(self,obj):
        values = self.get_position(obj)
        converters = values[1]
        return converters
    def get_currency_code(self,obj):
        values = self.get_position(obj)
        codes = values[2]
        return codes
    def get_currency_rate(self,from_curr,to_curr):
        values = self.result_list
        
        rates = values[3]
        return rates



url='https://www.nbp.pl/kursy/xml/lasta.xml'

object1 = Connect(url)
parsed = Parsing(object1)
currency_set = CurrencySet(parsed)
currency = Currency()
print(currency.get_position(currency_set))