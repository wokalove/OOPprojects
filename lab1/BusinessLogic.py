from Data import *

class Convert(object):
    @staticmethod
    def get_set():
        object1 = Connect()
        parsed = Parsing(object1)
        currency_set = CurrencySet(parsed)
        print(currency_set)
        return currency_set
    @staticmethod
    def get_currency():
        currency = Currency()
        return currency
    @staticmethod
    def convert_from_pln(money,avg_exchange_rate,converter):
        converted = money* avg_exchange_rate/converter
        return converted
    @staticmethod
    def convert_to_pln(money,avg_exchange_rate,converter):
        converted = money/avg_exchange_rate*converter
        return converted
    
    def convert(self,money,rate_one, rate_two,converter_one, converter_two):
        to_pln = self.convert_to_pln(money, rate_one,converter_one)
        converted_money = self.convert_from_pln(to_pln,rate_two,converter_two)
        print (converted_money)
        return converted_money



