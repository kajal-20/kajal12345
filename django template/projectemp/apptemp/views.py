from django.shortcuts import render


# Create your views here.
def firstemplate(request):
    template_name = "test.html"
    context= {}

    return render(request,template_name,context)