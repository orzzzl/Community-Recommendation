from django.shortcuts import get_object_or_404, render
from .models import sat
from rcmOnFacts.RcmSystem.rcmAlgorithm import algorithm


# Create your views here.
def index(request):
    return render(request, 'rcmfacts/index.html')

def questions(request):
    sessionVal = None
    try:
        sessionVal = request.session ['secondRound']
    except:
        pass
    else:
        pass
    return render(request, 'rcmfacts/questions.html', {'sessionVal': sessionVal})

def res(request):
    sessionVal = None
    try:
        sessionVal = request.session ['secondRound']
    except:
        pass
    else:
        pass
    choices = request.POST
    try:
        res = algorithm.rcmdtion (choices, sessionVal)
    except (Exception):
        return render(request, 'rcmfacts/questions.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        request.session ['firstRound'] = res [1]
        return render(request, 'rcmfacts/res.html', {'res': res [0] [0 : 9], "choices": choices})

def contact (request):
    return  render (request, 'rcmfacts/contact.html')

def satisfaction1 (request):
    return  render (request, 'rcmfacts/satisfaction1.html')

def satisfaction2 (request):
    return  render (request, 'rcmfacts/satisfaction2.html')

def satisfaction3 (request):
    return  render (request, 'rcmfacts/satisfaction3.html')

def thankyou (request):
    answer = request.POST ['submitType']
    a = int (answer [0])
    b = int (answer [1])
    selectedRcm = get_object_or_404(sat, pk=a)
    if b == 1:
        selectedRcm.sat += 1
    else:
        selectedRcm.nosat += 1
    selectedRcm.save()
    res = {}
    tmpRcm = get_object_or_404(sat, pk=1)
    res ['firstSat'] = tmpRcm.sat
    res ['firstNoSat'] = tmpRcm.nosat
    res ['firstRate'] = float("{0:3.03f}".format((tmpRcm.sat + 0.0) / (tmpRcm.sat + tmpRcm.nosat)))
    tmpRcm = get_object_or_404(sat, pk=2)
    res ['secondSat'] = tmpRcm.sat
    res ['secondNoSat'] = tmpRcm.nosat
    res ['secondRate'] = float("{0:3.03f}".format((tmpRcm.sat + 0.0) / (tmpRcm.sat + tmpRcm.nosat)))
    tmpRcm = get_object_or_404(sat, pk=3)
    res ['thirdSat'] = tmpRcm.sat
    res ['thirdNoSat'] = tmpRcm.nosat
    res ['thirdRate'] = float("{0:3.03f}".format((tmpRcm.sat + 0.0) / (tmpRcm.sat + tmpRcm.nosat)))
    return  render (request, 'rcmfacts/thankyou.html', {'pollRes': res})