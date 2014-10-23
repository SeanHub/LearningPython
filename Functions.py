print("------ BANK OF AMERICA III: Banking with a Vengence ------")
balances = [120.83, 600.80, 100568.10]
# define/create a function
def taxCustomer(index) :
    tax = 100.50
    balances[index] -= tax
taxCustomer(0)
print(round(balances[0], 2))
input("Press Enter to quit...")
