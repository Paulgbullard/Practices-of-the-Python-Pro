#Sorting a string
#Take a single string, and return a string that contains the same characters but sorted from lowest unicode character to highest
#Additional - take a sentence, and sort each string within that sentence alphabetically,a nd print with commas between

def string_sort(string):
    return ''.join(sorted(string))

print(string_sort('tarantula'))

def sentence_word_sort(string):
    sorted_words = []
    split_string = str.split(string)
    for word in split_string:
        sorted_words.append(''.join(sorted(word)))
    sorted_words_string = ', '.join(sorted_words)
    return sorted_words_string


print(sentence_word_sort('tom dick harry'))