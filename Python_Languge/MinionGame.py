def minion_game(string):
    StuartPoint = 0
    KevinPoint = 0
    length = len(string)
    for i in range(length):
        if string[i] in ("A", "E", "I", "O", "U"):
            KevinPoint += (length-i) 
        else:
            StuartPoint += (length-i)
    if KevinPoint > StuartPoint :
        print(f"Kevin {KevinPoint}")
    elif StuartPoint > KevinPoint :
        print(f"Stuart {StuartPoint}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)