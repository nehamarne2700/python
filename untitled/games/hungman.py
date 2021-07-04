import random as rd

choice = rd.randint(1, 8)  # randint() inbuilt function of the random module to generate random numbers bet given range

vocabulary = {1: "Awkward", 2: "Bagpipes", 3: "Banjo", 4: "Fervid", 5: "Jukebox", 6: "Kiosk", 7: "Memento", 8: "Zombie"}

meaning = {1: "causing or feeling uneasy embarrassment or inconvenience",
           2: "a musical instrument with reed pipes that are sounded by the pressure of wind emitted from a bag squeezed by the player's arm",
           3: "a stringed instrument of the guitar family, with a round open-backed soundbox of parchment stretched over a metal hoop.",
           4: "intensely enthusiastic or passionate, especially to an excessive degree",
           5: "a machine that automatically plays a selected musical recording when a coin is inserted",
           6: "a small open-fronted hut or cubicle from which newspapers, refreshments, tickets, etc. are sold",
           7: "an object kept as a reminder of a person or event",
           8: "a person who is or appears lifeless, apathetic, or completely unresponsive to their surroundings."}

hangman_steps_starting = (10, 8, 7, 6, 5, 4, 1)  # steps from hangman dic to build hangman for every wrong attempt

hangman = {1: "         __ __ __ ",
           2: "        |        |",
           3: "        |        |",
           4: "        O        |",
           5: "      \_|_/      |",
           6: "        |        |",
           7: "      _/ \_      |",
           8: "                 |",
           9: "             ____|____",
           10: " "}

word = vocabulary[choice].upper()  # random word from vocabulary converted to uppercase

temp_word = list(word)  # returns word as a list

guess_word = list()  # empty list is created

for i in range(0, len(word)):
    guess_word.append("_")

print("=" * 60)
print("\t\t\t\tWelcome to HANGMAN game")
print("=" * 60)

print("\t\tword to guess : " + "_ " * len(word))
print()
print("Meaning of word : {}".format(meaning[choice]))
# format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly bracets

wrong_count = 0

while wrong_count < 6 and '_' in guess_word:
    letter = input("\nGuess a letter for word : ").upper()

    if len(letter) > 1 or len(letter) < 1:
        print("Please enter a single letter only!!!")
        continue

    if letter in temp_word:
        cnt = temp_word.count(letter)  # count() method returns the number of elements with the specified value.
        for i in range(0, cnt):
            index = temp_word.index(letter)  # index() method returns the index of the given element in the list.
            guess_word[index] = temp_word[index]  # place the guess letter in guess word
            temp_word[index] = '*'
        final_word = ' '.join(
            guess_word)  # join method returns a string whr string elements of para have been joined by str separator
        print(final_word)

    else:
        wrong_count += 1
        if wrong_count == 6:
            print("Sorry game over, you failed to guess it correctly!! The man is dead now.....")
            print("correct word was : ", word)

    print()
    for step in range(hangman_steps_starting[wrong_count], 10):
        print(hangman[step])

if '_' not in guess_word:
    print("Congratulations! you guessed the word correctly ")
