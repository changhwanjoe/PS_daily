def min_change(word1,word2,count):
    if word1 == "":
        count+=len(word2)
        return count
    elif word2 == "":
        count+=len(word1)
        return count
    else:
        result = min(min_change(word1[1:],word2[1:],count])))

    word1 == word2 :
