from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request, 'snake_games/index.html', {'message': 'Hello World!'})
