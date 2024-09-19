from django.shortcuts import render

def main_view(request):
    return render(request, 'testapp1\main.html')

def movie_view(request):
    head_msg = "welcome to movie news"
    m1 = "alia and ranveer gets married"
    m2 = " Munja movie is comming soon"
    type = "movies"
    my_dict = {"head_msg":head_msg, "m1":m1, "m2":m2, "type":type}
    return render(request, 'testapp1\movie.html', my_dict)

def sports_view(request):
    head_msg = "welcome to sport news"
    m1 = "alia and ranveer gets married"
    m2 = " Munja movie is comming soon"
    type = "sports"
    my_dict = {"head_msg":head_msg, "m1":m1, "m2":m2, "type":type}
    return render(request, 'testapp1\movie.html', my_dict)

def politics_view(request):
    head_msg = "welcome to politics news"
    m1 = "alia and ranveer gets married"
    m2 = " Munja movie is comming soon"
    type = "politics"
    my_dict = {"head_msg":head_msg, "m1":m1, "m2":m2, "type":type}
    return render(request, 'testapp1\movie.html', my_dict)