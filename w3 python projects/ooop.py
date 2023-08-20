
import random

num   = random.randrange(0, 30)

tries = 10

for _ in range(10):
    gnum = int(input(" start guessing your number now:\n"))
    tries = tries - 1
    if gnum > num:
        print(f"your number is bigger\nyou have {tries} left!")


    elif gnum < num:
        print(f"your number is smaller \nyou have {tries} left!")

    else:
        print("OMG you won!!!! I am proud of you and don't forget to slap shahjee on his ass")

