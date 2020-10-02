from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to render bag contents page """

    return render(request, 'bag/bag.html')
