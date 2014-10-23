print("------ BANK OF AMERICA 2: Bank Harder ------")
# create a dictionary (key : value)
accounts = {'001':'£120.00', '002':'£10,000.00', '003':'£5742.14'}
# key lookup
print("Account balance: " + accounts[input("Your account number: ")])
# is the given string present in the dictionary
print(input("Enter an account number to check if it's present on our system: "
            ) in accounts)
input("Press Enter to quit...")
