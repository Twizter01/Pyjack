
ROMANS: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "C": 50

}

def roman_to_integer1(romans: str) -> int:
    if not romans:
        raise ValueError("No Romans Found")
    
    if len(romans) == 1:
        return ROMANS[romans]

    total: int = 0
    i: int = 0

    while i < len(romans):
        if romans[i] not in ROMANS:
            raise KeyError(f"Key {romans[i]} Not Found")

        current = ROMANS[romans[i]]
        
        if i + 1 < len(romans):
            next = ROMANS[romans[i + 1]]

            if current < next:
                total += (next - current)
                i += 2
                continue
        total += current
        i += 1

    return total

def roman_to_integer0(romans: str) -> int:
    total = 0
    for i in range(len(romans) - 1):
        current = ROMANS[romans[i]]
        next = ROMANS[romans[i + 1]]
        if romans[i] in ROMANS:
            if current >= next:
                total += current
            else:
                total -= current

    total += ROMANS[romans[-1]]
    return total


def roman_to_integer(romans: str) -> int:
    if not romans:
        raise ValueError("Empty string")
    
    total: int = 0
    i: int = 0

  
    while i < len(romans):
        if romans[i] not in ROMANS:
            raise KeyError("Key not found")
            
        current = ROMANS[romans[i]]

        if i + 1 < len(romans):
            next = ROMANS[romans[i + 1]]

            if current < next:
                total += (next - current)
                i += 2
                continue

        total += current
        i += 1 

    return total


try:
    print(roman_to_integer("XIX"))
    print(roman_to_integer("XIV"))
    print(roman_to_integer("XCV"))
    print(roman_to_integer("IV"))
    print(roman_to_integer("III"))
    print(roman_to_integer("X"))
    print(roman_to_integer("U"))
except (ValueError, TypeError, KeyError) as e:
    print(f"Error: {e}")





def roman_to_integer(romans_str: str) -> int:
    if len(romans_str) < 2:
        return ROMANS[romans_str]

    if len(romans_str) == 2:
        return (int(ROMANS[romans_str[0]]) + int(ROMANS[romans_str[1]]))
    
    while len(romans_str) > 2:
        for num in romans_str:
            if num in ROMANS:
                


