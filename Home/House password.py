#coding: utf-8

def checkio(data):

    if len(data)<10:
        return False
    if data.islower():
        return False
    if data.isupper():
        return False
    if data.isdigit():
        return False
    else:
        for i in ['1','2','3','4','5','6','7','8','9']:
            if i in data:
                return True
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False
    assert checkio('bAse730onE4') == True
    assert checkio('asasasasasasasaas') == False
    assert checkio('QWERTYqwerty') == False
    assert checkio('123456123456') == False
    assert checkio('QwErTy911poqqqq') == True
