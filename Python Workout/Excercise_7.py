#Create an Ubbi Dubbi translator
#Each vowel is prefaced with 'ub'. Milk = Mubilk, Program = Prubgrubam
#Take a single word, return a string translated according to the rules above
#Additional - deal with cases

def ubbi_dubbi(word):
    translation = []
    for letter in word:
        if letter.lower() in 'aeiou':
            translation.append(f"ub{letter}")
        else:
            translation.append(f"{letter}")
    
    return ''.join(translation)

print(ubbi_dubbi('Milk'))