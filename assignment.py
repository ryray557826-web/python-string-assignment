while True:
    print("""
    1. Reverse the sentence
    2. Count vowels
    3. Check palindrome
    4. Find and replace a word
    5. Format (title case)
    6. Split into words
    7. Word frequency counter
    8. Swap case
    9. Exit
    """)

    choice = int(input("Choice here: "))

    if choice == 1:
        phrase = input("Enter a sentence/word/phrase: ")
        print("Reversed:", phrase[::-1])

    elif choice == 2:
        phrase = input("Enter a sentence/word/phrase: ")
        vowels = "aeiouAEIOU"
        count = sum(1 for ch in phrase if ch in vowels)
        print("Number of vowels:", count)
    elif choice == 3:
        phrase = input("Enter a sentence/word/phrase: ")
        reversed = phrase[::-1]
        print("Reversed:", reversed)
        if phrase == reversed:
            print("The word is a palindrome.")
        elif phrase != reversed:
            print("The word is not a palindrome.")
    elif choice == 4:
        phrase = input("Enter a sentence/word/phrase: ")
        replace= input("Word to replace: ")
        replacment= input("Word to replace with: ")
        print("After replacing:"+phrase.replace(replace, replacment))
    elif choice == 5:
        phrase = input("Enter a sentence/word/phrase: ")

        small_words = {"and", "or", "the", "of", "in", "on", "at", "to", "a", "an"}
        words = phrase.lower().split()
        result = []
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word not in small_words:
                result.append(word.capitalize())
            else:
                result.append(word)  #
        fphrase = " ".join(result)

        print("After Formatting (Formal Title Case):", fphrase)
    elif choice == 6:
        phrase = input("Enter a sentence/word/phrase: ")
        sphrase = phrase.split()
        print("Split words:", sphrase)
    elif choice == 7:
        phrase = input("Enter a sentence/word/phrase: ")
        split = phrase.split()
        freq={}
        for word in split:
            freq[word] = freq.get(word, 0) + 1
        print("Frequencies:")
        for word, freq in freq.items():
                print(f"Word: {word}, freq: {freq}")
    elif choice == 8:
        phrase = input("Enter a sentence/word/phrase: ")
        print("Swap cased words:", phrase.swapcase())
    elif choice == 9:
        print("Exiting program...")
        break
