from django.shortcuts import render

categoryList = ["Adventure","Romantic","Tragedy","Science Fiction","Horror"]
filmList = [
    {
        "filmName" : "American Horror Story",
        "explanation" : "Horror IMDB:8.0",
        "image" : "americanhorror.jpeg",
        "homepage":True
    },
    {
        "filmName" : "Avatar",
        "explanation" : "Adventure IMDB:7.0",
        "image" : "avatar.jpeg",
        "homepage":False
    },
    {
        "filmName" : "Ayla",
        "explanation" : "Tragedy IMDB:7.5",
        "image" : "ayla.jpeg",
        "homepage":False
    },
    {
        "filmName" : "Joker",
        "explanation" : "Science Fiction IMDB:9.0",
        "image" : "joker.jpeg",
        "homepage":True
    }
    ]

def home (request): 
    data = {
        "categories": categoryList,
        "films" : filmList
    }
    return render(request,"index.html", data)

def movies (request):
    data = {
        "categories": categoryList,
        "films" : filmList
    }
    return render(request,"movies.html", data)
