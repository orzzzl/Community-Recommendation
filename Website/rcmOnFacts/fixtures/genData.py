__author__ = 'zelengzhuang'

import json
modName = 'rcmOnFacts.cityData'
InputFileName = '/Users/zelengzhuang/Defiled_Katty/CityDataCrawler/out.json'
OutputFileName = 'cityData.json'


def getNum (strNum):
    res = ""
    for i in xrange (len (strNum)):
        tmp = strNum [i]
        if (tmp == ' ' or tmp == ','):
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

    t ["fields"] = fieldTmp
    t ["model"] = modName
    t ["pk"] = pknum
    res.append(t)

fout = open (OutputFileName, 'w')
json.dump(res, fout, indent=2)