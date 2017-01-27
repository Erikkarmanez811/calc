import search
import compare

def w_compare(i):
    return lambda word1, word2: compare.compare(word1[i],word2[i])
    
def lex(aR):
    ar = list(aR)
    token = []
    tokens = []
    meta_tokens = []
    for i in ar:
        if i == ' ':
            tt = ''
            for ui in token:
                tt += ui
            tokens.append(tt)
            token = []
        if i == ',':
            meta_tokens.append(tokens)
            tokens = []
        else:
            token.append(i)
    return meta_tokens

def d_load():
    words_r = (open('words.txt','r')).read()
    words = lex(words_r)
    
    return words

def u_load(words):
    
    words_tu = ''
    
    for word in words:
        words_tu  +=  word[0] + ' ' + word[1] + ' ,'
        
    words_w = open('words.txt','w')
    words_w.write(words_tu)
    words_w.close()
    
    return True

    
def add(word):
    
    words = d_load()
    
    index = search.search(words, word, w_compare(0))
    
    if index[0]:
        return False
    
    words.insert(index[1] ,word)
    
    return u_load(words)
    
    
def find_word(word,i):
    
    words = d_load()
    
    index = search.search(words, word, w_compare(i))
    
    if index[0]:
        return [index[0], words[index[1]]]
    
    return [False, ['','']]
    
def def_lang(word):
    word_u = ord(word[0])
    if word_u >= 97 and word_u <= 122:
        return 'eng'
    if word_u >= 1072 and word_u <= 1103:
        return 'rus'
    return 'español'
while True:
    print('t or a')

    answer = input()

    if answer == 'a': 
        
        word = [input(),input()]
        
        if add(word):
            print('Your word has been successfully added')
        else:
            print('Your word has not been added')
        
        
       
    if answer == 't':
        word_tt = input()
        lang = def_lang(word_tt)
        i = 0
        if lang == 'rus':
            i = 1
        if lang == 'eng':
            i = 0
        
        
        found_word = find_word(word_tt,i)
        
        if found_word[0]:
            print(found_word[1][i])
        else:
            print('Your word is not in the dictionary')
            
        
