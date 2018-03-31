from django.shortcuts import render


def index(request):
    if request.user.is_anonymous:
        return render(request,
                      'SelectGame/index-anonymous.html',
                      {})
    else:
        return render(request,
                      'SelectGame/index.html',
                      {})
