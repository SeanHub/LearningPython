inLove = False
while inLove != True :
    love = input("Do you love me? ")
    if love == ("yes") :
        inLove = True
    else :
        inLove = False
        print("I need you to love me!")
print("Thank God :)")
print("Tell me three things you love about me...")
aspects = [input("I love your "), input("I love your "), input("I love your ")]
for aspect in aspects :
    print("You love my " + aspect)
input("Press Enter to quit...")
