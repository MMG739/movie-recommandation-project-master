from django.shortcuts import render
from movie_test.models import Media,Movie,Series

# Create your views here.
def home(request):
    media = Media.objects.all()
    return render(request, 'home.html', {'Media':media,'test':media[0],'test2':media[0].get_img(),'test3':media[0].get_average_rating()})

def films(request):
    media = Movie.objects.all()
    return render(request, 'films.html',{'Media':media})

def series(request):
    media = Series.objects.all()
    return render(request, 'series.html',{'Media':media})

def film_detail(request, Media_id):
    media = Media.objects.get(id=Media_id)
    return render(request, 'media_detail.html', {'Media': media})
def film_genre(request, movie_genre):
    media = Media.objects.filter(genre=movie_genre)
    return render(request, 'media_genre.html', {'Media': media})
def film_year(request, movie_year):
    media = Media.objects.filter(year=movie_year)
    return render(request, 'media_year.html', {'Media': media})

# def film_detail(request, Media_id):
#     media = Media.objects.get(id=Media_id)
#     average_rating = media.get_average_rating()
#     return render(request, 'media_detail.html', {'media': media, 'average_rating': average_rating})

def contact(request):
    return render(request, 'contact.html')

# from django.shortcuts import redirect
# from .models import Rating

# def add_rating(request, Media_id):
#     if request.method == 'POST':
#         rating = request.POST.get('rating')
#         Rating.objects.create(media_id=Media_id, rating=rating)
#     return redirect('film_detail', Media_id=Media_id)
