from django.shortcuts import render

def getunban(request):
    return render(request, "getunban/index.html")
