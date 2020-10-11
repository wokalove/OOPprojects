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
        self.currency_set = obj.data['tabela_kursow']['pozycja']
        #print(self.currency_set)
    def get_position(self):
        all_positions = []
        self.len_currency_set = len(self.currency_set)
        for i in range(self.len_currency_set):
            self.result_list = [v for k,v in self.currency_set[i].items()]
            #all_positions.append(self.result_list)
            #print(self.result_list)
        return all_positions
    
class Currency(object):
    
    def get_currency_name(self,curr,name):
         
        self.len_currency_set = len(curr.currency_set)
        for i in range(self.len_currency_set):
            self.result_list = [v for k,v in curr.currency_set[i].items()]
            if self.result_list[0] == name:
                name = self.result_list[0]
        return name

    def get_currency_converter(self,curr,from_curr, to_curr):
        self.len_currency_set = len(curr.currency_set)
        for i in range(self.len_currency_set):
            self.result_list = [v for k,v in curr.currency_set[i].items()]

            if self.result_list[0] == from_curr:
               from_curr = self.result_list[1]
            if self.result_list[0] == to_curr:
                to_curr = self.result_list[1]
        converter = [from_curr,to_curr]
        return converter

    def get_currency_code(self,curr,name):
        self.len_currency_set = len(curr.currency_set)
        for i in range(self.len_currency_set):
            self.result_list = [v for k,v in curr.currency_set[i].items()]
    
            if self.result_list[0] == name:
                code = self.result_list[2]
        return code
        
    def get_currency_rate(self,curr,from_curr,to_curr):
        self.len_currency_set = len(curr.currency_set)
        for i in range(self.len_currency_set):
            self.result_list = [v for k,v in curr.currency_set[i].items()]

            if self.result_list[0] == from_curr:
               from_curr = self.result_list[3]
            if self.result_list[0] == to_curr:
                to_curr = self.result_list[3]
        #print(rate)
        rate =  [from_curr,to_curr]
        return rate

'''
url='https://www.nbp.pl/kursy/xml/lasta.xml'

object1 = Connect(url)
parsed = Parsing(object1)
currency_set = CurrencySet(parsed)
currency = Currency()
print(currency.get_currency_code(currency_set,'peso filipińskie'))
'''