__author__ = 'zelengzhuang'

from rcmOnFacts.RcmSystem.tools import cos
from rcmOnFacts.models import cityData

class algorithm:
    @staticmethod
    def rcmdtion (input):
        gender = int (input ['gender'])
        marriage = int (input ['marriage'])
        race = int (input ['race'])
        if gender == 1:
            target = {
                'malePercentage': 0,
                'femalePercentage': 1
            }
        elif gender == 2:
            target = {
                'malePercentage': 0.5,
                'femalePercentage': 0.5
            }
        else:
            target = {
                'malePercentage': 1,
                'femalePercentage': 0
            }
        if marriage == 1:
            target ['neverMarried'] = 1
            target ['nowMarried'] = 0
            target ['seperated'] = 0
            target ['divorced'] = 0
            target ['widowed'] = 0
        elif marriage == 2:
            target ['neverMarried'] = 0
            target ['nowMarried'] = 1
            target ['seperated'] = 0
            target ['divorced'] = 0
            target ['widowed'] = 0
        elif marriage == 3:
            target ['neverMarried'] = 0
            target ['nowMarried'] = 0
            target ['seperated'] = 1
            target ['divorced'] = 0
            target ['widowed'] = 0
        elif marriage == 4:
            target ['neverMarried'] = 0
            target ['nowMarried'] = 0
            target ['seperated'] = 0
            target ['divorced'] = 1
            target ['widowed'] = 0
        elif marriage == 5:
            target ['neverMarried'] = 0
            target ['nowMarried'] = 0
            target ['seperated'] = 0
            target ['divorced'] = 0
            target ['widowed'] = 1
        elif marriage == 6:
            target ['neverMarried'] = 0.2
            target ['nowMarried'] = 0.2
            target ['seperated'] = 0.2
            target ['divorced'] = 0.2
            target ['widowed'] = 0.2

        if race == 1:
            target ['white'] = 1
            target ['black'] = 0
            target ['americanIndian'] = 0
            target ['asian'] = 0
            target ['hispanic'] = 0
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 0
            target ['otherRace'] = 0
        elif race == 2:
            target ['white'] = 0
            target ['black'] = 1
            target ['americanIndian'] = 0
            target ['asian'] = 0
            target ['hispanic'] = 0
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 0
            target ['otherRace'] = 0
        elif race == 3:
            target ['white'] = 0
            target ['black'] = 0
            target ['americanIndian'] = 1
            target ['asian'] = 0
            target ['hispanic'] = 0
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 0
            target ['otherRace'] = 0
        elif race == 4:
            target ['white'] = 0
            target ['black'] = 0
            target ['americanIndian'] = 0
            target ['asian'] = 1
            target ['hispanic'] = 0
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 0
            target ['otherRace'] = 0
        elif race == 5:
            target ['white'] = 0
            target ['black'] = 0
            target ['americanIndian'] = 0
            target ['asian'] = 0
            target ['hispanic'] = 1
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 0
            target ['otherRace'] = 0
        elif race == 6:
            target ['white'] = 0
            target ['black'] = 0
            target ['americanIndian'] = 0
            target ['asian'] = 0
            target ['hispanic'] = 0
            target ['hawaiian'] = 1
            target ['twoOrMore'] = 0
            target ['otherRace'] = 0
        elif race == 7:
            target ['white'] = 0
            target ['black'] = 0
            target ['americanIndian'] = 0
            target ['asian'] = 0
            target ['hispanic'] = 0
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 1
            target ['otherRace'] = 0
        elif race == 8:
            target ['white'] = 0
            target ['black'] = 0
            target ['americanIndian'] = 0
            target ['asian'] = 0
            target ['hispanic'] = 0
            target ['hawaiian'] = 0
            target ['twoOrMore'] = 0
            target ['otherRace'] = 1

        assert (len (target.keys()) == 15)
        res = []
        for i in cityData.objects.all():
            simlarity = float("{0:3.03f}".format(cos(i, target, target.keys())))
            tmp = {
                'zipThing': i,
                'simlarity': simlarity
            }
            res.append(tmp)
        res.sort(key=lambda zipObj: zipObj ["simlarity"], reverse=True)
        return res [0: 10]

