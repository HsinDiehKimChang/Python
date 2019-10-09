# 20190122
# Python script week3
# Written by Hsin-Dieh Chang

# Ask user to type a sentence
print("Please type a sentence")

# store this sentence to variable
sentence = input()

# determine the number of characters in the sentence
sentenceLengh = len(sentence)

# Ask user to type a number
print("Please insert a number between 1 and", sentenceLengh)

# store this number and casting to number
userNumber = int(input())

# use while loop to let user get an inifinite attempts to guest
# if not right then try again
while (userNumber != sentenceLengh):
        # elif statement
    # if userNumber is less than sentenceLengh
    if (userNumber < sentenceLengh):
        # tell users that the number was less than the number
        print("The number you provided", userNumber,
              "was less than the number of characters in the sentence.")
    # if userNumber is greater than sentenceLengh
    elif (userNumber > sentenceLengh):
        # tell users that the number was greater than the number
        print("The number you provided", userNumber,
              "was greater than the number of characters in the sentence.")
    # if userNumber is equal to sentenceLengh
    elif (userNumber == sentenceLengh):
        # tell users that the number was equal to the number
        print("The number you provided", userNumber,
              "was equal to the number of characters in the sentence.")

        # ask users to insert another number
    print("Please insert another number again:")
    # re-store the variable
    userNumber = int(input())
# if number is right, then out of loop then print
print("The number you provided", userNumber,
      "was equal to the number of characters in the sentence.")
