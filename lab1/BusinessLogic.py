from Data import *

class Convert(object):
    @staticmethod
    def convert_from_pln(money,avg_exchange_rate,converter):
        converted = money* avg_exchange_rate/converter
        return converted
    @staticmethod
    def convert_to_pln(money,avg_exchange_rate,converter):
        converted = money/avg_exchange_rate*converter
        return converted
    
    def convert(self,money,currency_one, currency_two,converter_one, converter_two):
        to_pln = self.convert_to_pln(money, currency_one,converter_one)
        converted_money = self.convert_from_pln(to_pln,currency_two,converter_two)
        return converted_money


con = Convert()
print(con.convert_to_pln(20,4.30,100))