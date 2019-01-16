from collections import deque

data = open("input.txt").read()

players = int(data[:3])
last_marble = int(data[-12: -7]) #* 100 include for part 2
scores = [0] * players
circle = deque([0])

for i in range(1, last_marble):
    if i % 23 == 0:
        circle.rotate(7)
        scores[i % players] += i + circle[-1]
        circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(i)

print (max(scores))