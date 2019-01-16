# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:51:52 2019

@author: theilel2
"""

data = open("input.txt").read().split("\n")

data.sort()

sleeping_time = []
time_to_sleep = 0
sleeptime = 0
guard_no = 0
    
for i in data:
    if "Guard" in i:
        if guard_no != 0:
            sleeping_time.append([guard_no, sleeptime])
            sleeptime = 0
        guard_no = i.split(" ")[3][1:]
    elif "falls" in i:
        time_to_sleep = i.split(":")[1][:2]
    else:
        sleeptime += int(i.split(":")[1][:2]) - int(time_to_sleep)
        time_to_sleep = 0
        
longest_sleeper = []
longest_sleeping_time = 0
for i in sleeping_time:
    if i[1] > longest_sleeping_time:
        longest_sleeping_time = i[1]
        longest_sleeper.append(i[0])
    if i[1] == longest_sleeping_time:
        longest_sleeper.append(i[0])
        
longest_sleeper = list(set(longest_sleeper))

solution_gard = []

for sleeper in longest_sleeper:
    minute = []
    for i in range(0, 60):
        minute.append([i, 0])
        
    relevant = False
    for i in data:
        if i.split(" ")[3][1:] == sleeper:
            relevant = True
        elif "Guard" in i:
            relevant = False
        
        if relevant == True:
            if "falls" in i:
                time_to_sleep = i.split(":")[1][:2]
                awakening_time = 0
            else:
                awakening_time = i.split(":")[1][:2]
                
                for i in range(int(time_to_sleep), int(awakening_time)):
                    minute[i][1] += 1
                
                time_to_sleep = 0
    highest_minute = 0
    highest_count = 0
    for i in minute:
        if i[1] > highest_count:
            highest_minute = i[0]
            highest_count = i[1]
    solution_gard.append([sleeper, highest_minute, highest_count])