def intToRoman(num):
    # Step 1: Define symbol-value pairs in descending order
    val_to_symbol = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    roman = ""
    
    # Step 2: Loop through the symbol list
    for value, symbol in val_to_symbol:
        if num == 0:
            break
        # Find how many times the symbol fits into num
        count = num // value
        if count > 0:
            roman += symbol * count     # Append the symbol `count` times
            num -= value * count        # Subtract that much from the number
    
    return roman
