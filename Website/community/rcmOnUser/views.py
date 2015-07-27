from django.shortcuts import render

# Create your views here.
def preference(request):
    return render (request, 'preference.html')

def res(request):
    choices = request.POST
    return render(request, 'res.html', {'res': choices})
