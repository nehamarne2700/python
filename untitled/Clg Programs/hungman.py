import random as rd

vocabulary = {1: "Shielded", 2: "Template", 3: "Ethics", 4: "Abruptly", 5: "Bookworm", 6: "Haiku", 7: "Memento", 8: "Syndrome"}

meaning = {1: "protected from danger",
           2: "something that establishes or serves as a pattern",
           3: "deciding what is morally right and wrong in computing -- and in life",
           4: "suddenly and unexpectedly",
           5: "a person who enjoys reading",
           6: "a Japanese poem of seventeen syllables, in three lines of five, seven, and five, traditionally evoking images of the natural world.",
           7: "an object kept as a reminder of a person or event",
           8: "a group of symptoms which consistently occur together, or a condition characterized by a set of associated symptoms"}

hangman_steps_starting = (10, 8, 7, 6, 5, 4, 1)

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

choice = rd.randint(1, 8)

word = vocabulary[choice].upper()

temp_word = list(word)

guess_word = list()

for i in range(0, len(word)):
    guess_word.append("_")

print("*" * 60)
print("\t\t\t\tThis Is HANGMAN game")
print("*" * 60)

print("\t\tword to guess : " + "_ " * len(word))
print()
print("Meaning of word : {}".format(meaning[choice]))

wrong_count = 0

while wrong_count < 6 and '_' in guess_word:
    letter = input("\nGuess a letter for word : ").upper()

    if len(letter) > 1 or len(letter) < 1:
        print("Please enter a single letter only!!!")
        continue

    if letter in temp_word:
        cnt = temp_word.count(letter)
        for i in range(0, cnt):
            index = temp_word.index(letter)
            guess_word[index] = temp_word[index]
            temp_word[index] = '*'
        final_word = ' '.join(
            guess_word)
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
