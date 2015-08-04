__author__ = 'zelengzhuang'

import json
modName = 'rcmOnUser.price'
InputFileName = '/Users/zelengzhuang/Defiled_Katty/CityDataCrawler/out.json'
OutputFileName = 'score.json'
clinic = 'clinic_score.json'
preschool = 'preschool_score.json'
crime = 'crime.json'
shopping = 'shopping.json'
eating = 'eating.json'

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

pknum = 1
res = []
fs = open (shopping, 'r')
fin = open (InputFileName, 'r')
fc = open (clinic, 'r')
fp = open (preschool, 'r')
fcrime = open (crime, 'r')
fe = open (eating, 'r')
eatingJson = json.load (fe)
cJson = json.load (fc)
pJson = json.load (fp)
inJson = json.load(fin)
shoppingJson = json.load (fs)
crimeJson = json.load (fcrime)
min = 99999999
for i in inJson:
    t = {}
    fieldTmp = {}
    fieldTmp ['zipCode'] = i ['zip'].strip()
    ziptar = int (fieldTmp ['zipCode'])
    ############################time to work
    timeStr = i ['mtttw']
    try:
        numTime = float (getNum(timeStr))
        assert (numTime != 0)
    except:
        print "time fail"
    else:
        fieldTmp ['transportation'] = (0.0 + 1) / (numTime / 21.4)
        min = numTime if numTime < min else min
    ############################price
    strMM = i ['mmocfuwithoutam']
    try:
        numMM = int (getNum (strMM))
    except:
        print "failed" + i ['zip']
    else:
        fieldTmp ['money'] = numMM

    ############################clinic
    clinicOk = 0
    for j in cJson:
        if int (j ['fields'] ['zipcode']) != ziptar:
            continue
        else:
            clinicOk = 1
            fieldTmp ['health'] = j ['fields'] ['score']
            fieldTmp ['clinicNumber'] = j ['fields'] ['totalNo']
    if clinicOk == 0:
        print ziptar
    
    ###########################preschool
    preschoolOk = 0
    for j in pJson:
        if int (j ['fields'] ['zipcode']) != ziptar:
            continue
        else:
            preschoolOk = 1
            fieldTmp ['school'] = j ['fields'] ['score']
            fieldTmp ['preschoolNumber'] = j ['fields'] ['totalNo']
    if preschoolOk == 0:
        print ziptar

    ###########################crime
    crimeOk = 0
    for j in crimeJson:
        if int (j ['fields'] ['zipcode']) != ziptar:
            continue
        else:
            crimeOk = 1
            fieldTmp ['security'] = float (j ['fields'] ['score'])
    if crimeOk == 0:
        print "crime" + str (ziptar)

    ###########################shopping
    shoppingOk = 0
    for j in shoppingJson:
        if int (j ['fields'] ['zipcode']) != ziptar:
            continue
        else:
            shoppingOk = 1
            fieldTmp ['shopping'] = float (j ['fields'] ['score'])
    if shoppingOk == 0:
        print "shopping" + str (ziptar)
        
    ###########################eating
    eatingOk = 0
    for j in eatingJson:
        if int (j ['fields'] ['zipcode']) != ziptar:
            continue
        else:
            eatingOk = 1
            fieldTmp ['eating'] = float (j ['fields'] ['score'])
    if eatingOk == 0:
        print "eating" + str (ziptar)
            
    t ["fields"] = fieldTmp
    t ["model"] = modName
    t ["pk"] = pknum
    res.append(t)
    pknum += 1
fout = open (OutputFileName, 'w')
json.dump(res, fout, indent=2)
print min