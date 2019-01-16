steps = [[item[5], item[36]] for item in open("input.txt").read().split("\n")]

solution_string = ""
can_be_done = []

while len(steps) > 0:
    can_be_done.clear()
    for i in steps:
        if i[0] not in [item[1] for item in steps]:
            can_be_done.append(i)
    
    smalles_value = 1000
    for i in can_be_done:
        numeric_value = ord(i[0])
        if numeric_value < smalles_value:
            smalles_value = numeric_value
    
    steps = [item for item in steps if item[0] != chr(smalles_value)]
    solution_string += chr(smalles_value)
solution_string += can_be_done[0][1]

print ("Part 1: " + solution_string)


steps = [[item[5], item[36]] for item in open("input.txt").read().split("\n")]
time = 0

workers = [0, 0, 0, 0, 0]
time_occupied = [0, 0, 0, 0, 0]
letters = ["", "", "", "", ""]

while len(steps) > 0:
    if(0 in time_occupied):
        for i in steps:
            if i[0] not in [item[1] for item in steps]:
                if 0 in workers and i[0] not in letters:
                    worker = workers.index(0)
                    workers[worker] = 1
                    time_occupied[worker] = 60 + abs(ord(i[0]) - 64)
                    letters[worker] = i[0]
    for i in time_occupied:
        if i > 0:
            time_occupied[time_occupied.index(i)] -= 1
    time += 1
    
    for i in range(0, len(time_occupied)):
        if len(steps) == 1:
            if  letters[i] != "" and time_occupied[i] == 0:
                workers[i] = 0
                time += (60 + abs(ord(steps[0][1]) - 64))
                steps = [item for item in steps if item[0] != letters[i]]
                letters[i] = ""
        elif letters[i] != "" and time_occupied[i] == 0:
            workers[i] = 0
            steps = [item for item in steps if item[0] != letters[i]]
            letters[i] = ""
        
print (time)