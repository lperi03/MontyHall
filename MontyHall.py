##Monty Hall Problem in Python
##Simulating this for 3 doors
import numpy as np
import random
import matplotlib.pyplot as plt

#need a function that simulates the host opening a wrong door
#also need a function to simulate switching (if applicable)

num_doors = [1, 2, 3]

#function to simulate the player opening a door
def player_selection(doors):
    player_choice = random.choice(doors)
    return player_choice

#function to select prize randomly from possible doors
def prize_selection(doors):
    return random.choice(doors)


#function to simulate host opening a wrong door
def host_selection(doors, player_choice, prize):
    player_choice_index  = doors.index(player_choice)
    prize_index = doors.index(prize)
    if player_choice == prize:
        host_doors = doors - list(doors[player_choice_index])
    else:
        host_doors = doors - (list(doors[player_choice_index]) + list(doors[prize_index]))
    return random.choice(host_doors)

#function to simulate switching
#the bool input determines whether or not the player switches
def switch_choice(bool, host_choice, player_choice, doors):
    player_choice_index = doors.index(player_choice)
    host_choice_index = doors.index(host_choice)
    remaining_doors = doors - (list(doors[player_choice_index]) + list(doors[host_choice_index]))
    if bool == True:
        return random.choice(remaining_doors)
    else:
        return player_choice


#game sequence
#switch is a boolean that represents whether a player will switch. 
#the point is to simulate number of wins when a player switches vs doesn't switch
def play_game(switch, doors):
    prize = prize_selection(doors)
    prize_index = doors.index(prize)
    player_choice = player_selection(doors)
    print("the player selected")
    host_choice = host_selection(doors, player_choice, prize)
    if switch:
        final_choice = switch_choice(True, host_choice, player_choice, doors)
    else:
        final_choice = player_choice
    return final_choice == player_choice

#engine to generate probability of winning given a number of trials, and a boolean 'switch' that determines whether or not the player will switch their choice
def engine(numTrials, switch):
    doors = [1, 2, 3]
    numSuccesses = 0
    numTrials = 0
    probSuccesses = []
    for i in range(numTrials):
        result = play_game(True, doors)
        #play_game(False, doors)
        if result:
            numSuccesses += 1
            numTrials += 1
            probSuccesses.append(numSuccesses/numTrials)

        else:
            numTrials += 1
            probSuccesses.append(numSuccesses/numTrials)

        
        







