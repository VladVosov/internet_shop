from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        viewport = request.POST.get('viewport')

    return render(request, 'catalog/index.html')
