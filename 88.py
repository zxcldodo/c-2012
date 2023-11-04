wordz = ["car","dog","book","game","window","grandfather","grandmother","grandbanan"]
word = random.choice(wordz)
guessed_leters = []
max_att = 10
while True:
    guessed_word = ""
    for leters in word:
        if leters in guessed_leters:
            guessed_word += leters
        else:
            guessed_word += "_"
    print("guessed word:" + guessed_word)
    if guessed_word == word:
        print("14/88! word is:") + word
        break
    guess = input("print letter:").lower()
    if guess in guessed_leters:
        print("daunnnnnnnnnnnnnnnn")
    elif guess in word:
        print("good")
        guessed_leters.append(guess)
    else:
        print("daun ti sin shalavu")
        guessed_leters.append(guess)
        max_att -= 1
    if max_att == 0:
        print("you lose your father!word was") + word
        break
