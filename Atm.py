from tempfile import NamedTemporaryFile


class Atm(object):
    def __init__(self,name,cardNumber,pin,money,):
        self.name=name
        self.cardNumber=cardNumber
        self.pin=pin
        self.money=money

    def checkBalance(self):
        print("Your current balance amount is", self.money)

    def cashDeposit(self):
        deposit=int(input("Please enter the amount that you want to deposit:"))
        self.money=deposit+self.money
        print("Your current balance amount is",(self.money))

    def cashWithdraw(self):
        withdraw=int(input("Please enter the amount that you want to withdraw:"))
        self.money=self.money-withdraw
        print("Your current balance amount is",(self.money))

user1=Atm("Dan",99999999,0000,696969)
user1.checkBalance()
user1.cashDeposit()
user1.cashWithdraw()