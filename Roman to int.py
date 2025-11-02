def romToInt(romint):
    roman={"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    result = 0

    for i in range(0,len(romint)-1):
        if roman[romint[i]] <roman[romint[i+1]]:
            result -= roman[romint[i]]
        else:
            result += roman[romint[i]]
    return result+roman[romint[-1]]

rom = input("Enter a Roman Numeral:")
print("Roman To Integer is:", romToInt(rom))