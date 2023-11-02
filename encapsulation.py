class bankaccount:
    def __init__(self,account_number,balance):
        self.accountnumber=account_number
        self.balance=balance

    def getbalance(self):
        return self.balance
account1=bankaccount("12345","1000")
print(account1.accountnumber)
print(account1.getbalance())

