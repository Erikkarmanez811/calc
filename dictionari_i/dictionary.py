import merge_sort
def lex(aR):
    ar = list(aR)
    words = []
    token = ''
    for i in ar:
        if i == ' ':
            
            if token != '':
                words.append(token)
                token = ''

            
            
        else:
            token += i
    return words
while True:
    print('a or t')
    cho = input()
    if cho == 'a':
        word = input() + ' '
        word_t = input() + ','
        words_r = (open('words.txt','r')).read()
        words_eng = 
        words_ru = 
        Words = open('words.txt','w')
        Words.write(words_r)
        Words.write(word)
        Words.write(word_t)
        Words.close()
    if cho == 't':
        word_t = input()
        words = lex(open('words.txt','r').read())
        word_i = words.index(word_t)
        if word_i % 2 == 0:
            print(words[word_i + 1])
        else:
            print(words[word_i - 1])
            
            
        
