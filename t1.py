def test():
    fin = open('words.txt')
    count = 0
    word = fin.readline()
    x = len(word)
    for i in word:
        if i == ' ':
            count = count + 1
    y = x - count
    if y >= 20:
        print word
        return word
    else:
        print 'words have only', y, 'char'
test()
