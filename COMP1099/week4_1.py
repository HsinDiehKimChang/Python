# 20190129
# Python script week4
# Written by Hsin-Dieh Chang
# 
# import moudules

import random
#computer selectd a random number between 1 and 500
answer=random.randint(1,500)

####for convient to check code
print("answer is: ",answer)

#Four rounds
for i in range(4):
	#Print which round
	print("This is ",i+1, "round")

	#Guesses times
	guesses=1
	#Print which guesses
	print("This is ",guesses, "guesses")

	#Ask user to input a number
	print("Please guess a number between 1 and 500")
		
	#capture number from keyboard and casting to int
	userGuess=int(input())

	while (guesses<3):
		if (answer < userGuess):
			# tell users that the number was greater than the random number
			print("The number you provided", userGuess,"was greater than the number.")
			# tell users how many guesses are left and the round they in
			print("You remain ",3-guesses," in",i+1,"round")
		elif (answer > userGuess):
			# tell users that the number was less than the random number
			print("The number you provided", userGuess,"was less than the number.")
			# tell users how many guesses are left and the round they in
			print("You remain ",3-guesses," in",i+1,"round")
		else:
			# break this condition
			break

		#Add guesses times
		guesses=guesses+1



		print("This is ",guesses, "guesses")
		#Ask user to input another number
		print("Please guess another number between 1 and 500")
		#capture number from keyboard and casting to int
		userGuess=int(input())

	#if user got it
	if(answer==userGuess):
		# tell users that the number was equal to the randomnumber
		print("Congratulated! You got it! The number is ",answer)
		# tell users how many guesses are left and the round they in
		print("You used ",i+1," rounds and" ,i*3+guesses,"trials")
		# break guesses
		break
		
#Not guess
if(answer!=userGuess):		
	#Not guess
	print("Answer is: ",answer,"and you used ",i+1," rounds and" ,i*3+guesses,"trials")
