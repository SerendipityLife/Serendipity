from django.shortcuts import render
from django.http import HttpResponse
from status.models import TestDb


def index(request):
    return HttpResponse('Hello, world. You\'re at the status index.')

def insertTestDb(request):
    name = request.GET.get('name')
    TestDb(name=name).save()
    return render(request, 'status/test.html', {'testDb': 'inserted Status Data -> ' + name})