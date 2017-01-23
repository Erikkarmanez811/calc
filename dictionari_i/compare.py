def compare(str1,str2):
    for i in range(min(len(str1),len(str2))):
        if ord(str1[i]) < ord(str2[i]):
            return True
        elif ord(str1[i]) > ord(str2[i]):
            return False
    return len(str1) < len(str2)
        
