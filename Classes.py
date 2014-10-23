class Account :
    """Represents a bank account."""
    tier = 'master'
    # __init__ is run at object creation, ala constructor 
    def __init__(self, accNo, accBalance) :
        self.no = accNo
        self.balance = accBalance
    def displayBalance(self) :
        return self.balance
    def displayTier(self) :
        return self.tier
    def taxAccount(self) :
        tax = 102.04
        self.balance -= tax

class Insurance :
    policy = 'master'
    def displayFee(self) :
        if self.policy == 'extra' :
            print("Insurance Policy Fee: £1781.90")

# a child class, using multiple inheritence
class BusinessAccount(Account, Insurance) :
    # overriding
    tier = 'business'
    policy = 'extra'

print("------ BANK ------")
account = Account('001', 431.40)
print(account.balance)
account.taxAccount()
print(round(account.balance, 2))
print(account.displayBalance())
print("")
print(account.displayTier())
businessAccount = BusinessAccount('002', 10928.21)
print(businessAccount.displayTier())
businessAccount.displayFee()
input("Press Enter to quit...")
