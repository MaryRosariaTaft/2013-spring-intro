# dividing a number by 10 removes the ones digit
# a number's remainder after division by 10 is the ones digit

## These functions don't work if the digit being returned is "0"

#preconditions: n is an integer
def onesDigit(n):
    return n % 10

#preconditions: n is an integer >= 10
def tensDigit(n):
    return onesDigit(n / 10)

#preconditions: n is an integer >= 10
def lastTwoDigits(n):
    return n % 100
