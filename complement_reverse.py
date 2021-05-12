def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)  # reverse all letters in a string
    Pattern = Complement(Pattern)  # complement each letter in a string
    return Pattern


def Reverse(Pattern):
    patternb = list(range(len(Pattern)))
    n = len(Pattern)
    for i in range(n):
        patternb[i] = Pattern[n - i - 1]
    return "".join(patternb)


def Complement(Pattern):
    Pattern = list(Pattern)
    n = len(Pattern)
    for i in range(n):
        if Pattern[i] == "A":
            Pattern[i] = "T"
        elif Pattern[i] == "T":
            Pattern[i] = "A"
        elif Pattern[i] == "G":
            Pattern[i] = "C"
        else:
            Pattern[i] = "G"
    return "".join(Pattern)

print (ReverseComplement("ATCGGGGAT"))