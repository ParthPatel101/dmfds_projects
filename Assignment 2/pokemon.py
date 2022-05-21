import csv
from collections import defaultdict

def firePercentage(f):
    numFireTypes = 0
    numFireTypesOver40 = 0
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        for x in reader:
            if x[4] == 'fire':
                numFireTypes += 1
                if float(x[2]) >= 40.0:
                    numFireTypesOver40 += 1
        with open('pokemon1.txt', 'w') as outfile:
            outfile.write(f"Percentage of fire type Pokemons at or above level 40 = {round((numFireTypesOver40/numFireTypes) * 100)}")

def fillInNaN(f):
    threshold = 40.0
    atkAvgAbove40 = 0
    atkAvgbelow40 = 0
    defAvgAbove40 = 0
    defAvgbelow40 = 0
    hpAvgAbove40 = 0
    hpAvgbelow40 = 0
    atkAvgAbove40Counter = 0
    atkAvgbelow40Counter = 0
    defAvgAbove40Counter = 0
    defAvgbelow40Counter = 0
    hpAvgAbove40Counter = 0
    hpAvgbelow40Counter = 0
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)
        for y in reader:
            if float(y[2]) > threshold:
                if y[6] != 'NaN':
                    atkAvgAbove40 += float(y[6])
                    atkAvgAbove40Counter += 1
                if y[7] != 'NaN':
                    defAvgAbove40 += float(y[7])
                    defAvgAbove40Counter += 1
                if y[8] != 'NaN':
                    hpAvgAbove40 += float(y[8])
                    hpAvgAbove40Counter += 1
            else:
                if y[6] != 'NaN':
                    atkAvgbelow40 += float(y[6])
                    atkAvgbelow40Counter += 1
                if y[7] != 'NaN':
                    defAvgbelow40 += float(y[7])
                    defAvgbelow40Counter += 1
                if y[8] != 'NaN':
                    hpAvgbelow40 += float(y[8])
                    hpAvgbelow40Counter += 1
        atkAvgAbove40 = round(atkAvgAbove40/atkAvgAbove40Counter, 1)
        defAvgAbove40 = round(defAvgAbove40/defAvgAbove40Counter, 1)
        hpAvgAbove40 = round(hpAvgAbove40/hpAvgAbove40Counter, 1)
        
        atkAvgbelow40 = round(atkAvgbelow40/atkAvgbelow40Counter, 1)
        defAvgbelow40 = round(defAvgbelow40/defAvgbelow40Counter, 1)
        hpAvgbelow40 = round(hpAvgbelow40/hpAvgbelow40Counter, 1)

    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        with open('pokemonResult.csv','w',newline='') as csvout:
            writer = csv.writer(csvout)
            columns = next(reader)  
            writer.writerow(columns)
            for x in reader:
                if x[4] == 'NaN': #fill in type
                    if x[5] == "fire":
                        x[4] = "grass"
                    if x[5] == "water":
                        x[4] = "fire"
                    if x[5] == "fighting":
                        x[4] = "normal"
                    if x[5] == "flying":
                        x[4] = "fighting"
                if x[6] == 'NaN': #fill in atk
                    if float(x[2]) > 40.0:
                        x[6] = str(atkAvgAbove40)
                    else:
                        x[6] = str(atkAvgbelow40)
                if x[7] == 'NaN': #fill in def
                    if float(x[2]) > 40.0:
                        x[7] = str(defAvgAbove40)
                    else:
                        x[7] = str(defAvgbelow40)
                if x[8] == 'NaN': #fill in hp
                    if float(x[2]) > 40.0:
                        x[8] = str(hpAvgAbove40)
                    else:
                        x[8] = str(hpAvgbelow40)
                writer.writerow(x)

def typeToPersonality(f):
    output = defaultdict(list)
    with open(f) as csvfile:
        reader = csv.DictReader(csvfile)
        for x in reader:
            if x['type'] != "NaN":
                if x['type'] not in output.keys():
                    output[x['type']] = [x['personality']]
                else:
                    output[x['type']].append(x['personality'])
        for y in output.keys():
            output[y].sort()
        sorted_dict = dict(sorted(output.items()))
        with open('pokemon4.txt', 'w') as outfile:
            for i in sorted_dict.keys():
                outfile.write(f"{i}: ")
                for x in sorted_dict[i]:
                    outfile.write(f"{x}, ")
                outfile.write("\n")

def averageHPStage3(f):
    numStage3 = 0
    avgLevelStage3 = 0
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        for x in reader:
            if x[9] == '3.0':
                numStage3 += 1
                avgLevelStage3 += float(x[2])
        with open('pokemon5.txt', 'w') as outfile:
            outfile.write(f"Average hit point for Pokemons of stage 3.0 = {round(avgLevelStage3/numStage3)}")

def main():
    firePercentage("pokemonTrain.csv")
    fillInNaN("pokemonTrain.csv")
    typeToPersonality("pokemonTrain.csv")
    averageHPStage3("pokemonTrain.csv")

if __name__ == "__main__":
    main()