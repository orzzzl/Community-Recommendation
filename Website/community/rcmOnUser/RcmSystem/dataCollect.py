__author__ = 'zelengzhuang'

def dataCollect (input):
    a = {}
    sums = 0
    attList = ['school', 'eating', 'shopping', 'health', 'transportation', 'security']
    for i in input.keys ():
        try:
            a [i] = eval (input [i])
        except:
            pass
        else:
            if i in attList:
                sums += a [i]
    assert sums != 0
    for i in attList:
        a [i] = float (a [i]) / sums
    a ["costLow"] = a ['cost'] [0]
    a ["costHigh"] = a ['cost'] [1]
    return  (a, attList)
