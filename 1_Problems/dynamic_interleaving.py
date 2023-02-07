def isInterLeavgin(str1,str2,str3):
    if str1 =="" and str2=="" and str3=="":
        return True
    elif len(str1)+len(str2) != len(str3):
        return False
    elif len(str1)==0 and str2 == str3:
        return True
    elif len(str2)==0 and str1 == str3:
        return True
    else:
        ans1 = False
        ans2 = False
#        print(f"str1 = {str1}, str2 = {str2},str3 = {str3}")
        if str1[0] == str3[0]: 
            ans1 = isInterLeavgin(str1[1:], str2, str3[1:])
        elif str2[0] == str3[0]:
            ans2 = isInterLeavgin(str1, str2[1:], str3[1:])

    return ans1 or ans2


if __name__ == "__main__" :
    word1 = "yz"
    word2 = "abcd"
    word3 = "bayczd"
    res = isInterLeavgin(word1,word2,word3)
    print(res)