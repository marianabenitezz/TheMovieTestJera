import requests
import json
from PIL import Image
from io import BytesIO

https = 'https://api.themoviedb.org/3/'
api_key = '?api_key=e11e8b1786788ea384c7accb4d9e5d92'

# 'id'
# 'original_title'
# 'overview'
# 'poster_path'
# 'release_date'
# 'vote_average'


def buscarFilme(palavra):
    filmes = []
    if palavra == '':
        return filmes

    else:
        search_query = https + 'search/movie' + api_key + '&language=en-US&page=1&query='
        f = search_query + palavra
        req = requests.get(f).json()["results"]
        for i in range(len(req)):
            filmes.append(req[i])

    return filmes


def buscarFilmesMaisPopulares():
    req = requests.get(https + 'movie/popular' + api_key).json()['results']

    filmesMaisPopulares = []
    for i in range(len(req)):
        filmesMaisPopulares.append(req[i])

    return filmesMaisPopulares


def buscarRecomendacao(id):
    req = requests.get(https + 'movie/' + str(id) + '/recommendations' +
                       api_key).json()['results']
    recomendacoes = []
    for i in range(len(req)):
        recomendacoes.append(req[i])

    return recomendacoes


def buscarFilmeSimilar(movie_id):
    req = requests.get(https + 'movie/' + movie_id + '/similar' +
                       api_key).json()['results']
    similares = []
    for i in range(len(req)):
        similares.append(req[i])
    return req


def buscarImagem(path):
    response = requests.get(https + 't/p/original' + path)
    img = Image.open(BytesIO(response.content))

    return img