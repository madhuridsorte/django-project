from django.shortcuts import render

def test_view(request):
    brands = {'1':'Madhuri','2':'Rani','3':'Meena'}
    return render(request, 'templates/testapp/main.html', brands)