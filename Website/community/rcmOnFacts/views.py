from django.shortcuts import render

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