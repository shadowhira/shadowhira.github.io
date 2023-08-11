from django.shortcuts import render

def happy(request):
    return render(request, "happy/index.html")
