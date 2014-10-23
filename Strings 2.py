print("------ BANK OF AMERICA (but not really) ------")
# store some strings in a variable
accInfo = (input("What's your account number: "),
           input("What's your account password: "))
# print statements containing any two strings we specify
login = "Welcome account %s, you're password is %s."
# feed login the strings from accountInformation
information = login % accInfo
print(information)
print("In the statement above, type in a search to find when a string occurs.")
# finds first occurence of string, + 1 to defeat zero-based indexing
print(information.find(input("String: ")) + 1)
input("Press Enter to quit...")
