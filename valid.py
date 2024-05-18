# Uses Luhn Algorithm to check the validity of a
# 16-digit card number
# Author: Adith Venkatesh

# checkCard method where the card validity is checked
def checkCard(cardNumber):
    reverse = cardNumber[::-1]
    everyOther = reverse[1::2]
    print(everyOther)
    every = cardNumber[1::2]
    print(every)
    final_string = ""
    for x in everyOther:
        number = int(x) * 2
        if number > 9:
            num_str = str(number)
            sum = int(num_str[0]) + int(num_str[1])
            final_string += str(sum)
            
        else:
            final_string += str(number)
    finalSum = 0
    print(final_string)

    for x in final_string:
        finalSum += int(x)
       
    for x in every:
        finalSum += int(x)
        
    print(finalSum)
    if finalSum % 10 == 0:
        return True
    
    else:
        return False   

#User input 
cardNumber = input("Enter a 16-digit card number: ")

if len(cardNumber) != 16:
    print("You did not enter a 16 digit number.... try again")
    quit()
    
else:
    if checkCard(cardNumber):
        print("Valid Card Number!")
    
    else:
        print("Invalid Card Number :(")
