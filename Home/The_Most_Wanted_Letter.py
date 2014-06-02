#coding: utf-8

import string

def checkio(text):

    '''
        **melhor resolução**

        text = text.lower()
        return max(string.ascii_lowercase, key=text.count)

        text = ''.join(i for i in text.lower() if i.isalpha())
        return max(set(text), key=text.count)

    '''

    text = text.lower()
    for i in ['.', '!', '?', '*', '#', ' ','-',',']:
        if i in text:
            text = text.replace(i,'')

    if text.isalpha() == False:
        for i in range(10):
            text = text.replace(str(i),'')

    text = text.replace('',' ').rsplit()

    text.sort()

    cont=0
    tam = 0
    letter = 0
    while cont < len(text):
        if text.count(text[cont]) > tam:
            tam = text.count(text[cont])
            letter = text[cont]
        cont += 1

    #replace this for solution
    return letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo000000000!!!!") == "a"
    assert checkio("abe") == "a"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a"
    print("The local tests are done.")
