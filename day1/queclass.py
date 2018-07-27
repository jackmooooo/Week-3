import random

import time


class MyStack:

    def __init__(self):
        self.List = []

    def push(self, x):
        self.List.append(x)


    def pushlist(self, arr):
        for i in arr:
            self.push(i)
        print(self.List)


    def pop(self):
        x = self.lent()-1
        self.List = self.List[:x]


    def popmult(self, num):
        for i in range(int(num)):
            self.pop()
        print(self.List)


    def top(self):
        x = self.List[:self.lent()-2]
        self.List = self.List[:self.lent()-2]
        return x


    def empty(self):
        if self.lent() == 0:
            return True
        else:
            return False


    def lent(self):
        returned = 0
        for i in self.List:
            returned += 1
        return returned


class MyQueue:

    def __init__(self):
        self.List = []


    def push(self, x):
        self.List.append(x)
        print(self.List)


    def pushlist(self, arr):
        for i in arr:
            self.push(i)
        print(self.List)


    def pop(self):
        if self.empty():
            print("you cant remove anything because there is nothing here.")
            return
        else:
            x = self.List[0]
            self.List = self.List[1:]


    def popmult(self, num):
        for i in range(int(num)):
            self.pop()
        print(self.List)


    def peek(self):
        if self.lent() == 0:
            print("there is nothing to see here.")
        else:
            return self.List[0]


    def empty(self):
        if self.lent() == 0:
            return True
        else:
            return False


    def lent(self):
        returned = 0
        for i in self.List:
            returned += 1
        return returned


def directory():
    true = True
    stacks = []
    queues = []
    while true:
        print("")
        inp1 = input("make '1', push '2', pop '3', see next '4', see if empty '5', length '6'  >> ")
        print("")
        if inp1 == "1":
            inp2 = input("stack'1', queue'2'  >> ")
            print('')
            if inp2 == "1":
                new = MyStack()
                stacks.append(new)
                print("it will appear at the end of the queues array.")
                print("")
                print("there are currently " + str(len(stacks)) + " stacks.")
            elif inp2 == "2":
                new = MyStack()
                stacks.append(new)
                print("it will appear at the end of the stacks array")
                print("")
                print("there are currently " + str(len(stacks)) + " queues.")
        elif inp1 == "2":
            inp2 = input("stack'1', queue'2'  >> ")
            print('')
            if inp2 == "1":
                arr = []
                inp3 = int(input("what stack (0 index)  >> "))
                print('')
                newtrue = True
                while newtrue:
                    inp4 = input("what value  >> ")
                    print('')
                    if inp4 == "cancel" or inp4 == "end" or inp4 == "stop" or inp4 == "exit" or inp1 == "quit":
                        newtrue = False
                    else:
                        arr.append(inp4)
                stacks[inp3].pushlist(arr)
            elif inp2 == "2":
                inp3 = input("what queue (0 index)  >> ")
                print('')
                newtrue = True
                while newtrue:
                    arr = []
                    inp4 = input("what value  >> ")
                    print('')
                    if inp4 == "cancel" or inp4 == "end" or inp4 == "stop" or inp4 == "exit" or inp1 == "quit":
                        newtrue = False
                    else:
                        arr.append(inp4)
                queues[inp3].pushlist(arr)
        elif inp1 == "3":
            inp2 = input("stack'1', queue'2'  >> ")
            print('')
            if inp2 == "1":
                inp3 = int(input("what stack (0 index)  >> "))
                print("")
                inp4 = int(input("how many  >> "))
                print('')
                stacks[inp3].popmult(inp4)
            elif inp2 == "2":
                inp3 = int(input("what queue (0 index)  >> "))
                print('')
                inp4 = int(input("how many  >> "))
                print("")
                queues[inp3].popmult(inp4)
        elif inp1 == "4":
            inp2 = input("stack'1', queue'2'  >> ")
            print('')
            if inp2 == "1":
                inp3 = int(input("what stack (0 index)  >> "))
                print('')
                print(stacks[inp3].top())
            elif inp2 == "2":
                print('')
                print(queues[inp3].peek())
        elif inp1 == "5":
            inp2 = input("stack'1', queue'2'  >> ")
            print("")
            if inp2 == "1":
                inp3 = int(input("what stack (0 index)  >> "))
                print('')
                print(stacks[inp3].empty())
            elif inp2 == "2":
                inp3 = int(input("what queue (0 index)  >> "))
                print('')
                print(queues[inp3].empty())
        elif inp1 == "6":
            inp2 = input("stack'1', queue'2'  >> ")
            print('')
            if inp2 == "1":
                inp3 = int(input("what stack (0 index)  >> "))
                print('')
                print(stacks[inp3].lent())
            elif inp2 == "2":
                inp3 = int(input("what queue (0 index)  >> "))
                print('')
                print(queues[inp3].lent())
        elif inp1 == "cancel" or inp1 == "exit" or inp1 == "end" or inp1 == "stop" or inp1 == "quit":
            true = False

start = time.time()

directory()

end = time.time()

print("you spent " + str(end-start) + " seconds on this")
