__author__ = 'zelengzhuang'

import json
modName = 'rcmOnFacts.cityData'
InputFileName = '/Users/zelengzhuang/Defiled_Katty/CityDataCrawler/out.json'
OutputFileName = 'cityData.json'

def getNum (strNum):
    res = ""
    for i in xrange (len (strNum)):
        tmp = strNum [i]
        if (tmp == ' ' or tmp == ',' or tmp == '$'):
            continue
        if (tmp.isdigit () or tmp == '.'):
            res += tmp
        else:
            break
    return res

def round (number):
    return float("{0:3.03f}".format(number))


pknum = 0
res = []
fin = open (InputFileName, 'r')
inJson = json.load(fin)
for i in inJson:
    pknum += 1
    t = {}
    fieldTmp = {}

    #######################Male or Female
    strM = i ['males']
    strW = i ['females']
    numM = int (getNum(strM.strip()))
    numW = int (getNum(strW.strip()))
    sums = numM + numW
    fieldTmp ['zipCode'] = i ['zip'].strip()
    fieldTmp ['malePercentage'] = round ((numM + 0.0) / sums)
    fieldTmp ['femalePercentage'] = round ((numW + 0.0) / sums)

    #######################Marriage
    strNeverm = i ['neverm']
    strWidow = i ["widowed"]
    strNowm = i ["nowm"]
    strSep = i ["seperated"]
    strDivorced = i ["divorced"]
    try:
        numNeverm = float (getNum(strNeverm))
        numWidow = float (getNum(strWidow))
        numNowm = float (getNum(strNowm))
        numSep = float (getNum(strSep))
        numDivorced = float (getNum(strDivorced))
        sumsOfMarr = numWidow + numNeverm + numDivorced + numNowm + numSep
        assert (sumsOfMarr != 0)
    except (Exception):
        print pknum
        print "$$$$$$$$$$$$"
    else:
        sumsOfMarr = numWidow + numNeverm + numDivorced + numNowm + numSep
        fieldTmp ['neverMarried'] = round (numNeverm / sumsOfMarr)
        fieldTmp ['nowMarried'] = round (numNowm / sumsOfMarr)
        fieldTmp ['seperated'] = round (numSep / sumsOfMarr)
        fieldTmp ['divorced'] = round (numDivorced / sumsOfMarr)
        fieldTmp ['widowed'] = round (numWidow / sumsOfMarr)

    #########################Races
    strwhite = i ['wp']
    strblack = i ['bp']
    stramericanindian = i ['aip']
    strasian = i ['ap']
    strhispanic = i ['holp']
    strhawaiian = i ['nhaopip']
    strtwoormore = i ['tomrp']
    strother = i ['sorp']
    try:
        numwhite = float (getNum(strwhite))
        numblack = float (getNum(strblack))
        numamericanindian = float (getNum(stramericanindian))
        numasian = float (getNum(strasian))
        numhispanic = float (getNum(strhispanic))
        numhawaiian = float (getNum(strhawaiian))
        numtwoormore = float (getNum(strtwoormore))
        numother = float (getNum(strother))
        sumsOfRaces = numwhite + numblack + numamericanindian + numasian + numhispanic + numhawaiian + numtwoormore + numother
        assert (sumsOfRaces != 0)
    except (Exception):
        print "race exception"
    else:
        fieldTmp ['white'] = round (numwhite / sumsOfRaces)
        fieldTmp ['black'] = round (numblack / sumsOfRaces)
        fieldTmp ['americanIndian'] = round (numamericanindian / sumsOfRaces)
        fieldTmp ['asian'] = round (numasian / sumsOfRaces)
        fieldTmp ['hispanic'] = round (numhispanic / sumsOfRaces)
        fieldTmp ['hawaiian'] = round (numhawaiian / sumsOfRaces)
        fieldTmp ['twoOrMore'] = round (numtwoormore / sumsOfRaces)
        fieldTmp ['otherRace'] = round (numother / sumsOfRaces)

    ############################Sex Orient
    gay = i ['gm']
    lesbian = i ['lc']
    try:
        gaynum = float (getNum(gay))
        lesbiannum = float (getNum(lesbian))
    except (Exception):
        print "sex exception"
    else:
        fieldTmp ['gay'] = round (gaynum)
        fieldTmp ['lesbian'] = round (lesbiannum)

    ############################Rent or Buy
    rent = i ['roa']
    totalhouse = i ['hac']
    try:
        rentNum = float (getNum(rent))
        totalhouseNum = float (getNum(totalhouse))
    except (Exception):
        print "rent or buy exception"
    else:
        fieldTmp ['rent'] = round (rentNum / totalhouseNum)
        fieldTmp ['buy'] = round (1 - fieldTmp ['rent'])


    ############################Education
    highschool = i ['hsoh']
    bachelor = i ['bdoh']
    master = i ['gopd']
    try:
        noedunum = 1 - float (getNum(highschool)) / 100
        highNum = float (getNum(highschool)) / 100 - float (getNum(bachelor)) / 100
        bachelorNum = float(getNum(bachelor)) / 100 - float (getNum(master)) / 100
        masterNum = float (getNum(master)) / 100
    except (Exception):
        print "education exception"
    else:
        fieldTmp ['noEducation'] = round (noedunum)
        fieldTmp ['highSchool'] = round (highNum)
        fieldTmp ['bachelor'] = round (bachelorNum)
        fieldTmp ['master'] = round (masterNum)
    ############################price
    strMM = i ['mmocfuwithoutam']
    try:
        numMM = int (getNum (strMM))
    except:
        print "failed" + i ['zip']
    else:
        fieldTmp ['money'] = numMM
    t ["fields"] = fieldTmp
    t ["model"] = modName
    t ["pk"] = pknum
    res.append(t)
fout = open (OutputFileName, 'w')
json.dump(res, fout, indent=2)