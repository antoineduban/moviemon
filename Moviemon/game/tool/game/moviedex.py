from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import elements as e
from .data import Data
from .elem import Text
import os

class Moviedex(Data):
    marker = 0
    def __init__(self):
        i = 0
        content = []
        m = self.get_movies()
        for elem in m:
            if i == Moviedex.marker: 
                content.append(Text('==> '))
            content.append(Text(elem['title'] + "<br/>"))
            i += 1
        content.append(Text('<br/>A - Detail<br/>Select - Quit</br>'))
        self.moviedex = e.Div(content, attr={'class':'containter'})
    def __str__(self):
        return str(self.moviedex)

class Movie(Data):
    def __init__(self, movie):
        content = []
        self.movie = self.get_movie(movie.replace("_", " "))
        content.append(Text(str(self.movie)))
        content.append(Text('<br/>B - Back<br/>'))
        self.movie = e.Div(content, attr={'class':'containter'})
    def __str__(self):
        return str(self.movie)


def movie_render(request, moviemon):
        if (request.method == 'POST'):
            if 'B' in request.POST:
                return HttpResponseRedirect('/moviedex')
        return render(request, "game/movie.html", {'movie': Movie(moviemon)})

def moviedex_render(request):
        m = Moviedex()
        if (request.method == 'POST'):
            if 'Down' in request.POST and Moviedex.marker < len(m.get_movies()) - 1:
                Moviedex.marker += 1
                return render(request, "game/moviedex.html", {'moviedex': Moviedex()})
            if 'Up' in request.POST and Moviedex.marker > 0:
                Moviedex.marker -= 1
                return render(request, "game/moviedex.html", {'moviedex': Moviedex()})
            if 'A' in request.POST:
                m = Moviedex()
                return HttpResponseRedirect('/moviedex/'+ m.movies[Moviedex.marker]['title'].replace(" ", "_"))
            if 'Select' in request.POST:
                return HttpResponseRedirect('/worldmap')
        return render(request, "game/moviedex.html", {'moviedex': Moviedex()})



