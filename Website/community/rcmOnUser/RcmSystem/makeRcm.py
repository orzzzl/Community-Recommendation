__author__ = 'zelengzhuang'
from .dataCollect import dataCollect
from rcmOnFacts.RcmSystem.tools import cos2
from rcmOnUser.models import score


def makeRcm (input, sessionVal):
    choice = dataCollect(input) [0]
    attList = dataCollect(input) [1]
    subChoice = choice ['submitType']
    res = []
    resSimilarityOnly = []
    for i in score.objects.all():
        if i.money < choice ['costLow'] or i.money > choice ['costHigh']:
            simlarity = 0
        else:
            simlarity = float("{0:3.03f}".format(cos2(i, choice, attList)))

        simlarityFirstRound = 0
        if subChoice == 1:
            for j in sessionVal:
                if j ['zip'] == i.zipCode:
                    simlarityFirstRound = j ['simlarity']
                    break

        tmp = {
            'zipThing': i,
            'simlarity': simlarity
        }
        if subChoice == 1:
            tmp ['simlarityFirstRound'] = simlarityFirstRound

        tmpNew = {
            'zip': i.zipCode,
            'simlarity': simlarity
        }
        res.append(tmp)
        resSimilarityOnly.append(tmpNew)
    if subChoice == 2:
        res.sort(key=lambda zipObj: zipObj ["simlarity"], reverse=True)
    else:
        res.sort(key=lambda zipObj: zipObj ["simlarity"] + zipObj ["simlarityFirstRound"], reverse=True)
    resSimilarityOnly.sort(key=lambda zipObj: zipObj ["simlarity"], reverse=True)
    ret = (res, resSimilarityOnly)
    return ret