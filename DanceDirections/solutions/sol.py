translation = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}
cases = int(input())
for _ in range(cases):
    posX = 0
    posY = 0
    facing = 0
    n = int(input())
    for _ in range(n):
        letter, amount = input().split()
        amount = int(amount)
        if letter in "NWES":
            dy, dx = translation[letter]
            dy *= amount
            dx *= amount
            posY += dy
            posX += dx
        elif letter == "CW":
            facing += amount
            facing %= 360
        elif letter == "CCW":
            facing -= amount
            facing %= 360
        elif letter in ["F", "B"]:
            dy, dx = translation[facing//90]
            dy *= amount
            dx *= amount
            if letter == "F":
                posY += dy
                posX += dx
            else:
                posY -= dy
                posX -= dx
    print(abs(posX) + abs(posY))
