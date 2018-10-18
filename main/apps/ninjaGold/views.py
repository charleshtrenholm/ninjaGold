from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'points' not in request.session: 
        request.session['points'] = 0
    if 'data' not in request.session: 
        request.session['data'] = []

    context = {
        'data': request.session['data'],
        'points': request.session['points']
        }
    return render(request, "ninjaGold/index.html", context)

def process(request):
    if request.POST['source'] == 'farm':
        points = random.randint(10,20)
        request.session['points'] += points
        print(points, request.session['points'])

    elif request.POST['source'] =='cave':
        points = random.randint(5,10)
        request.session['points'] += points
        print(points, request.session['points'])

    elif request.POST['source'] == 'house':
        points = random.randint(2,5)
        request.session['points'] += points
        print(points, request.session['points'])

    else:
        points = int(random.uniform(-50,50))
        request.session['points'] += points 
        print(points, request.session['points'])
    
    data= {
        'source': request.POST['source'],
        'points': points,
        'time': strftime("%Y/%m/%d %-I:%M:%S %p", gmtime())
    }
    temp_list = request.session['data']
    temp_list.insert(0, data)
    request.session['data'] = temp_list
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')