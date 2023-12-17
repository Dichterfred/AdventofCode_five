with open("fuenf.txt", "r") as f:
    lines = f.readlines()
    print(lines)

    seeds = []
    seedToSoil = []
    soilToFert = []
    fertToWater = []
    wattolight = []
    ligtotemp = []
    temptohum = []
    humtoloca = []

    count = 0
    for i in lines:
        if i.__contains__("seeds"):
            seeds.append(lines[count][6:].strip())

        if i.__contains__("seed-to-soil"):
            k = 0
            while True:
                if lines[count + k + 1] == '\n':
                    break

                seedToSoil.append(lines[count + k + 1].strip().split(" "))
                k += 1

        if i.__contains__("soil-to-fertilizer"):
            k = 0
            while True:
                if lines[count + k + 1] == '\n':
                    break

                soilToFert.append(lines[count + k + 1].strip().split(" "))
                k += 1

        if i.__contains__("fertilizer-to-water"):
            k = 0
            while True:
                if lines[count + k + 1] == '\n':
                    break

                fertToWater.append(lines[count + k + 1].strip().split(" "))
                k += 1

        if i.__contains__("water-to-light"):
            k = 0
            while True:
                if lines[count + k + 1] == '\n':
                    break

                wattolight.append(lines[count + k + 1].strip().split(" "))
                k += 1

        if i.__contains__("light-to-temperature"):
            k = 0
            while True:
                if lines[count + k + 1] == '\n':
                    break

                ligtotemp.append(lines[count + k + 1].strip().split(" "))
                k += 1

        if i.__contains__("temperature-to-humidity"):
            k = 0
            while True:
                if lines[count + k + 1] == '\n':
                    break

                temptohum.append(lines[count + k + 1].strip().split(" "))
                k += 1

        if i.__contains__("humidity-to-location"):
            for j in range(len(lines) - count - 1):
                humtoloca.append(lines[count + j + 1].strip().split(" "))

        count += 1

    seeds = seeds[0].split(" ")

    maps = [seeds, seedToSoil, soilToFert, fertToWater, wattolight, ligtotemp, temptohum, humtoloca]

    for i, j in enumerate(maps):
        for lenj in range(len(j)):
            if i == 0:
                j[lenj] = int(j[lenj])
            else:
                for l1 in range(len(j[lenj])):
                    j[lenj][l1] = int(j[lenj][l1])

    print(seeds)
    print(seedToSoil)
    print(soilToFert)
    print(fertToWater)
    print(wattolight)
    print(ligtotemp)
    print(temptohum)
    print(humtoloca)

    seedsdict1 = {}
    seedsdict2 = {}
    seedsdict3 = {}
    seedsdict4 = {}
    seedsdict5 = {}
    seedsdict6 = {}
    seedsdict7 = {}
    seedsdict8 = {}

    rangedict = {}

    for i, j in enumerate(maps[0]):
        seedsdict1[j] = j

    for index, seed in enumerate(seeds):
        for len_maps, o in enumerate(seedToSoil):
            for rangelen in range(seedToSoil[len_maps][2]):
                rangedict[seedToSoil[len_maps][1] + rangelen] = seedToSoil[len_maps][0 ] + rangelen

                if rangedict.__contains__(seed):
                    seedsdict1[seed] = rangedict[seed]
                    seedsdict2[rangedict[seed]] = rangedict[seed]
                else:
                    seedsdict2[seed] = seed

            rangedict.clear()

    rangedict.clear()


    # for index, seed in enumerate(seedsdict2):
    #     for len_maps, o in enumerate(soilToFert):
    #         for rangelen in range(soilToFert[len_maps][2]):
    #             rangedict[soilToFert[len_maps][1] + rangelen] = soilToFert[len_maps][0] + rangelen
    #
    #     if rangedict.__contains__(seed):
    #         seedsdict2[seed] = rangedict[seed]
    #         seedsdict3[rangedict[seed]] = rangedict[seed]
    #     else:
    #         seedsdict3[seed] = seed
    #
    # rangedict.clear()
    #
    #
    # for index, seed in enumerate(seedsdict3):
    #     for len_maps, o in enumerate(fertToWater):
    #         for rangelen in range(fertToWater[len_maps][2]):
    #             rangedict[fertToWater[len_maps][1] + rangelen] = fertToWater[len_maps][0 ] + rangelen
    #
    #     if rangedict.__contains__(seed):
    #         seedsdict3[seed] = rangedict[seed]
    #         seedsdict4[rangedict[seed]] = rangedict[seed]
    #     else:
    #         seedsdict4[seed] = seed
    #
    # print(rangedict)
    #
    # rangedict.clear()
    #
    # for index, seed in enumerate(seedsdict4):
    #     for len_maps, o in enumerate(wattolight):
    #         for rangelen in range(wattolight[len_maps][2]):
    #             rangedict[wattolight[len_maps][1] + rangelen] = wattolight[len_maps][0 ] + rangelen
    #
    #     if rangedict.__contains__(seed):
    #         seedsdict4[seed] = rangedict[seed]
    #         seedsdict5[rangedict[seed]] = rangedict[seed]
    #     else:
    #         seedsdict5[seed] = seed
    #
    # rangedict.clear()
    #
    # for index, seed in enumerate(seedsdict5):
    #     for len_maps, o in enumerate(ligtotemp):
    #         for rangelen in range(ligtotemp[len_maps][2]):
    #             rangedict[ligtotemp[len_maps][1] + rangelen] = ligtotemp[len_maps][0 ] + rangelen
    #
    #     if rangedict.__contains__(seed):
    #         seedsdict5[seed] = rangedict[seed]
    #         seedsdict6[rangedict[seed]] = rangedict[seed]
    #     else:
    #         seedsdict6[seed] = seed
    #
    # rangedict.clear()
    #
    # for index, seed in enumerate(seedsdict6):
    #     for len_maps, o in enumerate(temptohum):
    #         for rangelen in range(temptohum[len_maps][2]):
    #             rangedict[temptohum[len_maps][1] + rangelen] = temptohum[len_maps][0 ] + rangelen
    #
    #     if rangedict.__contains__(seed):
    #         seedsdict6[seed] = rangedict[seed]
    #         seedsdict7[rangedict[seed]] = rangedict[seed]
    #     else:
    #         seedsdict7[seed] = seed
    #
    # rangedict.clear()
    #
    # for index, seed in enumerate(seedsdict7):
    #     for len_maps, o in enumerate(humtoloca):
    #         for rangelen in range(humtoloca[len_maps][2]):
    #             rangedict[humtoloca[len_maps][1] + rangelen] = humtoloca[len_maps][0 ] + rangelen
    #
    #     if rangedict.__contains__(seed):
    #         seedsdict7[seed] = rangedict[seed]
    #         seedsdict8[rangedict[seed]] = rangedict[seed]
    #     else:
    #         seedsdict8[seed] = seed
    #
    # rangedict.clear()


    print(seedsdict1)
    print(seedsdict2)
    print(seedsdict3)
    print(seedsdict4)
    print(seedsdict5)
    print(seedsdict6)
    print(seedsdict7)
    print(seedsdict8)

    # locations = []
    #
    # for i, j in enumerate(seedsdict8):
    #     locations.append(j)
    #
    # locations.sort()
    #
    # print(locations[0])

