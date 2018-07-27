import random

def roll(inp):
    print(random.randint(1, inp))

def directory():
    true = True
    while true:
        print("")
        inp1 = input("what dice would you like to roll  >> ")
        print("")
        if inp1[0] == "d":
            roll(int(inp1[1:]))
        elif inp1 == "cancel" or inp1 == "end" or inp1 == "stop" or inp1 == "quit":
            true = False

directory()
