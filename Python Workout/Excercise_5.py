#Convert a word to pig latin
#If the word begins with a vowel (a,e,i,o,u), add "way" to the end of the word. Air = Airway, Eat = Eatway
#If the word begins with a consonent, take the first letter, move to the end of the word, and add "ay". Python = ythonpay,
#computer = omputercay

def pig_latin(word):
    if word[0].lower() in 'aeiou':
        return f"{word.lower()}way"
    return f"{word[1:len(word)]}{word[0].lower()}ay"

print(pig_latin('Python'))