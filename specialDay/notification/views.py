from django.shortcuts import render

app_name = "nofitication"
def notification(request):
    return render(request, "notification/index.html")
