FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    array = FIRST_TEN + SECOND_TEN  #concatena as listas de 1 a 19
    array.insert(0,'')      #adiciona vazio a posição 0

    if number < 20:  #se o numero e menor que vinte ele esta na lista dos arrays
        num = array[number]

    elif 19 < number < 100:
        num = OTHER_TENS[int(str(number)[0])-2]

        if int(str(number)[1]) > 0:
            num += ' ' + array[int(str(number)[1])]

    else:
        num = array[int(str(number)[0])] + ' ' + HUNDRED

        if 9 < int(str(number)[1:]) < 20: #se os dois ultimos digitos do numero são menores que vinte
            num += ' ' + array[int(str(number)[1])+11] #entao o numero esta dentro do array

        else:
            if int(str(number)[1]) > 0:
                num += ' ' + OTHER_TENS[int(str(number)[1])-2]

            if 0 < int(str(number)[2]) < 10:
                num += ' ' + array[int(str(number)[2])]

    #replace this for solution
    return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four'
    assert checkio(133) == 'one hundred thirty three'
    assert checkio(12) == 'twelve'
    assert checkio(101) == 'one hundred one'
    assert checkio(212) == 'two hundred twelve'
    assert checkio(40) == 'forty'
    assert not checkio(212).endswith(' ')
