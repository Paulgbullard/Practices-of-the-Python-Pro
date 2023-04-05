#Translate a series of words into pig latin.
#If the word begins with a vowel (a,e,i,o,u), add "way" to the end of the word. Air = Airway, Eat = Eatway
#If the word begins with a consonent, take the first letter, move to the end of the word, and add "ay". Python = ythonpay,
#computer = omputercay

def pl_sentence(sentence):
    output = []
    for word in str.split(sentence):
        if word[0].lower() in 'aeiou':
            output.append(f'{word.lower()}way')
        else:
            output.append(f"{word[1:len(word)]}{word[0].lower()}ay")
    return ' '.join(output)

print(pl_sentence('This is A test translation'))