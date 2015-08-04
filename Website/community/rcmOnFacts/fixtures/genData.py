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
    fieldTmp ['malePercentage'] = (numM + 0.0) / sums
    fieldTmp ['femalePercentage'] = (numW + 0.0) / sums

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
        fieldTmp ['neverMarried'] = numNeverm / sumsOfMarr
        fieldTmp ['nowMarried'] = numNowm / sumsOfMarr
        fieldTmp ['seperated'] = numSep / sumsOfMarr
        fieldTmp ['divorced'] = numDivorced / sumsOfMarr
        fieldTmp ['widowed'] = numWidow / sumsOfMarr

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
        fieldTmp ['white'] = numwhite / sumsOfRaces
        fieldTmp ['black'] = numblack / sumsOfRaces
        fieldTmp ['americanIndian'] = numamericanindian / sumsOfRaces
        fieldTmp ['asian'] = numasian / sumsOfRaces
        fieldTmp ['hispanic'] = numhispanic / sumsOfRaces
        fieldTmp ['hawaiian'] = numhawaiian / sumsOfRaces
        fieldTmp ['twoOrMore'] = numtwoormore / sumsOfRaces
        fieldTmp ['otherRace'] = numother / sumsOfRaces

    ############################Sex Orient
    gay = i ['gm']
    lesbian = i ['lc']
    try:
        gaynum = float (getNum(gay))
        lesbiannum = float (getNum(lesbian))
    except (Exception):
        print "sex exception"
    else:
        fieldTmp ['gay'] = gaynum
        fieldTmp ['lesbian'] = lesbiannum

    ############################Rent or Buy
    rent = i ['roa']
    totalhouse = i ['hac']
    try:
        rentNum = float (getNum(rent))
        totalhouseNum = float (getNum(totalhouse))
    except (Exception):
        print "rent or buy exception"
    else:
        fieldTmp ['rent'] = rentNum / totalhouseNum
        fieldTmp ['buy'] = 1 - fieldTmp ['rent']


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
        fieldTmp ['noEducation'] = noedunum
        fieldTmp ['highSchool'] = highNum
        fieldTmp ['bachelor'] = bachelorNum
        fieldTmp ['master'] = masterNum
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