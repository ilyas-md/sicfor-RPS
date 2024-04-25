import random
def game():
    print("rock = 1")
    print("paper = 2")
    print("scissor = 3")
    rps = int(input("select your choice from above:"))
    if rps == 1: #user_chooses_rock
        comp = random.randint(1,3)
        if rps == comp:
            print("computer choose rock",comp)
            print("ohh...both equals")
        elif comp == 2:
            print("computer choose paper",comp)
            print("you lose")
        else:
            print("computer choose scissor")
            print("you win")
    elif rps == 2: #user_chooses_paper
        comp = random.randint(1, 3)
        if comp == 1:
            print("computer choose rock", comp)
            print("you win")
        elif rps == comp:
            print("computer choose paper", comp)
            print("ohh...both equals")
        else:
            print("computer choose scissor")
            print("you lose")
    else: #user_chooses_scissor
        comp = random.randint(1, 3)
        if comp == 1:
            print("computer choose rock", comp)
            print("you lose")
        elif comp == 2:
            print("computer choose paper", comp)
            print("you win")
        else:
            print("computer choose scissor")
            print("ohh...both equals")