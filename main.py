import random

wins = 0
losts = 0


def play():
    global wins, losts

    answer = random.choice(["python", "java", "swift", "javascript"])

    word = '-' * len(answer)
    attempts = 8
    was = set()
    while attempts > 0 and word.count('-') != 0:
        print()
        print(word)
        user_letter = input("Input a letter: > ")

        if len(user_letter) != 1:
            print("Please, input a single letter.")
            continue
        elif not user_letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        elif user_letter in was:
            print("You've already guessed this letter.")
            continue
        else:
            was.add(user_letter)

        ex = False
        open = False
        for j in range(len(word)):
            if answer[j] == user_letter and word[j] != user_letter:
                word = word[0:j] + user_letter + word[j + 1:]
                ex = True
            elif answer[j] == user_letter:
                print("No improvements.")
                attempts -= 1
                ex = True
                break
        if not ex:
            print("That letter doesn't appear in the word.")
            attempts -= 1

    print()
    if word == answer:
        print(word)
        print(f"You guessed the word {answer}!")
        print("You survived!")
        wins += 1
    else:
        print("You lost!")
        losts += 1


print("H A N G M A N")
while True:
    deal = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if deal == "play":
        play()
    elif deal == "results":
        print(f"You won: {wins} times")
        print(f"You lost: {losts} times")
    elif deal == "exit":
        exit()
