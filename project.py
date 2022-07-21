import random
import os


def scorefilecreator():		#function that creates high score file if there is none

	try:
		scoreread = open("highscores.txt", "r")		#if the program is able to detect and read the highscore file
		scoreread.close()							#nothing will happen

	except:											#else it creates a file

		scorecreate = open("highscores.txt", "w")

		for i in range(10):							#creates 10 blank scores
			scorecreate.write("0" + "|" + "")
			scorecreate.write("\n")

		scorecreate.close()

def readscoresandstore():
	scorelist = []

	scoreread = open("highscores.txt", "r")

	for line in scoreread:
		highscore = line[:-1].split("|")		#stores each line of score (player and corresponding score) as a list
		highscore[0] = int(highscore[0])		#typecasts the first element which is the score as an integer
		scorelist.append(highscore)

	scoreread.close()
	return scorelist

def highscores():

	try:
		scorelist = readscoresandstore()

		print()
		print("HIGHSCORES")
		print()

		print("Player" + "         " + "Score")
		print()

		for scores in scorelist:
			print(scores[1], " "*(14-len(scores[1])), scores[0])		#prints the player name followed by a space that is multiplied
																		#to 14 - the length of the name in order to have constant spacing
		print()															#between the name and scores all throughout
		choice = input("Press Enter to Return to the Main Menu: ")

	except:
		scorefilecreator()

		scorelist = readscoresandstore()

		print()
		print("Highscores")
		print()

		print("Player" + "         " + "Score")
		print()

		for scores in scorelist:
			print(scores[1], " "*(14-len(scores[1])), scores[0])

		print()
		choice = input("Press Enter to Return to the Main Menu: ")

def calculatescore(errors, turnscorebonus):
	if turnscorebonus < 0:						#Sets turnscorebonus to 0 if it is negative since it should not deduct points
		turnscorebonus = 0
	if difficulty == 1:							#A difficulty of 1 means it is easy, 2 means medium, and 3 means hard
		return 50*(6-errors)+turnscorebonus		#each difficulty has a different score multiplier (50, 75, and 100)
	elif difficulty == 2:						#this is then multiplied to (6-errors), therefore the less errors the user made the
		return 75*(6-errors)+turnscorebonus		#the higher their score, lastly this is added to turnscorebonus (refer to meaning 
	elif difficulty == 3:						#in game function)
		return 100*(6-errors)+turnscorebonus

def highscoresaver(playerscore):				#takes the player's score which is a list containing the score and initially a 
												#blank player name
	highscoreproceed = True 				#we assume that the player gets a new high score and if in reality he/she did not,
											#a condition below will check it and set this value to False
	scorelist = readscoresandstore()

	scorelist.append(playerscore)

	scorelist.sort()						# -|Arranges the highscores stored in the list in
	scorelist.reverse()						# -|greatest to least order

	if scorelist.index(playerscore) < 10:	#in other words the score is in the top 10
		scorelist.pop(-1)

	else:									#this means that the score is ranked 11
		if playerscore[0] == scorelist[-2][0]:		#checks if the player's score is equal to the rank 10's score
			scorelist.pop(-2)						#pops the rank 10's score to make space for the new player's high score
		else:								#The player's score is lower than the lowest high score
			highscoreproceed = False		#therefore, the player did not achieve a highscore
			
	if highscoreproceed == True:		#Executes if the player got a highscore
		print()
		print("You just got a highscore!")
		print()
		print("Player" + "         " + "Score")
		print()

		for scores in scorelist:
			print(scores[1], " "*(14-len(scores[1])), scores[0])

		while True:

			print()
			name = input("Please Enter your name here: ")
			print()

			if len(name) > 14:
				print("Name too long (Maximum of 14 characters). Try Again")

			else:
				break

		scorelist[scorelist.index(playerscore)][1] = name

		print("HIGHSCORES")
		print()
		print("Player" + "         " + "Score")
		print()

		for scores in scorelist:
			print(scores[1], " "*(14-len(scores[1])), scores[0])
		print()

		scoresave = open("highscores.txt", "w")
		for highscore in scorelist:
			scoresave.write(str(highscore[0]) + "|" + highscore[1])		#Since the player's highscore is in the scorelist
			scoresave.write("\n")										#it gets saved into a file

		scoresave.close()

def check(letter, word, wordwblanks):

	string = ""

	if letter in word.lower():			#checks first if the letter guessed is in the word
		for x in word:					#iterates through the "word" string
			if letter == x.lower():		
				string += x + " "		#adds the guessed letter to the string
			elif x in wordwblanks:
				string += x + " "		#adds the letter which has already been guessed correctly/revealed to the string
			else:
				string += "_ "			#adds _s for the unguessed letters to the string

		return string

	else:
		return False

def choosecategory():
	categorylist = []
	categoryhandle = open("categories.txt", "r")
	for line in categoryhandle:
		data = line[:-1].split("|")
		categorylist.append(data)

	while True:
		print()
		print("Pick a category:")
		for categories in categorylist:
			print(categories[0])
		print()

		category = int(input("Enter the number of your choice: "))

		if category >= 1 and category <= len(categorylist)-1:
			while True:
				print()
				print("You have selected the", categorylist[category-1][0][4:], "category")
				print("Pick a difficulty: ")
				print("[1] Easy")
				print("[2] Medium")
				print("[3] Hard")
				print("[4] Go back and repick category")
				print()

				global difficulty

				difficulty = int(input("Enter the number of your choice: "))

				if difficulty == 1:
					return categorylist[category-1][1]

				elif difficulty == 2:
					return categorylist[category-1][2]

				elif difficulty == 3:
					return categorylist[category-1][3]

				elif difficulty == 4:
					break

				else:
					print()
					print("Invalid choice, you may only enter 1, 2, or 3 as your choice.")
					print("Try again")

		elif category == len(categorylist):
			return False

		else:
			print()
			print("Invalid choice, you may only enter 1, 2, 3, 4, or 5 as your choice.")
			print("Try again")
			print()



