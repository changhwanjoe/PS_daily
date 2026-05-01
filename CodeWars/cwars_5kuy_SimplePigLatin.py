def pig_it(text):
    result = []
    for letter in text.split():
        if letter.isalpha():
            letter += letter[0] 
            result.append(letter[1:] + "ay")
        else:
            result.append(letter)
    return (" ").join(result)
    #your code here

'''clever code
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
 
'''