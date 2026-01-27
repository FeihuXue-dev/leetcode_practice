"""Convert Roman numerals to integers."""
def romanToInt(self, s:str) -> int:
    roman_number_dict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    total = 0
    present_value = 0
    for char in s[::-1]:
        value = roman_number_dict[char]
        if value < present_value:
            total = total - value
        else:
            total = total + value

        present_value = value

    return total

input = str("MCMXCIV")

result = romanToInt(None, input)
print(result) # Output: 1994
