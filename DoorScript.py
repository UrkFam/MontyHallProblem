# This is a code rendition of the Monty Hall Problem
# Basically, if you had to pick a door out of 3 at random, you will theoretically have a 1/3 chance
# of winning the grand prize (3 doors, 2 small prizes, 1 grand prize)
# However, given the host will remove a small prize after you select your choice, the Monty Hall Problem
# seeks to prove that by switching your door from the remaining one, your odds increase to 2/3 (double your odds)

import random


def generate(numIterations):
    stay = 0
    switch = 0

    # userInput = input("How many iterations of this test?: ")
    iterations = int(numIterations)

    i = 0

    # Run iterations of this problem
    while i < iterations:
        # Reset doors
        doors = [None, None, None]
        # Pick a winning door at random
        winningDoorNumber = random.randint(0, 2)
        doors[winningDoorNumber] = 1
        winningDoor = doors[winningDoorNumber]

        # Have contestant choose a door (1-3)
        # doorInput = input("Pick a door between (1-3): ")
        doorInput = random.randint(0, 2)
        selectDoor = int(doorInput)
        contestantDoorNumber = selectDoor
        contestantDoor = doors[selectDoor]

        # Find a door to show the contestant
        goatDoor = -1
        while goatDoor == winningDoorNumber or goatDoor == contestantDoorNumber:
            goatDoor = random.randint(0, 2)
        if contestantDoor == winningDoor:
            stay += 1
            print("Contestant picks", contestantDoorNumber, "and the winning door was", winningDoorNumber)
            print("Stay Wins!")
        else:
            switch += 1
            print("Contestant picks", contestantDoorNumber, "and the winning door was", winningDoorNumber)
            print("Switch Wins!")
        i += 1
    results = 'Staying won', stay, "times and", "switching won", switch, 'times'
    return results
