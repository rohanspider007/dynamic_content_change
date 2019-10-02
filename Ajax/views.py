from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


a = 1
def add(request):
    global a
    if a <= 5:
        a = a+1
    price = 50 * a
    return render(request, 'dataload.html', {'a': a, 'price': price})

def sub(request):
    global a
    a = a-1
    if a <= 1:
        a = 1
    price = 50 * a
    return render(request, 'dataload.html', {'a': a, 'price': price})

