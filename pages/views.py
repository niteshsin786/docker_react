from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def about(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def home_view(request, *args, **kwargs):
    count_title = []
    count_link = []
    request1 = requests.get(
        'https://api.stackexchange.com/2.2/questions?pagesize=20&order=desc&sort=activity&site=stackoverflow')
    for x in request1.json()['items']:
        if x['answer_count'] == 0:
            a = x['title']
            b = x['link']
            count_title.append(a)
            count_link.append(b)
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dictionary = dict(zip(count_title, count_link))
    return render(request, "about.html", {'dictionary': dictionary})


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")