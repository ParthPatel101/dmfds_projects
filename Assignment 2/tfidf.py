import re
from collections import Counter
import math

def preProcess(f):
    with open(f) as file:
        stopList = ['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did','not','now','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']
        lines = file.readlines()
        for line in lines:
            datafile = line
            datafile = datafile.replace("\n", "")
            with open(datafile) as df:
                data = df.read()
                data =re.sub('\n',' ', data)
                data =re.sub('[^a-zA-Z0-9_ ]','', data)
                data =re.sub(' {1,}',' ', data)
                data =re.sub('http[A-Za-z0-9]*com', '', data)
                data = data.lower()
                s = data.split()
                for i in stopList:
                    if i in s:
                        try:
                            while True:
                                s.remove(i)
                        except ValueError:
                            pass
                for i in range(0, len(s)):
                    if s[i][-3::1] == 'ing':
                        s[i] = s[i][:-3:1]
                    elif s[i][-2::1] == 'ly':
                        s[i] = s[i][:-2:1]
                    elif s[i][-4::1] == 'ment':
                        s[i] = s[i][:-4:1]
                data = ' '.join(s)
                with open("preproc_" + datafile, 'w') as file:
                    file.write(data)
                TF = dict(Counter(s))
                for i in TF.keys():
                    TF[i] = (TF[i]/len(s))
                
                IDF = {}
                for i in TF.keys():
                    numDocsWordIsIn = 0
                    for line in lines:
                        ddd = line
                        ddd = ddd.replace("\n", "")
                        with open(ddd) as df:
                            z = df.read()
                            z = re.sub('\n',' ', z)
                            z = re.sub('[^a-zA-Z0-9_ ]','', z)
                            z = re.sub(' {1,}',' ', z)
                            z = re.sub('http[A-Za-z0-9]*com', '', z)
                            z = z.lower()
                            if i in z:
                                numDocsWordIsIn += 1
                    IDF[i] = (math.log((len(lines) / numDocsWordIsIn)) + 1)
                TFXIDF = {}
                for i in IDF.keys():
                    TFXIDF[i] = round(TF[i] * IDF[i], 2)
                sortedTFXIDF = {k: v for k, v in sorted(TFXIDF.items(), key=lambda item: (item[1], item[0]), reverse = True)}
                uniqueValues = sorted(set(sortedTFXIDF.values()), reverse = True)
                MostImportantFiveWords = []
                for val in uniqueValues:
                    s = sorted([k for k,v in sortedTFXIDF.items() if v == val])
                    for i in s:
                        if len(MostImportantFiveWords) < 5:
                            MostImportantFiveWords.append(i)
                        else:
                            break
                    if len(MostImportantFiveWords) >= 5:
                        break
                with open("tfidf_" + datafile, 'w') as file:
                    l = []
                    for i in MostImportantFiveWords:
                        l.append((i,TFXIDF[i]))
                    print(l, file = file)

def main():
    preProcess("tfidf_docs.txt")

if __name__ == "__main__":
    main() 