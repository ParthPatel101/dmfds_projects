import csv

def replaceNaNs(f):
    AichiPrefectureLatAvg = 0
    AichiPrefectureLatCounter = 0
    AichiPrefectureLongAvg = 0
    AichiPrefectureLongCounter = 0
    
    AnhuiLatAvg = 0
    AnhuiLatCounter = 0
    AnhuiLongAvg = 0
    AnhuiLongCounter = 0
    
    BeijingLatAvg = 0
    BeijingLatCounter = 0
    BeijingLongAvg = 0
    BeijingLongCounter = 0
    
    GansuLatAvg = 0
    GansuLatCounter = 0
    GansuLongAvg = 0
    GansuLongCounter = 0
    
    GuangdongLatAvg = 0
    GuangdongLatCounter = 0
    GuangdongLongAvg = 0
    GuangdongLongCounter = 0
    
    GuangxiLatAvg = 0
    GuangxiLatCounter = 0
    GuangxiLongAvg = 0
    GuangxiLongCounter = 0
    
    GuizhouLatAvg = 0
    GuizhouLatCounter = 0
    GuizhouLongAvg = 0
    GuizhouLongCounter = 0
    
    hokkiadoLatAvg = 0
    hokkiadoLatCounter = 0
    hokkiadoLongAvg = 0
    hokkiadoLongCounter = 0
    
    HongKongLatAvg = 0
    HongKongLatCounter = 0
    HongKongLongAvg = 0
    HongKongLongCounter = 0
    
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)
        for y in reader:
            if y[6] != 'NaN':
                if y[4] == 'Aichi Prefecture':
                    AichiPrefectureLatAvg += float(y[6])
                    AichiPrefectureLatCounter += 1
                elif y[4] == 'Anhui':
                    AnhuiLatAvg += float(y[6])
                    AnhuiLatCounter += 1
                elif y[4] == 'Beijing':
                    BeijingLatAvg += float(y[6])
                    BeijingLatCounter += 1
                elif y[4] == 'Gansu':
                    GansuLatAvg += float(y[6])
                    GansuLatCounter += 1
                elif y[4] == 'Guangdong':
                    GuangdongLatAvg += float(y[6])
                    GuangdongLatCounter += 1
                elif y[4] == 'Guangxi':
                    GuangxiLatAvg += float(y[6])
                    GuangxiLatCounter += 1
                elif y[4] == 'Guizhou':
                    GuizhouLatAvg += float(y[6])
                    GuizhouLatCounter += 1
                elif y[4] == 'Hokkaido':
                    hokkiadoLatAvg +=float(y[6])
                    hokkiadoLatCounter += 1
                elif y[4] == 'Hong Kong':
                    HongKongLatAvg += float(y[6])
                    HongKongLatCounter += 1
                else:
                        print("oops")
            if y[7] != 'NaN':
                if y[4] == 'Aichi Prefecture':
                    AichiPrefectureLongAvg += float(y[7])
                    AichiPrefectureLongCounter += 1
                elif y[4] == 'Anhui':
                    AnhuiLongAvg += float(y[7])
                    AnhuiLongCounter += 1
                elif y[4] == 'Beijing':
                    BeijingLongAvg += float(y[7])
                    BeijingLongCounter += 1
                elif y[4] == 'Gansu':
                    GansuLongAvg += float(y[7])
                    GansuLongCounter += 1
                elif y[4] == 'Guangdong':
                    GuangdongLongAvg += float(y[7])
                    GuangdongLongCounter += 1
                elif y[4] == 'Guangxi':
                    GuangxiLongAvg += float(y[7])
                    GuangxiLongCounter += 1
                elif y[4] == 'Guizhou':
                    GuizhouLongAvg += float(y[7])
                    GuizhouLongCounter += 1
                elif y[4] == 'Hokkaido':
                    hokkiadoLongAvg +=float(y[7])
                    hokkiadoLongCounter += 1
                elif y[4] == 'Hong Kong':
                    HongKongLongAvg += float(y[7])
                    HongKongLongCounter += 1
                else:
                        print("oops")
                    
    AichiPrefectureLatAvg /= AichiPrefectureLatCounter
    AichiPrefectureLongAvg /= AichiPrefectureLongCounter
    AnhuiLatAvg /= AnhuiLatCounter
    AnhuiLongAvg /= AnhuiLongCounter
    BeijingLatAvg /= BeijingLatCounter
    BeijingLongAvg /=BeijingLongCounter
    GansuLatAvg /= GansuLatCounter
    GansuLongAvg /= GansuLongCounter
    GuangdongLatAvg /= GuangdongLatCounter
    GuangdongLongAvg /= GuangdongLongCounter
    GuangxiLatAvg /= GuangxiLatCounter
    GuangxiLongAvg /= GuangxiLongCounter
    GuizhouLatAvg /= GuizhouLatCounter
    GuizhouLongAvg /= GuizhouLongCounter
    hokkiadoLatAvg /= hokkiadoLatCounter
    hokkiadoLongAvg /= hokkiadoLongCounter
    HongKongLatAvg /= HongKongLatCounter
    HongKongLongAvg /= HongKongLongCounter
    
    AichiCounter = dict()
    AnhuiCounter = dict()
    BeijingCounter = dict()
    GansuCounter = dict()
    GuangdongCounter = dict()
    GuangxiCounter = dict()
    GuizhouCounter = dict()
    HokkiadoCounter = dict()
    HongKongCounter = dict()
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)
        for s in reader:
            if s[4] == 'Aichi Prefecture':
                city = s[3]
                if city != "NaN":
                    if city in AichiCounter:
                        AichiCounter[city] += 1
                    else:
                        AichiCounter[city] = 1
            elif s[4] == 'Anhui':
                city = s[3]
                if city != "NaN":
                    if city in AnhuiCounter:
                        AnhuiCounter[city] += 1
                    else:
                        AnhuiCounter[city] = 1
            elif s[4] == 'Beijing':
                city = s[3]
                if city != "NaN":
                    if city in BeijingCounter:
                        BeijingCounter[city] += 1
                    else:
                        BeijingCounter[city] = 1
            elif s[4] == 'Gansu':
                city = s[3]
                if city != "NaN":
                    if city in GansuCounter:
                        GansuCounter[city] += 1
                    else:
                        GansuCounter[city] = 1
            elif s[4] == 'Guangdong':
                city = s[3]
                if city != "NaN":
                    if city in GuangdongCounter:
                        GuangdongCounter[city] += 1
                    else:
                        GuangdongCounter[city] = 1
            elif s[4] == 'Guangxi':
                city = s[3]
                if city != "NaN":
                    if city in GuangxiCounter:
                        GuangxiCounter[city] += 1
                    else:
                        GuangxiCounter[city] = 1
            elif s[4] == 'Guizhou':
                city = s[3]
                if city != "NaN":
                    if city in GuizhouCounter:
                        GuizhouCounter[city] += 1
                    else:
                        GuizhouCounter[city] = 1
            elif s[4] == 'Hokkaido':
                city = s[3]
                if city != "NaN":
                    if city in HokkiadoCounter:
                        HokkiadoCounter[city] += 1
                    else:
                        HokkiadoCounter[city] = 1
            elif s[4] == 'Hong Kong':
                city = s[3]
                if city != "NaN":
                    if city in HongKongCounter:
                        HongKongCounter[city] += 1
                    else:
                        HongKongCounter[city] = 1
            else:
                print("oops")

    Aichi2Counter = dict()
    Anhui2Counter = dict()
    Beijing2Counter = dict()
    Gansu2Counter = dict()
    Guangdong2Counter = dict()
    Guangxi2Counter = dict()
    Guizhou2Counter = dict()
    Hokkiado2Counter = dict()
    HongKong2Counter = dict()
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)
        for s in reader:
            if s[4] == 'Aichi Prefecture':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Aichi2Counter:
                                    Aichi2Counter[j] += 1
                                else:
                                    Aichi2Counter[j] = 1
                        elif i in Aichi2Counter:
                            Aichi2Counter[i] += 1
                        else:
                            Aichi2Counter[i] = 1
            elif s[4] == 'Anhui':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Anhui2Counter:
                                    Anhui2Counter[j] += 1
                                else:
                                    Anhui2Counter[j] = 1
                        elif i in Anhui2Counter:
                            Anhui2Counter[i] += 1
                        else:
                            Anhui2Counter[i] = 1
            elif s[4] == 'Beijing':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Beijing2Counter:
                                    Beijing2ounter[j] += 1
                                else:
                                    Beijing2Counter[j] = 1
                        elif i in Beijing2Counter:
                            Beijing2Counter[i] += 1
                        else:
                            Beijing2Counter[i] = 1
            elif s[4] == 'Gansu':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Gansu2Counter:
                                    Gansu2Counter[j] += 1
                                else:
                                    Gansu2Counter[j] = 1
                        elif i in Gansu2Counter:
                            Gansu2Counter[i] += 1
                        else:
                            Gansu2Counter[i] = 1

            elif s[4] == 'Guangdong':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Guangdong2Counter:
                                    Guangdong2Counter[j] += 1
                                else:
                                    Guangdong2Counter[j] = 1
                        elif i in Guangdong2Counter:
                            Guangdong2Counter[i] += 1
                        else:
                            Guangdong2Counter[i] = 1

            elif s[4] == 'Guangxi':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Guangxi2Counter:
                                    Guangxi2Counter[j] += 1
                                else:
                                    Guangxi2Counter[j] = 1
                        elif i in Guangxi2Counter:
                            Guangxi2Counter[i] += 1
                        else:
                            Guangxi2Counter[i] = 1

            elif s[4] == 'Guizhou':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Guizhou2Counter:
                                    Guizhou2Counter[j] += 1
                                else:
                                    Guizhou2Counter[j] = 1
                        elif i in Guizhou2Counter:
                            Guizhou2Counter[i] += 1
                        else:
                            Guizhou2Counter[i] = 1

            elif s[4] == 'Hokkaido':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in Hokkiado2Counter:
                                    Hokkiado2Counter[j] += 1
                                else:
                                    Hokkiado2Counter[j] = 1
                        elif i in Hokkiado2Counter:
                            Hokkiado2Counter[i] += 1
                        else:
                            Hokkiado2Counter[i] = 1
                            
            elif s[4] == 'Hong Kong':
                symptom = s[11]
                if symptom != "NaN":
                    symptom = symptom.split("; ")
                    for i in symptom:
                        if ";" in i:
                            i = i.split(";")  
                            for j in i:
                                if j in HongKong2Counter:
                                    HongKong2Counter[j] += 1
                                else:
                                    HongKong2Counter[j] = 1
                        elif i in HongKong2Counter:
                            HongKong2Counter[i] += 1
                        else:
                            HongKong2Counter[i] = 1
            else:
                print("oops")
    
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        with open('covidResult.csv','w',newline='') as csvout:
            writer = csv.writer(csvout)
            columns = next(reader)  
            writer.writerow(columns)
            for x in reader:
                if "-" in x[1]:
                    l = x[1].split("-")
                    x[1] = str(int((int(l[0]) + int(l[1])) /2 + 0.5))
                l = x[8].split(".")
                x[8] = l[1] + "." + l[0] + "." + l[2]
                l = x[9].split(".")
                x[9] = l[1] + "." + l[0] + "." + l[2]
                l = x[10].split(".")
                x[10] = l[1] + "." + l[0] + "." + l[2]
                
                if x[6] == 'NaN':
                    if x[4] == 'Aichi Prefecture':
                        x[6] = round(AichiPrefectureLatAvg, 2)
                    elif x[4] == 'Anhui':
                        x[6] = round(AnhuiLatAvg, 2)
                    elif x[4] == 'Beijing':
                        x[6] = round(BeijingLatAvg, 2)
                    elif x[4] == 'Gansu':
                        x[6] = round(GansuLatAvg, 2)
                    elif x[4] == 'Guangdong':
                        x[6] = round(GuangdongLatAvg, 2)
                    elif x[4] == 'Guangxi':
                        x[6] = round(GuangxiLatAvg, 2)
                    elif x[4] == 'Guizhou':
                        x[6] = round(GuizhouLatAvg, 2)
                    elif x[4] == 'Hokkaido':
                        x[6] = round(hokkiadoLatAvg, 2)
                    elif x[4] == 'Hong Kong':
                        x[6] = round(HongKongLatAvg, 2)

                if x[7] == 'NaN':
                    if x[4] == 'Aichi Prefecture':
                        x[7] = round(AichiPrefectureLongAvg, 2)
                    elif x[4] == 'Anhui':
                        x[7] = round(AnhuiLongAvg, 2)
                    elif x[4] == 'Beijing':
                        x[7] = round(BeijingLongAvg, 2)
                    elif x[4] == 'Gansu':
                        x[7] = round(GansuLongAvg, 2)
                    elif x[4] == 'Guangdong':
                        x[7] = round(GuangdongLongAvg, 2)
                    elif x[4] == 'Guangxi':
                        x[7] = round(GuangxiLongAvg, 2)
                    elif x[4] == 'Guizhou':
                        x[7] = round(GuizhouLongAvg, 2)
                    elif x[4] == 'Hokkaido':
                        x[7] = round(hokkiadoLongAvg, 2)
                    elif x[4] == 'Hong Kong':
                        x[7] = round(HongKongLongAvg, 2)

                if x[3] == 'NaN':
                    if x[4] == 'Aichi Prefecture':
                        x[3] = sorted(AichiCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Anhui':
                        x[3] = sorted(AnhuiCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Beijing':
                        x[3] = sorted(BeijingCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Gansu':
                        x[3] = sorted(GansuCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Guangdong':
                        x[3] = sorted(GuangdongCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Guangxi':
                        x[3] = sorted(GuangxiCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Guizhou':
                        x[3] = sorted(GuizhouCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Hokkaido':
                        x[3] = sorted(HokkiadoCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Hong Kong':
                        x[3] = sorted(HongKongCounter.items(), key=lambda k: (-k[1], k[0]))[0][0]

                if x[11] == 'NaN':
                    if x[4] == 'Aichi Prefecture':
                        x[11] = sorted(Aichi2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Anhui':
                        x[11] = sorted(Anhui2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Beijing':
                        x[11] = sorted(Beijing2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Gansu':
                        x[11] = sorted(Gansu2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Guangdong':
                        x[11] = sorted(Guangdong2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Guangxi':
                        x[11] = sorted(Guangxi2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Guizhou':
                        x[11] = sorted(Guizhou2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Hokkaido':
                        x[11] = sorted(Hokkiado2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                    elif x[4] == 'Hong Kong':
                        x[11] = sorted(HongKong2Counter.items(), key=lambda k: (-k[1], k[0]))[0][0]
                writer.writerow(x)
def main():
    replaceNaNs("covidTrain.csv")

if __name__ == "__main__":
    main()              