def retrievewords(category):
	retrievehandle = open(category, "r")

	for line in retrievehandle:
		wordlist = line.split("|")

	return wordlist

	retrievehandle.close()


def hangmanillus(errors):
	if errors == 0:
		print("  +---+")
		print("  |   |")
		print("      |")
		print("      |")
		print("      |")
		print("      |")
		print("=========")
		print()

	elif errors == 1:
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print("      |")
		print("      |")
		print("      |")
		print("=========")
		print()

	elif errors == 2:
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print("  |   |")
		print("      |")
		print("      |")
		print("=========")
		print()

	elif errors == 3:
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|   |")
		print("      |")
		print("      |")
		print("=========")
		print()

	elif errors == 4:
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|\  |")
		print("      |")
		print("      |")
		print("=========")
		print()

	elif errors == 5:
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|\  |")
		print(" /    |")
		print("      |")
		print("=========")
		print()

	elif errors == 6:
		print("  +---+")
		print("  |   |")
		print("  O   |")
		print(" /|\  |")
		print(" / \  |")
		print("      |")
		print("=========")
		print()



def game(category):
	os.system("cls")
	wordwblanks = ""
	errors = 0
	Win = True
	misses = []
	counter = 0
	proceed = True
	turnscorebonus = 35

	words = retrievewords(category)

	while True:						#a loop to avoid the repetition of previous played words
		n = random.randint(0,len(words)-1)
		word = words[n]

		if counter == len(words):	#this means that the counter has reached the number of possible words under the category
			proceed = False			#and difficulty
			break					#proceed = False means the game part won't run

		if word in prevwordslist:
			counter += 1			#adds 1 to counter everytime a word is picked (from randomizing) that has already been played
			continue
		else:
			prevwordslist.append(word)		#adds the word to the list of words that have already been played
			break

	if proceed == True:				#only runs if there are remaining words to be played
		print("Guess the word by entering only a letter or the whole word itself")

		print()

		print("The word is: ")

		for letters in word:
			if letters == " ":
				wordwblanks += "   "
			else:
				wordwblanks += "_ "

		print(wordwblanks)
		print()

		while "_" in wordwblanks:
			print()
			print(wordwblanks)
			print()
			hangmanillus(errors)
			print("Lives:", 6-errors)

			print("Misses: ", end="")
			for x in misses:
				print(x + ", ", end="")
			print()
			print()

			guess = input("Guess: ")
			guess = guess.lower()

			if len(guess) > 1 and len(guess) < len(word) or len(guess) > len(word) or guess.isdigit() == True:
				print()
				print("Invalid guess, try again.")
				print()

			elif guess in wordwblanks or guess in misses:
				print()
				print("You have already made that guess, try again.")
				print()

			elif len(guess) == len(word.lower()):
				if guess == word.lower():
					break
				else:
					misses.append(guess)

					errors+=1
					if errors > 5:
						Win = False
						print()
						hangmanillus(errors)
						break

			elif check(guess, word, wordwblanks) != False:
				turnscorebonus -= 5
				wordwblanks = check(guess, word, wordwblanks)

			else:
				turnscorebonus -= 5
				if errors == 0:
					misses.append(guess) 
				else:
					misses.append(guess)

				errors += 1
				if errors > 5:
					Win = False
					print()
					hangmanillus(errors)
					break

			print()

		if Win == True:
			print()
			print("Congratulations! You have successfully guessed the word:", word)
			print("and won the game.")

			print()
			score = calculatescore(errors, turnscorebonus)
			print("Your score:", score)

			highscoresaver([score, ""])

			againormenu(category)

		else:
			print()
			print("Game Over. You lose")
			print("The word was:", word)

			againormenu(category)

	else:		#Runs if there are no more words available to play under the category and didfficulty
		print("You have guessed all the possible words under this category and difficulty.")
		print("You may try other categories and difficulties instead or exit and relaunch")
		print("this program to replay this category and difficulty")
		print()
		choice = input("Press Enter to proceed and go back to the main menu:")

def againormenu(category):
	proceed = True
	while proceed == True:

		print()
		print("[1] Play Again using the same category and difficulty")
		print("[2] Play Again and choose a different category and/or difficulty")
		print("[3] Return to Main Menu")
		print()

		choice = input("Enter the number of your choice: ")
		print()

		if choice == "1":
			game(category)
			break

		elif choice == "2":
			while True:
				category = choosecategory()

				if category == False:
					proceed = False
					break
				else:
					game(category)
					break

		elif choice == "3":
			proceed = False
			break

		else:
			print()
			print("Invalid choice, you may only enter 1, 2 or 3 as your choice.")
			print("Try again")


#Program starts running here

prevwordslist = []

scorefilecreator()

while True:
	print()
	print("-----------------")
	print(":    HANGMAN    :")
	print("-----------------")

	print()
	print()

	print("  +---+")
	print("  |   |")
	print("  O   |")
	print(" /|\  |")
	print(" / \  |")
	print("      |")
	print("=========")

	print()
	print()

	print("[1] Play a game")
	print("[2] High Scores")
	print("[3] Exit")

	print()

	choice = input("Enter the number of your choice: ")
	

	if choice == "1":
		while True:
			category = choosecategory()
			if category == False:
				break
			else:
				game(category)
				break


	elif choice == "2":
		highscores()

	elif choice == "3":
		print()
		print("Thank you for playing. The game will now exit...")
		print()
		break

	else:
		print()
		print("Invalid choice, you may only enter 1, 2, or 3 as your choice.")
		print("Try again")






