import random


word_list = ["aardvark", "baboon", "camel"]
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

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #using a for loop to check & compare each letter of the chosen word and the guessed word
    print(display)

    if "_" not in display:
        End_of_game = True
        print("Jeet gya bsdk")