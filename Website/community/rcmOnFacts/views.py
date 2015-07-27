from django.shortcuts import render

from rcmOnFacts.RcmSystem.rcmAlgorithm import algorithm


# Create your views here.
def index(request):
    return render(request, 'rcmfacts/index.html')

def questions(request):
    return render(request, 'rcmfacts/questions.html')

def res(request):
    choices = request.POST
    try:
        res = algorithm.rcmdtion (choices)
    except (Exception):
        return render(request, 'rcmfacts/questions.html', {
            'error_message': "You didn't select a choice.",
        })
    else:
        return render(request, 'rcmfacts/res.html', {'res': res, "choices": choices})