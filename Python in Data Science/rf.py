def countDog(word):
    lower_word = word.casefold()
    if "dog" in lower_word:
        counted_word = lower_word.count("dog")
        return counted_word
    else:
        return False

    
result = countDog('This dog runs faster than the other dog dude!')
print(result)