interger = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def intToRoman(num: int) -> str:
    output = ""

    if (num % 1000) < 900:
        output = output + "M"*(num // 1000)
        num = num % 1000
    elif (num % 1000) >= 900:
        output = output + "M"*(num // 1000)
        output = output + "CM"
        num = num % 1000 - 900

    if (num % 500) < 400:
        output = output + "D"*(num // 500)
        num = num % 500
    elif (num % 500) >= 400:
        output = output + "D"*(num // 500)
        output = output + "CD"
        num = num % 500 - 400

    if (num % 100) < 90:
        output = output + "C"*(num // 100)
        num = num % 100
    elif (num % 100) >= 90:
        output = output + "C"*(num // 100)
        output = output + "XC"
        num = num % 100 - 90

    if (num % 50) < 40:
        output = output + "L"*(num // 50)
        num = num % 50
    elif (num % 50) >= 40:
        output = output + "L"*(num // 50)
        output = output + "XL"
        num = num % 50 - 40

    if (num % 10) < 9:
        output = output + "X"*(num // 10)
        num = num % 10
    elif (num % 10) >= 9:
        output = output + "X"*(num // 10)
        output = output + "IX"
        num = num % 10 - 9

    if (num % 5) < 4:
        output = output + "V"*(num // 5)
        num = num % 5
    elif (num % 5) >= 4:
        output = output + "V"*(num // 5)
        output = output + "IV"
        num = num % 5 - 4

    output = output + "I"*num

    return output


print(intToRoman(1994))
