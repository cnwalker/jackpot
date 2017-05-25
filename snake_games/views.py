from django.shortcuts import render

# Create your views here.
def IndexView(request):
    context = {
        'active_script': 'basic_snake.js',
        'link_one': '/rewards/',
        'link_two': '/mechanics/'
    }
    return render(request, 'snake_games/index.html', context)

def RewardView(request):
    context = {
        'active_script': 'reward_snake.js',
        'link_one': '/',
        'link_two': '/mechanics/'
    }
    return render(request, 'snake_games/index.html', context)

def MechanicsView(request):
    context = {
        'active_script': 'mechanics_snake.js',
        'link_one': '/rewards/',
        'link_two': '/mechanics/'
    }
    return render(request, 'snake_games/index.html', context)
