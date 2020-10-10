class UserInterface(object):
    def questions(self):
        money = input("Enter money amount:")
        from_currency = input("From currency:")
        to_currency = input("To currency:")
        print(money,from_currency,to_currency)

interface = UserInterface()
interface.questions()