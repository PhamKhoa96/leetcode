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

    if (num % 1000) != 0 and (num % 1000) < 900:
        output = output + "M"*(num // 1000)
        temp = num % 1000
    elif (num % 1000) >= 900:

        if temp % 500 != 0:
            output = output + "D"*(temp // 500)
            temp = temp % 500
            if temp % 100 != 0:
                output = output + "C"*(temp // 100)
                temp = temp % 100
                if temp % 50 != 0:
                    output = output + "L"*(temp // 50)
                    temp = temp % 50
                    if temp % 10 != 0:
                        output = output + "X"*(temp // 10)
                        temp = temp % 10
                        if temp % 5 != 0:
                            output = output + "V"*(num // 5)
                            output = output + "V"*(temp % 5)

    return output
