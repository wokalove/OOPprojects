from BusinessLogic import Convert


class UserInterface(object):
    def __init__(self) -> None:
        self.business_logic = Convert()
    
    def questions(self):
    
        currency_set = self.business_logic.get_set()
        length = len(currency_set)
        currency = self.business_logic.get_currency()

        money = int(input("Enter money amount:"))
     
        #from_curr = 'dolar amerykański'
        #to_curr = 'dolar Hongkongu'
        from_curr = input("From currency:")
        to_curr = input("To currency:")
        
        rates = currency.get_currency_rate(currency_set,length,from_curr,to_curr)
        
        rate=[]
        for r in rates:
            rate.append(float(r.replace(',', '.')))
        rate_one = rate[0]
        rate_two = rate[1]

        converters = currency.get_currency_converter(currency_set,length,from_curr,to_curr)
        converter =[]
        for c in converters:
            converter.append(float(c.replace(',', '.')))
        converter_one = converter[0]
        converter_two = converter[1]
    
        converted = self.business_logic.convert(money,rate_one,rate_two,converter_one,converter_two)
        
        print("Converted to",currency.get_currency_name(currency_set,length,to_curr),
        currency.get_currency_code(currency_set,length,to_curr)," :",round(converted,2))

def main():
    interface = UserInterface()
    interface.questions()


if __name__ == "__main__":
    main()