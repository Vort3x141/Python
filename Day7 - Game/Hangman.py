import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

#Choosing a random word from the list
#choosen word count 
display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)
#append _ in the empty list which is equal to the length of the choosen word. 
End_of_game = False

while not End_of_game:
    guess = input("Guess a letter: ").lower()
    #inputing a letter and converting it into a lower case

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you loose a life")
        lives -=1
        if lives == 0:
            End_of_game = True
            print("You loose")
    
    #using a for loop to check & compare each letter of the chosen word and the guessed word
    print(display)

    if "_" not in display:
        End_of_game = True
        print("You win")

    print(hangman_art.stages[lives])
        