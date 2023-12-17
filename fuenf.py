f = open("fuenf_test.txt", "r")
lines = f.readlines()

seeds = []
seedToSoil = []
soilToFert = []
fertToWater = []
wattolight = []
ligtotemp = []
temptohum = []
humtoloca = []

count = 0

# print(lines)

for i in lines:
    if i.__contains__("seeds"):
        seeds.append(lines[count][6:].strip())

    if i.__contains__("seed-to-soil"):
        k = 0
        while True:
            if lines[count + k + 1] == '\n':
                break

            seedToSoil.append(lines[count + k + 1].strip())
            k += 1

    if i.__contains__("soil-to-fertilizer"):
        k = 0
        while True:
            if lines[count + k + 1] == '\n':
                break

            soilToFert.append(lines[count + k + 1].strip())
            k += 1

    if i.__contains__("fertilizer-to-water"):
        k = 0
        while True:
            if lines[count + k + 1] == '\n':
                break

            fertToWater.append(lines[count + k + 1].strip())
            k += 1

    if i.__contains__("water-to-light"):
        k = 0
        while True:
            if lines[count + k + 1] == '\n':
                break

            wattolight.append(lines[count + k + 1].strip())
            k += 1

    if i.__contains__("light-to-temperature"):
        k = 0
        while True:
            if lines[count + k + 1] == '\n':
                break

            ligtotemp.append(lines[count + k + 1].strip())
            k += 1

    if i.__contains__("temperature-to-humidity"):
        k = 0
        while True:
            if lines[count + k + 1] == '\n':
                break

            temptohum.append(lines[count + k + 1].strip())
            k += 1

    if i.__contains__("humidity-to-location"):
        for j in range(len(lines) - count - 1):
            humtoloca.append(lines[count + j + 1].strip())

    count += 1

seeds = seeds[0].split(" ")

maps = [seeds, seedToSoil, soilToFert, fertToWater, wattolight, ligtotemp, temptohum, humtoloca]

for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i] != seeds:
            maps[i][j] = maps[i][j].split(" ")


for i in range(len(maps)):
    for j in range(len(maps[i])):
        if i != 0:
            for k in range(len(maps[i][j])):
                maps[i][j][k] = int(maps[i][j][k])
        else:
            for l in range(len(maps[i])):
                maps[i][l] = int(maps[i][l])

print(seeds)
print(seedToSoil)
print(soilToFert)
print(fertToWater)
print(wattolight)
print(ligtotemp)
print(temptohum)
print(humtoloca)

numliststs = {}
numliststf = {}
numlistftw = {}
numlistwtl = {}
numlistltt = {}
numlisttth = {}
numlisthtl = {}

numlists = [numliststs, numliststf, numlistftw, numlistwtl, numlistltt, numlisttth, numlisthtl]

# for k in range(1, 8):
#     for i in range(len(maps[k])):
#         for j in range(maps[k][i][2]):
#             if maps[k] == seedToSoil:
#                 numliststs[maps[k][i][1] + j] = maps[k][i][0] + j
#             elif maps[k] == soilToFert:
#                 numliststf[maps[k][i][1] + j] = maps[k][i][0] + j
#             elif maps[k] == fertToWater:
#                 numlistftw[maps[k][i][1] + j] = maps[k][i][0] + j
#             elif maps[k] == wattolight:
#                 numlistwtl[maps[k][i][1] + j] = maps[k][i][0] + j
#             elif maps[k] == ligtotemp:
#                 numlistltt[maps[k][i][1] + j] = maps[k][i][0] + j
#             elif maps[k] == temptohum:
#                 numlisttth[maps[k][i][1] + j] = maps[k][i][0] + j
#             elif maps[k] == humtoloca:
#                 numlisthtl[maps[k][i][1] + j] = maps[k][i][0] + j

for k in range(1, 8):
    current_map = maps[k]
    current_numlist = numlists[k - 1]

    for i in range(len(current_map)):
        start_value = int(current_map[i][0])
        target_value = int(current_map[i][1])

        for j in range(current_map[i][2]):
            current_key = target_value + j
            current_value = start_value + j

            if current_numlist.get(current_key):
                current_numlist[current_key].append(current_value)
            else:
                current_numlist[current_key] = current_value


seednumbers = {}

for i in seeds:
    seednumbers[i] = i

print(seednumbers)
print(numlists)


for j in range(len(numlists)):
    for i in seednumbers:
        if numlists[j].__contains__(seednumbers[i]):
            seednumbers[i] = numlists[j][seednumbers[i]]




# print(seednumbers)
#
# print(numliststs)
# print(numliststf)
# print(numlistftw)
# print(numlistwtl)
# print(numlistltt)
# print(numlisttth)
# print(numlisthtl)

locations = []

for i in seednumbers:
    locations.append(seednumbers[i])

locations = sorted(locations)

print(locations[0])