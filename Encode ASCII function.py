
def Encode():
    string = str(input("ENTER STRING:\n"))
    y = 0
    count = 1
    total_encode = ""
    while y < len(string):
        try:
            while string[y] == string[y + 1]:
                count += 1
                y += 1
        except IndexError:
            pass
        if count < 10:
            count = ("0" + str(count))
        encode = (str(count) + string[y])
        total_encode += encode
        y += 1
        count = 1
    print(total_encode)


while True:
    Encode()
