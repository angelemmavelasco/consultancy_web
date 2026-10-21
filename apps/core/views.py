from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'core/index.html'
    context = {
        'user': "Angel Velasco"
    }
    return render(request, template, context)