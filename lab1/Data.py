import urllib.request
import xmltodict

class Connect:
    def __init__(self,url_link):
        self.connect = urllib.request.urlopen(url_link)
        Parsing(self)


class Parsing:
    def __init__(self,obj):
        read_file = obj.connect.read()
        self.data = xmltodict.parse(read_file)
        CurrencySet(self)
        
class CurrencySet:
    def __init__(self,obj):
        self.currency_set = obj.data
        #print(self.currency_set)
        print(self.currency_set.get('tabela_kursow'))
        

class Currency:
    def __init__(self,obj):
        self.obj = obj

        ''' '''
    #def get_currency_code():
        ''' '''
    #def get_rate():
        ''' '''

url='https://www.nbp.pl/kursy/xml/lasta.xml'

object1 = Connect(url)
#object2 = Convert(object1)