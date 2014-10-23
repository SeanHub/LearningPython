print("------ BANK OF AMERICA 4: A Good Day to Bank Hard ------")
# this function allows for multiple values, creates a tuple
def employeeNames(*names) :
    print(names)
employeeNames('Austin', 'Sean', 'Jonny')
# creates a dictionary instead of tuple
def employeeAccounts(**account) :
    print(account)
employeeAccounts(austin = 500, sean = 300, jonny = 150)
input("Press Enter to quit...")
