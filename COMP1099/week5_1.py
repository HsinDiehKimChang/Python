# 20190205
# Python script week5
# Written by Hsin-Dieh Chang
# 
#
import random

#
def function1(string,number):
	#x is the number of characters in the string passed into the function multiplied by the integer passed into the function.
	x=len(string)*number
	#for debug
	print("x=",x)
	#get the random number
	answer=random.randint(1,x)
	#testing purpose
	print("answer=",answer)
	


# ask the user for their first name
print("Please type your first name")
#get the variable
firstName=input()
# ask the user for their last name
print("Please type your last name")
#get the variable
lastName=input()
# ask the user for a random string
print("Please type a random string")
#get the variable
userString=input()
# ask the user for an integer
print("Please type an integer")
#get the variable
userInteger=int(input())

#If the user passes in an integer of zero ask them for another integer until they provide an integer other than zero.
while userInteger==0:
	# ask the user for an integer
	print("Please type another integer")
	#get the variable
	userInteger=int(input())

#Print out the first and last name as a single string on one line.
print(firstName,lastName)

#Print out the users first name y  times,  on one line, where y is the integer captured from the user.
for i in range(userInteger):
	#Print out the users first name y  times
	print(firstName,end=' ')

#for comfortable to read add one more space	
print(' ')

#Print a countdown from 20 to 0 in increments of 2, with each number being printed on a separate line.
for j in range(20,-2,-2):
	#Print countdown
	#print("Print countdown:")
	#Print countdown
	print(j)

#Print the first and last name separated by three dashes (---).
print(firstName,lastName,sep='---')

#Print a random number from 1 to x, where x is the number of characters in the random string captured from the user multiplied by the integer captured from the user. (Utilize the function written in step 1 to accomplish this task.)
function1(userString,userInteger)
