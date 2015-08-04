__author__ = 'zelengzhuang'


def cos (first, second, attributes):
    firstVal = 0
    secondVal = 0
    mutualVal = 0
    for attr in attributes:
        if not hasattr(first, attr):
            continue
        t = getattr(first, attr)
        firstVal += t * t
        secondVal += second [attr] * second [attr]
        mutualVal += t * second [attr]
    if (firstVal * secondVal) == 0:
        return 0
    return  (mutualVal + 0.0) * mutualVal / (firstVal * secondVal)

def cos2 (first, second, attributes):
    firstVal = 0
    secondVal = 0
    mutualVal = 0
    for attr in attributes:
        if not hasattr(first, attr):
            continue
        t = getattr(first, attr)
        firstVal += t * t
        secondVal += second [attr] * second [attr]
        mutualVal += t * second [attr]
    if (firstVal * secondVal) == 0:
        return 0
    return  (mutualVal + 0.0)


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