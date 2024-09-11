from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306226233',
        'name': 'Pradipta Wachyu Aditama',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
