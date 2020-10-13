import urllib.request
import xmltodict

class Connect:
    def __init__(self):
        self.connect = urllib.request.urlopen('https://www.nbp.pl/kursy/xml/lasta.xml')
        

class Parsing:
    def __init__(self):
        self.data = Connect()
    def parse(self):
        read_file = self.data.connect.read()
        self.data = xmltodict.parse(read_file)
        return self.data
class CurrencySet:
    def __init__(self):
        self.parsing_object = Parsing()

    def get_parsed(self):
        parsed = self.parsing_object.parse()
        self.new_curr_set = parsed['tabela_kursow']['pozycja']
        return self.new_curr_set


class Currency(object):
    
    def get_currency_name(self,curr,length,name):
        len_currency_set = length
        for i in range(len_currency_set):
            result_list = [v for k,v in curr[i].items()]
            if result_list[0] == name:
                name = result_list[0]
        return name

    def get_currency_converter(self,curr,length,from_curr, to_curr):
        len_currency_set = length
        for i in range(len_currency_set):
            result_list = [v for k,v in curr[i].items()]

            if result_list[0] == from_curr:
               from_curr = result_list[1]
            if result_list[0] == to_curr:
                to_curr = result_list[1]
        converter = [from_curr,to_curr]
        return converter

    def get_currency_code(self,curr,length,name):
        len_currency_set = length
        for i in range(len_currency_set):
            result_list = [v for k,v in curr[i].items()]
    
            if result_list[0] == name:
                code = result_list[2]
        return code
        
    def get_currency_rate(self,curr,length,from_curr,to_curr):
        len_currency_set = length
        
        for i in range(len_currency_set):
            result_list = [v for k,v in curr[i].items()]

            if result_list[0] == from_curr:
               from_curr = result_list[3]
            if result_list[0] == to_curr:
                to_curr = result_list[3]
        
        rate =  [from_curr,to_curr]
        return rate
