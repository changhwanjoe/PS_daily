def spin_words(sentence):
    splitted = sentence.split()
    s = []
    new = ""
    for word in splitted:
        if len(word)>=5:
            word = word[::-1]
        s.append(word)
    result = " ".join(s)
    return result
    # Your code goes here
    #return None