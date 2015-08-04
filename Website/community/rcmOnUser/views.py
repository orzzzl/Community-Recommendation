from django.shortcuts import render
from rcmOnUser.RcmSystem.makeRcm import makeRcm
# Create your views here.
def preference(request):
    sessionVal = None
    try:
        sessionVal = request.session ['firstRound']
    except:
        pass
    else:
        pass
    return render (request, 'preference.html', {'sessionVal': sessionVal})

def res(request):
    sessionVal = None
    try:
        sessionVal = request.session ['firstRound']
    except:
        pass
    else:
        pass
    choices = request.POST
    try:
        result = makeRcm(choices, sessionVal)
    except:
        return render(request, 'preference.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        request.session ['secondRound'] = result [1]
        return render(request, 'res.html', {'choices': choices, 'result': result [0] [0:9], 'sessionVal': sessionVal})
