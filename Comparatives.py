if int(input("Give me a number less than 8: ")) < 8 :
    print("Correct!")
if int(input("Give me a number less than or equal to 3: ")) <= 3 :
    print("Correct!")
if int(input("Give me a number greater than or equal to 600: ")) >= 600 :
    print("Correct!")
if int(input("Give me a number that is not 7: ")) != 7 :
    print("Correct!")
# is tests if they are the same object, == tests if they equal the same value
if int(input("Give me the number 7: ")) is 7 :
    print("Correct!")
# in doesn't work with type integer
if input("Give me a number which is in 902918: ") in "902918" :
    print("Correct!")
input("Press Enter to quit...")
