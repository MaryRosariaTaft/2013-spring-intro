##Write a python script to convert a integer to a roman numeral.
##
##Here are the preconditions:
##
##  1. Read an integer in the range
##     from 1 up to 3999.
##  
##  2. Use the following symbols:
##
##      Symbol  Value
##     --------------
##     I         1
##     V         5
##     X        10
##     L        50
##     C       100
##     D       500
##     M      1000
##
##
##  3. Abide by these rules when constructing a roman numberal:
##    
##     * The symbols "I", "X", "C", and "M" can be repeated three times in
##     succession, but no more. "D", "L", and "V" can never be repeated.
##     * "I" can be subtracted from "V" and "X" only. "X" can be subtracted from 
##     "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L",
##     and "D" can never be subtracted 
##     * Only one small-value symbol may be subtracted from any large-value 
##     symbol.
##     * A number written in Arabic numerals can be broken into digits. 
##     For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman
##     numeral, each of the non-zero digits should be treated separately.
##     In the above example, 1,000 = M, 900 = CM, and 3 = III. Therefore,
##     1903 = MCMIII. 

def numToRoman(n):
    if n < 4:
        return "I" * n
    if n < 9:
        return "V" + "I" * (n - 5)
    if n = 9:
        return "IX"
    if n < 40:
        return "X" * (n%10) + numToRoman(n - 10)
    if n < 90:
        return "L" + numToRoman(n - 50)
    if n < 100:
        return "XC" + numToRoman(n - 90)
    if n < 400
        return "C" * (n%100) + numToRoman(n%100)
    if n < 900
        return "D" + numToRoman(n - 500)
    if n < 1000
        return "CM" + numToRoman(n - 900)
    if n < 4000
        return "M" * numToRoman(n%1000) + numToRoman(n%1000)

num = input("Enter a number: ")
numToRoman(num)
