

def toBinary(a):
    l, m  = [] , []
    for i in a:
         l.append(ord(i))
    for i in l:
       m.append(int(bin(i)[2:]))
    return m





import math
print("welcome to txt to binary program")
ask = input("do you want to code in to binary or decode into txt"
            "press 1 for code\n or 2 for decode:\n")


if ask == "1":
    bi = input('what do you want to code in to binary?\n')
    print(f"your code is { str(toBinary(bi)) }")



elif ask == "2":
    bk = input('what do you want to decode in to txt?\n')
    print(f"you txt is{BinaryToDecimal(bk)}")




