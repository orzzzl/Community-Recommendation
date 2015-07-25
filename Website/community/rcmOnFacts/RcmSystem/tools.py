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
    return  (mutualVal + 0.0) * mutualVal / (firstVal * secondVal)