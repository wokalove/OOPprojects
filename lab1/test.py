import urllib.request
import xmltodict

class Connect:
    def __init__(self,url_link):
        self.connect = urllib.request.urlopen(url_link)


class Parsing:
    def __init__(self,obj):
        read_file = obj.connect.read()
        self.data = xmltodict.parse(read_file)
       # print(self.data)
        
class CurrencySet:
    def __init__(self,obj):
        self.currency_set = obj.data
        print(self.currency_set)

class Currency:
    '''
    def __init__():
        ''' '''
    def get_currency_code():
        ''' '''
    def get_rate():
        ''' '''
        '''
url='https://www.nbp.pl/kursy/xml/lasta.xml'

object1 = Connect(url)
parsed = Parsing(object1)
currency_set = CurrencySet(parsed)