class Hangman():
	def __init__(self):
		print "Welcome to 'Hangman', are you ready to die?"
		print "(1)Yes, for I am already dead.\n(2)No, get me outta here!"
		user_choice_1 = raw_input("->")
		
		if user_choice_1 == '1':
			print "Loading nooses, murderers, rapists, thiefs, lunatics..."
			self.start_game()
		elif user_choice_1 == '2':
			print "Bye bye now..."
			exit()
		else:
			print "I'm sorry, I'm hard of hearing, could you repeat that?"
			self.__init__()

	def start_game(self):
		print "A crowd begins to gather, they can't wait to see some real"
		print "justice. There's just one thing, you aren't a real criminal."
		print "No, no. You're the wrong time, wrong place type. You may think"
		print "you're dead, but it's not like that at all. Yes, yes. You've"
		print "got a chance to live. All you've gotta do is guess the right"
		print "words and you can live to see another day. But don't get so"
		print "happy yet. If you make 6 wrong guess, YOU'RE TOAST! VAMANOS!"
		self.core_game()

	def core_game(self):
		guesses = 0
		letters_used = ""
		the_word = "pizza"
		progress = ["?", "?", "?", "?", "?"]
		
		while guesses < 6:
			guess = raw_input("Guess a letter ->")

			if guess in the_word and not in letters_used:
				print "As it turns out, your guess was RIGHT!"
				letters_used += "," + guess
				self.hangman_graphic(guesses)
				print "Progress: " + self.progress_updater(guess, the_word, progress)
				print "Letter used: " + letters_used
			elif guess not in the_word and not(in letters_used):
				guesses += 1
				print "Things aren't looking so good, that guess was WRONG!" 
				print "Oh man, that crowd is getting happy, I thought you"
				print "wanted to make them mad?"
				letters_used += "," + guess
				self.hangman_graphic(guesses)
				print "Progress: " + "".join(progress)
				print "Letter used: " + letters_used
			else:
				print "That's the wrong letter, you wanna be out here all day?"
				print "Try again!"



	def hangman_graphic(self, guesses):
		if guesses == 0:
			print "________      "
			print "|      |      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 1:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 2:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "
		elif guesses == 3:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "
		elif guesses == 4:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "
		elif guesses == 5:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "
		else:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			print "The noose tightens around your neck, and you feel the"
			print "sudden urge to urinate."
			print "GAME OVER!"
			self.__init__()

	def progress_updater(self, guess, the_word, progress):
		i = 0
		while i < len(the_word):
			if guess == the_word[i]:
				progress[i] = guess
				i += 1
			else:
				i += 1

		return "".join(progress)

game = Hangman()
