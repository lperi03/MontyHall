##Monty Hall Problem in Python
##Simulating this for 3 doors
import numpy as np
import random
import matplotlib.pyplot as plt

#need a function that simulates the host opening a wrong door
#also need a function to simulate switching (if applicable)

successes = 0
trials  = 0
successPercentage = []
#function to simulate the player opening a door
def player_selection(doors):
    return random.choice(doors)

#function to select prize randomly from possible doors
def prize_selection(doors):
    return random.choice(doors)


#function to simulate host opening a wrong door
def host_selection(doors, player_choice, prize):
#     player_choice_index  = doors.index(player_choice)
#     prize_index = doors.index(prize)
    host_doors = []
    if player_choice == prize:
        host_doors = list(set(doors) - set([player_choice]))
    else:
        host_doors = list(set(doors) - set([player_choice] + [prize]))
    return random.choice(host_doors)

#function to simulate switching
#the bool input determines whether or not the player switches
def switch_choice(bool, host_choice, player_choice, doors):
#     player_choice_index = doors.index(player_choice)
#     host_choice_index = doors.index(host_choice)
    remaining_doors = list(set(doors) - set([player_choice] + [host_choice]))
    if bool == True:
        return random.choice(remaining_doors)
    else:
        return player_choice


#game sequence
#switch is a boolean that represents whether a player will switch. 
#the point is to simulate number of wins when a player switches vs doesn't switch
def play_game(switch, doors):
    prize = prize_selection(doors)
    player_choice = player_selection(doors)
#     print("the player selected door:" + str(player_choice))
    host_choice = host_selection(doors, player_choice, prize)
#     print("the host opened door:" + str(host_choice))
    if switch:
        final_choice = switch_choice(True, host_choice, player_choice, doors)
#         print("the player switched to door:" + str(final_choice))
    
    else:
        final_choice = player_choice
#         print("the player did not switch" + str(player_choice))
    return final_choice == prize

#engine to generate percentage of winning given a number of trials, and a boolean 'switch' that determines whether or not the player will switch their choice
def engine(numTrials, switch):
    doors = [1, 2, 3]
    numSuccesses = 0
    probSuccesses = []
    for i in range(1, numTrials + 1):
        result = play_game(switch, doors)
        #play_game(False, doors)
        if result:
            numSuccesses += 1
            probSuccesses.append(numSuccesses/i)

        else:
            probSuccesses.append(numSuccesses/i)

    successes = numSuccesses
    trials = numTrials
    successPercentage = probSuccesses
    print("the number of trials is:" + " " + str(numTrials))
    print("the number of successes is:" + " " + str(numSuccesses))
    if switch:
        print("the win percentage of the player who always switches after" + " " + str(numTrials) + " " "trials is:" + " " + str(probSuccesses[-1]))
    else:
        print("the win percentage of the player who never switches after" + " " + str(numTrials) + " " "trials is:" + " " + str(probSuccesses[-1]))
    return probSuccesses


#defining the output list that contains the probabilities as number of trials increases
successPercentage = engine(10000, True)
print(len(successPercentage))
plt.figure(figsize = (10, 8))
plt.title("Monty Hall problem success probability visualizer")
plt.xlabel("number of trials")
plt.ylabel("total probability of success after" + str(trials) + "trials")
lst = []
for i in range(10000):
    lst.append(i)
plt.plot(lst, successPercentage)
#     print(successPercentage[i])
#     plt.plot(i, successPercentage[i])

plt.show()




        
        







