input_file = [item.split(",") for item in open("input.txt", "r").read().split("\n")]

highest_X = max([int(item[0]) for item in input_file])
highest_Y = max([int(item[1]) for item in input_file])
min_X = 0
min_Y = 0

is_infinite = []
infinite = False
in_multiple_areas = False
solution_area = []

for x in range(min_X, highest_X):
    for y in range(min_Y, highest_Y):
        in_multiple_areas = False
        infinite = False
        min_distance = 1000000
        distance = 0
        index = 0
        
        if x == min_X or x == highest_X:
            infinite = True
        if y == min_Y or y == highest_Y:
            infinite = True
        
        for coord in input_file:
            distance = abs(int(coord[0]) - x) + abs(int(coord[1]) - y)
            if distance == min_distance:
                in_multiple_areas = True
            if distance < min_distance:
                min_distance = distance
                index = input_file.index(coord)
                in_multiple_areas = False
                
        if in_multiple_areas == True:
            solution_area.append(".")
        else:
            solution_area.append(index)
            if infinite == True:
                is_infinite.append(index)

solution_area = [item for item in solution_area if item != "."]
is_infinite = list(set(is_infinite))
for i in is_infinite:
    solution_area = [item for item in solution_area if item != i]

values_in_solution = list(set(solution_area))
biggest_area = 0
for i in values_in_solution:
    count = solution_area.count(i)
    if count > biggest_area:
        biggest_area = count

print(biggest_area)

input_file = open("input.txt", "r").read().split("\n")
coords = set()
solution = 0

for line in input_file:
    x, y = map(int, line.split(", "))
    coords.add((x, y))

for i in range(highest_X + 1):
    for j in range(highest_Y + 1):
        solution += int(sum(abs(x - i) + abs(y - j) for x, y in coords) < 10000)

print (solution)