def convert(s: str, numRows: int) -> str:
    if (numRows == 1 or len(s)<numRows):
        return s
    
    rows = ['']*min(numRows, len(s))
    current_row = 0
    going_down = False

    for c in s:
        rows[current_row] += c
        if(current_row == 0 or current_row == numRows-1):
            going_down = not going_down
        current_row += 1 if going_down else -1