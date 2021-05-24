from .models import *

def getAllTerritories(request):
    return {'territories': Township.objects.all()} 

def getLastUpdate(request):
    return {'date': AcumulatedRegion.objects.all().order_by('-date',)[0].date}     